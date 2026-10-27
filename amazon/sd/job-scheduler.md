# System Design: Job Scheduler with Dependent Jobs

**Prompt:** "Design a scheduler that runs jobs with dependencies between them: a job runs only after
the jobs it depends on succeed. Handle failures, retries, and backoff."  
**Source:** 📣 2026 ([8554896](https://leetcode.com/discuss/post/8554896/), [8487224](https://leetcode.com/discuss/post/8487224/))

> **What they're testing:** releasing a job **only when all its parents succeed** (a counter per job),
> making sure **one job never runs twice at once**, and being honest: state changes can be exactly
> once, but **execution is at-least-once, so jobs must be idempotent**. Say that sentence.

---

## 1. Requirements

**Functional**
1. Users **submit a run**: a graph of jobs (DAG), each with a command, timeout, and retry policy.
2. A job **starts once all its parents succeed**. Independent jobs run in parallel.
3. Failures are **retried with backoff**. If a job fails for good, its downstream jobs are skipped.
4. Users can **check status**, **cancel**, and **re-run from the failure**.

**Out of scope:** cron triggers (follow-up), resource quotas, the compute platform (ECS/Batch runs the containers).

**Non-functional, in priority order**
1. **One active execution per job**, and a duplicate "done" message never releases a child early.
2. **Durable:** an accepted run is never lost; a scheduler crash loses no progress.
3. **Fast:** a ready job starts within **~2 s**.
4. **Scale:** ~1M jobs/day (~12/s average, ~500/s peak), DAGs up to 10k jobs.

---

## 2. Core Entities

- **Workflow**: id, version, jobs, and edges (parent → child).
- **Run**: run id, workflow version, status, idempotency key.
- **JobRun**: (run id, job id), status (`PENDING | READY | RUNNING | RETRY_WAIT | SUCCEEDED | FAILED
  | SKIPPED`), **`remaining_deps`** (parents not yet done), attempt, lease expiry, **lease token**.

---

## 3. API

```
POST /v1/runs                      → { run_id }   # header: Idempotency-Key
GET  /v1/runs/{run_id}             → { status, jobs: [{ job_id, status, attempt }] }
POST /v1/runs/{run_id}/cancel      |   POST /v1/runs/{run_id}/rerun → { run_id }

# Workers (internal)
POST /v1/leases                    → [{ run_id, job_id, lease_token, spec }]   # worker pulls work
POST /v1/jobs/{run}/{job}/heartbeat  body: { lease_token }
POST /v1/jobs/{run}/{job}/complete   body: { lease_token, outcome }
```

---

## 4. High-Level Design

```
  Users ──► API service ──(one transaction)──► ┌─────────────────────┐
                                               │ PostgreSQL (Aurora) │
  Workers (ECS/Batch) ◄── claim, heartbeat, ──►│ runs, job_runs,     │
                          complete             │ edges, events       │
                                               └──────────▲──────────┘
                     Sweeper (on every node): retry-due → READY,
                     expired lease → failed attempt
```

- **Why a SQL database:** 500 jobs/s × ~4 writes ≈ 2k writes/s, easy for one Postgres writer. And we
  need **transactions** to release children correctly.
- **FR1 submit:** check the graph has **no cycle** (topological sort: repeatedly remove jobs with no
  parents; if some are left, there's a cycle, so reject). Then insert the run and all jobs in **one
  transaction**, with `remaining_deps` = number of parents. Jobs with 0 parents start `READY`.
- **FR2 run when ready:** workers ask for work. The server claims READY rows with
  `SELECT … FOR UPDATE SKIP LOCKED` (each worker gets different rows, no blocking), marks them
  `RUNNING`, sets a 60 s lease, and bumps the lease token. On success, in one transaction: mark the
  job `SUCCEEDED`, subtract 1 from each child's `remaining_deps`, and mark any child at 0 `READY`.
- **FR3 retries:** a failed attempt goes to `RETRY_WAIT` with a backoff time. The sweeper moves it back
  to `READY` when due. On final failure, mark it `FAILED` and all descendants `SKIPPED`.
- **FR4:** status is a read; cancel reaches workers on their next heartbeat; re-run keeps succeeded jobs.

---

## 5. Deep Dives

### 5.1 Releasing children exactly once → NFR 1, 2

The bug: a worker's "complete" call times out and it retries. If both count, a child's counter drops
twice and it **starts before its other parent finishes**. Fix: completion is a conditional update.

```sql
UPDATE job_run SET status = 'SUCCEEDED'
 WHERE run_id = :r AND job_id = :j AND status = 'RUNNING' AND lease_token = :t;
-- 0 rows: duplicate or stale → return OK, change nothing
-- 1 row:  same transaction → decrement children, mark ready ones READY
```

Why not a queue for release? Queues deliver duplicates: the same bug.

### 5.2 One execution at a time, at-least-once → NFR 1

- **Lease:** a worker owns a job for 60 s and heartbeats every 15 s. If it dies, the lease expires and
  the job is retried.
- **Zombie worker:** worker A pauses, its lease expires, worker B takes the job with token 8. A wakes
  up and reports with token 7: **rejected**. A also kills its own job if it can't renew its lease.
- But A may already have written output. So jobs must be **idempotent**: write to
  `s3://…/{run_id}/{job_id}/` (a re-run overwrites, not appends), and use `run_id/job_id` as the
  idempotency key on external calls.

### 5.3 Retries and crashes → NFR 2, 3

- **Only retry retryable errors** (timeout, 5xx, throttling). Bad input fails right away.
- **Exponential backoff with jitter:** wait a random time up to `min(10 min, 10 s × 2^attempt)`, 5
  attempts. Jitter stops 300 failed jobs from all retrying in the same second.
- **Scheduler nodes are stateless;** all state is in Aurora (Multi-AZ). The sweeper runs on every node
  safely because its updates are conditional and use SKIP LOCKED. No leader election needed.
- **After a DB failover,** pause lease expiry for one lease period so live workers aren't marked dead.
- **Monitor** age of the oldest READY job (alarm above 10 s), lease expirations, retry rate.

---

## 6. Likely Follow-ups

**"Cron triggers, and missed slots after an outage?"** The trigger creates a run with idempotency key
`schedule_id + time`, so firing twice makes one run. Per schedule, choose: run all missed slots, only
the latest, or skip.

**"One tenant submits 50,000 jobs."** Per-tenant concurrency cap in the claim query, and fair ordering
across tenants instead of one global FIFO.

**"Why not Step Functions?"** In production I'd consider it (managed, built-in retries). This design
shows I understand the guarantees I'd rely on.

**"Scale 10x?"** Partition by `run_id` across databases; a run never spans two.

**"How does this connect to the routing team?"** A config rollout is a DAG: canary → health check →
1% → health check → one AZ → region. A failed health check skips the later waves and starts a
rollback job. Device applies must be idempotent, because jobs can run more than once.
