# System Design: Primary Database with Read Replicas and Automatic Failover

**Prompt:** "You have a primary DB and read replicas. Design failure detection, failover, consistency
during failover, and how clients get re-routed."  
**Source:** 📣 Seattle, May 2026 ([Reddit](https://www.reddit.com/r/OfferEngineering/comments/1unrane/))

> **What they're testing:** can you avoid **two primaries at once (split brain)** and avoid
> **losing writes the client was told succeeded**. Say both early.

---

## 1. Requirements

**Functional**
1. Apps use one **writer endpoint** and one **reader endpoint**. They never hard-code a host.
2. The system **detects** that the primary is down.
3. It **promotes a replica** and **re-routes clients** automatically.
4. Operators can do a **planned switchover** (for patching).

**Out of scope:** multi-master, sharding, backups, cross-region DR (follow-up).

**Non-functional, in priority order**
1. **Never two primaries.** Correctness beats availability here.
2. **No lost committed writes.**
3. **Recover in under 30 s.**
4. **No false failovers** from a short network blip or GC pause.

---

## 2. Core Entities

- **Node**: id, AZ, role (`PRIMARY | REPLICA`), replication position (how far it has caught up).
- **Epoch**: a number that goes up by 1 on every failover. Tells everyone who the *current* primary is.
- **Topology**: `{epoch, primary, replicas[]}`, stored in a consistent store (etcd, ZooKeeper, or DynamoDB).

---

## 3. API

```
writer.db.internal:5432          # always points at the current primary
reader.db.internal:5432          # load-balanced over healthy replicas

GET  /clusters/{id}/topology     → { epoch, primary, replicas[{node, lag_ms}] }
POST /clusters/{id}/switchover   → { failover_id }      # planned, operator-triggered
```

---

## 4. High-Level Design

```
   App servers
       │ writer / reader endpoint
  ┌────▼────┐   watches   ┌─────────────────┐
  │  Proxy  │◄────────────│ Topology store  │◄──── Failover manager
  └─┬────┬──┘             │ (etcd / DynamoDB)│       (checks health,
    │    │                └─────────────────┘        promotes replica)
 writes reads
 ┌──▼─────┐   replication   ┌──────────┐ ┌──────────┐
 │Primary │────────────────►│Replica A │ │Replica B │
 │ AZ-1   │                 │  AZ-2    │ │  AZ-3    │
 └────────┘                 └──────────┘ └──────────┘
```

- **FR1 endpoints:** apps talk to a **proxy** (RDS Proxy is the managed version). The proxy reads the
  topology and sends writes to the primary and reads to replicas.
- **FR2 detection:** a **failover manager** health-checks the primary every second with a small
  *write* (not just a TCP connect). It needs several misses in a row before it acts.
- **FR3 failover:** the manager picks the **most up-to-date replica**, bumps the epoch, writes the new
  topology, and promotes that replica. The proxy sees the change and sends writes to the new primary.
  The other replicas re-point to it. The old primary comes back later as a replica.
- **FR4 switchover:** same steps, but first stop writes on the old primary and wait for the target to
  catch up. No data loss, a few seconds of write pause.

---

## 5. Deep Dives

### 5.1 Never two primaries → NFR 1

The danger: the manager can't reach the primary, but some apps still can. If we promote B, both accept
writes and the data diverges.

- **Lease:** the primary may accept writes only while it holds a lease (say 10 s) in the topology
  store, renewed every 2 s. If it can't renew, it **stops taking writes on its own**. The manager
  promotes B only **after** the lease has expired, so the two never overlap.
- **Epoch check:** the proxy only routes to the primary named in the latest epoch. An old primary that
  wakes up with an old epoch gets ignored.
- The topology store is a 3-node cluster, so only the majority side of a network split can change it.

### 5.2 No lost committed writes → NFR 2

| Replication | Commit speed | Data loss on failover |
|---|---|---|
| Async | Fastest | Recent writes can be lost |
| **Semi-sync: wait for 1 replica in another AZ** ✔ | +1–2 ms | None, if we promote that replica |
| Sync to all replicas | Slowest | None, but one slow replica blocks every write |

Pick semi-sync, and promote the replica that has received the most data.

### 5.3 Fast failover without false alarms → NFR 3, 4

- Rough timeline: lease expires (~10 s) + promote (~5 s) + proxy picks up change (<1 s) ≈ **15–20 s**.
- Avoid false alarms: require several missed checks, check from more than one AZ, and allow at most
  one automatic failover per 10 minutes (after that, page a human).
- **In-flight writes:** if the primary dies mid-commit, the client doesn't know if it committed.
  Clients retry with backoff, and use an **idempotency key** for writes that must not run twice.
- **Why not DNS?** DNS changes are slow because clients cache them. Keep DNS only as a fallback.

---

## 6. Likely Follow-ups

**"What if replicas are lagging?"** Reads may be stale. For read-your-own-writes, send that user's
reads to the primary for a few seconds after they write. Take badly lagging replicas out of the pool.

**"What if the failover manager dies?"** Run it as 3 instances with one leader. If all are down, no
failover happens, but the current primary keeps working.

**"Cross-region?"** Async replication to another region, so a few seconds of data could be lost.
Promotion there is a **human decision**, because a cut-off region looks the same as a dead one.

**"How would you test it?"** Kill the primary on purpose, measure recovery time, and check that
every acknowledged write is still there.
