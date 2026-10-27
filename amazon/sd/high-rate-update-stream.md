# System Design: High-Rate Inventory Update Stream (Duplicates and Out-of-Order Events)

**Prompt:** "Inventory updates arrive at tens of thousands per second from many sources. Some are
duplicated, some arrive out of order. Keep an accurate current count and serve it."  
**Source:** 📣 Sep 2026 ([Reddit](https://www.reddit.com/r/OfferEngineering/comments/1wm2krn/))

> **What they're testing:** there are **two kinds of updates** and they need opposite handling.
> A **SET** ("warehouse counted 42") is safe to apply twice, but order matters: the newest wins.
> A **DELTA** ("−1, sold") doesn't care about order, but must apply **exactly once**. Say this early.

---

## 1. Requirements

**Functional**
1. Producers (warehouses, orders, returns) **publish updates** for a `(sku, location)`: `SET qty` or `DELTA ±n`.
2. The system **keeps the current quantity** per `(sku, location)`.
3. Clients (product page, checkout) **read current inventory**.
4. Downstream systems (search, "back in stock" alerts) **subscribe to changes**.

**Out of scope:** reservations at checkout, forecasting, catalog data.

**Non-functional, in priority order**
1. **Correct under duplicates and reordering.** No double-applied delta, no stale SET winning.
2. **Throughput:** 50k updates/s, **200k/s peak** (Prime Day), with very hot SKUs.
3. **Fresh:** an update is readable within **2 s**.
4. **Durable:** once we ack an update, it's never lost.

---

## 2. Core Entities

- **Update**: `event_id` (unique, from the producer), `source_id`, `source_seq` (goes up per source),
  `sku`, `location`, `type: SET | DELTA`, `qty`.
- **InventoryRecord**: `(sku, location)` → `qty`, `version`, last SET seq per source.
- **AppliedEvent**: `event_id` of each applied delta, kept 7 days (dedup marker).

---

## 3. API

```
POST /v1/inventory/updates   → 202 { accepted, rejected[] }
     body: { updates: [{ event_id, source_id, source_seq, sku, location, type, qty }] }

GET  /v1/inventory/{sku}?location=&consistent=false   → { locations: [{ location, qty, version }] }

Subscribe: DynamoDB Streams on the inventory table
```

**202** = "safely in the stream," not "applied." `event_id` is the idempotency key for retries.

---

## 4. High-Level Design

```
 Producers ──batched POST──► Ingest API ──► Kinesis (partition key = sku#location)
                                                │                 └──► Firehose → S3 (archive)
                                         ┌──────▼──────┐  bad events  ┌─────────┐
                                         │  Appliers   │─────────────►│ SQS DLQ │
                                         │ (one worker │              └─────────┘
                                         │  per shard) │
                                         └──────┬──────┘ conditional writes
                                         ┌──────▼──────┐      ┌──────────────┐
                                         │  DynamoDB   │◄─────│ Read API     │◄── product page
                                         │  Inventory  │      │ + cache (DAX)│
                                         └──────┬──────┘      └──────────────┘
                                                └── DynamoDB Streams ──► search, alerts
```

- **FR1 publish:** the ingest API validates, writes to **Kinesis partitioned by `sku#location`**, then
  returns 202. Kinesis stores across 3 AZs before it acks (NFR 4).
- **FR2 keep the count:** applier workers read Kinesis. Every event for one key lands on **one shard
  and one worker, in order**, so two workers never race on the same key. Producer duplicates and
  reordering still need handling (5.1, 5.2).
- **FR3 read:** reads go through a DAX cache. Checkout asks for a strongly consistent read.
- **FR4 subscribe:** DynamoDB Streams emits each *applied* change, so subscribers never see duplicates.

---

## 5. Deep Dives

### 5.1 Duplicates → NFR 1

Duplicates come from producer retries, Kinesis redelivery, and a worker crashing after writing but
before checkpointing. So: **at-least-once delivery + idempotent apply**.

- **SET:** applying it twice gives the same result, and the seq check in 5.2 drops the repeat anyway.
- **DELTA:** one DynamoDB transaction does both: (1) insert `AppliedEvent{event_id}` only if it doesn't
  exist, (2) add the delta to `qty`. If the event was already applied, step 1 fails and the whole
  thing is skipped. A 7-day TTL keeps the dedup table small.

### 5.2 Out-of-order events → NFR 1

| Case | Rule |
|---|---|
| SET vs. SET | Newest wins by **source seq, not clock**: apply only if `source_seq > last_set_seq` |
| DELTA vs. DELTA | Order doesn't matter: `+5, −1` = `−1, +5`. Count may dip below 0 briefly; show 0 |
| SET vs. DELTA | Hard case: was this late sale already counted in the SET? |

- **Why not timestamps?** Clocks on different producers drift, and a 2 s drift lets an old count win.
- **SET vs. DELTA fix:** the SET says "I include all sales up to order #X." A late delta at or below X
  is already counted, so drop it. If the source can't give X, accept small drift and fix it with
  **reconciliation** (5.3).

### 5.3 Hot keys and failures → NFR 2, 3, 4

- **Hot SKU:** a deal SKU at 5,000 updates/s exceeds one DynamoDB partition (~1,000 writes/s). The
  worker **batches each key for ~100 ms**: sum the deltas, keep the newest SET, write once. 5,000
  writes/s become ~10. The 100 ms fits the 2 s budget.
- **Checkpoint after the write,** never before. A crash means a replay, which dedup makes safe.
- **Throttling:** retry with backoff; Kinesis keeps data 24 h+, so we lag but lose nothing.
  **Bad events:** a few retries, then the **DLQ** with an alarm, and the worker moves on.
- **Reconciliation:** a daily full count from the warehouses is compared to ours and fixed with SETs.
  Track the drift as a metric. Any stream eventually drifts, so plan for repair.

---

## 6. Likely Follow-ups

**"How does checkout avoid overselling with cached reads?"** It doesn't use this path. Checkout does
a conditional decrement (`qty >= n`) on the main record. This system is for display and propagation.

**"Multi-region?"** Each `(sku, location)` has a **home region** where all its writes apply, and other
regions get read copies. Last-write-wins across regions would be wrong for deltas.

**"What do you monitor?"** Kinesis iterator age (freshness, alarm at 2 s), duplicate and stale-SET drop
rates per source, DLQ depth, and reconciliation drift.
