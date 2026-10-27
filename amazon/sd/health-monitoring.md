# System Design: Heartbeat / Health-Monitoring Service

**Prompt:** "Design a service that monitors the health of a large fleet using heartbeats and tells
other systems when something goes down."  
**Source:** 📣 US L5, Apr 2025 ([6623435](https://leetcode.com/discuss/post/6623435/))

> **What they're testing:** can you tell **"it died"** apart from **"I can't see it"**, and stop the
> monitor's own problems from marking **the whole fleet dead**. The consumer drains traffic off
> anything unhealthy, so a false "dead" is an outage we caused. Say that early.

---

## 1. Requirements

**Functional**
1. Owners **register entities** (hosts, routers, service instances) with a policy: heartbeat interval
   and how many misses mean "down."
2. Entities **send heartbeats** (push). The service also **probes** them (pull) to confirm.
3. The service tracks status (`HEALTHY → SUSPECT → UNHEALTHY`) and **publishes state-change events**
   to subscribers (alerting, the traffic-drain controller).
4. Callers can **query current status** for one entity or a whole AZ.

**Out of scope:** metrics and logs, dashboards, the fix itself (subscribers decide).

**Non-functional, in priority order**
1. **No mass false alarms.** A problem on the monitor's side must never mark lots of the fleet unhealthy.
2. **Detect a real failure within 15 s.**
3. **Scale:** 1M entities, heartbeat every 5 s, so **200k heartbeats/s**.
4. **Events are ordered per entity**, and an old event never overwrites a newer one.

---

## 2. Core Entities

- **Entity**: id, type, owner, AZ, policy.
- **Heartbeat**: entity id, **boot id** (changes on restart), **seq** (goes up by 1 each beat).
- **HealthState**: entity id, status, last seen, **version** (goes up on every status change).
- **StateChangeEvent**: entity id, from, to, version, reason.

---

## 3. API

```
POST /v1/entities                      → { entity_id }     # body: { type, owner, az, policy }
POST /v1/heartbeats                    → 204               # batched: [{ entity_id, boot_id, seq }]
GET  /v1/entities/{id}/health          → { status, last_seen, version }
GET  /v1/health?az=&status=UNHEALTHY   → { entities[], next_cursor }

Subscribe: Kinesis stream "health-changes", partition key = entity_id
```

---

## 4. High-Level Design

```
 Agents ──heartbeats──► Load balancer ──► Ingest (stateless)
                                              │ route by entity_id
 Probers (3 AZs) ──probe results──► ┌─────────▼──────────┐
                                    │ Evaluator shards   │ in-memory "last seen"
                                    │ (each owns a slice)│ + deadline per entity
                                    └─────────┬──────────┘
                              status changes  │ only
                                    ┌─────────▼──────────┐
              Query API ◄───────────│ DynamoDB           │
                                    │ HealthState        │
                                    └─────────┬──────────┘
                                              │ DynamoDB Streams
                                    ┌─────────▼──────────┐
                                    │ Kinesis            │──► Alerting, drain controller
                                    └────────────────────┘
```

- **Key decision:** 200k heartbeats/s just to say "still alive" is too much to write to a database.
  So **liveness lives in memory**, and we **write only status changes** (a few hundred per second).
- **FR1 register:** entities and policies live in a DynamoDB table. Each evaluator loads its slice.
- **FR2 heartbeats:** agents batch heartbeats per host and send to any stateless ingest node, which
  forwards to the evaluator that owns that entity (partition by entity id). Probers in 3 AZs send
  their results to the same evaluator.
- **FR3 status + events:** each heartbeat resets the entity's deadline. When one passes, the evaluator
  checks probes and maybe changes status, with a versioned write to DynamoDB. **DynamoDB Streams**
  feeds Kinesis, so table and event can't disagree. **FR4** queries read DynamoDB directly.

---

## 5. Deep Dives

### 5.1 No mass false alarms → NFR 1

- **Two signals.** A missed heartbeat only makes it `SUSPECT`. `UNHEALTHY` also needs **failed probes
  from at least 2 of 3 AZs**. That separates "it's dead" from "the network to us is broken."
- **Blast-radius breaker.** If more than ~5% of an AZ goes unhealthy within a minute, **stop
  auto-marking** in that scope and page a human. A human confirming a real rack failure in 2 minutes
  beats wrongly draining a whole AZ. (ELB does the same: if every target looks bad, it fails open.)
- **Check ourselves first.** If heartbeats into one shard suddenly drop by half, the problem is
  probably us. That shard stops making changes.

### 5.2 Fast detection without flapping → NFR 2

- Detection time ≈ misses × interval + probe time. With a 3 s interval, 3 misses, and ~2 s of probes,
  that's **~11 s**, under 15 s.
- **Hysteresis:** 3 misses to go down, **5 good beats in a row** to come back. Each flip moves
  traffic, so coming back is deliberately slower.

### 5.3 Duplicates, order, restarts, shard failure → NFR 4

- **Duplicates and late beats:** drop any heartbeat with a `seq` no higher than the last one. A late
  beat from before a crash can't bring a dead entity back.
- **Restarts:** a new **boot id** means it rebooted, even without a missed beat. Emit `RESTARTED`.
- **Clocks:** use the evaluator's receive time, never the sender's clock.
- **Event order:** each change bumps `version` with a conditional write. Kinesis keeps one entity's
  events in order. Subscribers drop any event older than the last version they applied.
- **Shard ownership:** each evaluator holds a **lease** in DynamoDB for its shards. If it dies, a peer
  takes over when the lease expires. The new owner has no deadlines in memory, so **it can't mark
  anything unhealthy for one full detection window** while fresh beats come in.

---

## 6. Likely Follow-ups

**"Scale to 100M entities?"** Add a per-rack aggregator that sends one summary ("39 of 40 alive,
missing X"). The central tier then scales with racks, not entities.

**"Who watches the watcher?"** Canary entities in every AZ that we kill on a schedule. The time until
we detect them is our detection-latency metric. If one is never detected, page.

**"How should the drain controller use the events?"** As input, not orders. Drain slowly, cap it
(say, at most 10% of an AZ automatically), and if the event stream goes quiet, keep the last known
state. Silence means "no news," not "everything is dead."
