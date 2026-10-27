# System Design: Distributed Rate Limiter

**Prompt:** "Design a rate limiter for an API used by many clients, enforced across a fleet of
servers. Token bucket or sliding window? Where does the state live? What about multiple regions?"  
**Source:** 📣 5+ reports, 2026 ([8512004](https://leetcode.com/discuss/post/8512004/), [7710904](https://leetcode.com/discuss/post/7710904/), [8426283](https://leetcode.com/discuss/post/8426283/))

> **What they're testing:** the textbook answer is common, so stand out on **making check-and-decrement
> atomic**, **what happens when Redis is down** (allow or deny?), **hot keys**, and **multi-region
> accuracy vs. latency**.

---

## 1. Requirements

**Functional**
1. The API gateway **asks "is this request allowed?"** for a key (API key, account, IP).
2. Operators **change rules** (rate, burst, endpoint, tier) **without a deploy**.
3. Rejected callers get **429** with `Retry-After`.
4. Limits apply **across the whole fleet**, and global quotas across regions.

**Out of scope:** billing-grade metering, DDoS protection (Shield/WAF), a quota UI.

**Non-functional, in priority order**
1. **Fast:** under **2 ms** added per request. It's on every request.
2. **Available:** a limiter failure **must not take the API down**.
3. **Scale:** **1M requests/s**, 10M active keys.
4. **Accurate:** within ~5% in a region. Global quotas can be a few seconds behind.

---

## 2. Core Entities

- **Rule**: match (key type, endpoint, tier), rate, burst, `fail_mode: OPEN | CLOSED`, scope
  (`REGIONAL | GLOBAL`), version.
- **Bucket**: one per rule per key: `{tokens, last_refill_time}`.
- **Decision**: allowed, remaining, retry_after.

---

## 3. API

```
CheckLimit(key, rule, cost = 1)  → { allowed, remaining, retry_after_ms }   # internal, in-process

PUT /v1/rules/{rule_id}          body: { match, rate, burst, fail_mode, scope, shadow }

HTTP 429   Retry-After: 2   X-RateLimit-Remaining: 0
```

`cost` charges more than 1 (batch APIs, LLM tokens). `shadow: true` logs would-be denials only.

---

## 4. High-Level Design

```
   Clients ──► Load balancer
                   │
   ┌───────────────▼──────────────┐   poll every 10 s  ┌──────────────┐
   │ API gateway nodes            │◄───────────────────│ Rule service │
   │  limiter library + cached    │                    │ (DynamoDB)   │
   │  rules + local backup bucket │                    └──────────────┘
   └───────────────┬──────────────┘
                   │ 1 call per request (~0.5 ms)
   ┌───────────────▼──────────────┐   usage every 1 s   ┌──────────────┐
   │ ElastiCache Redis (sharded   │◄───────────────────►│ Other regions│
   │ by key)                      │                     └──────────────┘
   └──────────────────────────────┘
```

- **FR1 check:** the limiter is a library inside the gateway (no extra network hop). It matches the
  rule, builds the key `rl:{rule}:{api_key}`, and makes **one atomic call to Redis** that refills and
  takes a token. One round trip is what keeps it under 2 ms.
- **FR2 rules:** stored in DynamoDB with a version. Gateways poll and swap in new rules. If the rule
  service is down, they **keep the last good rules**.
- **FR3 429:** `Retry-After` comes from the bucket: time until the next token.
- **FR4 fleet-wide:** state is in Redis, not on each gateway, so all gateways share one bucket per key.
  Sizing: 1M ops/s ÷ ~100k ops/s per Redis shard ≈ 10 shards, so ~16–20 with headroom.

---

## 5. Deep Dives

### 5.1 Algorithm and atomicity → NFR 4

| Algorithm | Problem | Verdict |
|---|---|---|
| Fixed window | 2× burst at the window edge | No |
| Sliding window log | One timestamp per request: too much memory | No |
| Sliding window counter | Close approximation, 2 numbers | ✔ For "N per hour" quotas |
| **Token bucket** | Exact rate + allowed burst, 2 numbers | ✔ **Default** (API Gateway uses it) |

- **Token bucket:** each check adds tokens for the time passed (capped at burst), then takes one if
  available. No background timer needed.
- **The race:** two gateways both read "1 token left," both allow. Fix: run read-refill-decrement as
  **one atomic Redis operation** (a small server-side script), so calls on a key can't interleave.
  Use **Redis's clock**, not each gateway's, so clock drift can't create tokens.

### 5.2 Redis down or slow → NFR 2

- **Hard 5 ms timeout + circuit breaker** (stop calling Redis for a while). Then `fail_mode` decides:
  - **OPEN** (default, normal API quotas): allow, but apply a **local bucket of limit ÷ number of
    gateways**. Rough, but some protection.
  - **CLOSED** (login attempts, OTP sends): deny. Letting an attack through is worse.
- **Redis failover can lose recent counts.** Buckets reset to full, a brief over-allow. Fine: this is
  soft state, not worth synchronous replication.
- **Don't retry a limiter call.** The first may have taken a token. Clients retrying on 429 should use
  **backoff with jitter** (random delay) so they don't all retry at once.

### 5.3 Hot keys and multi-region → NFR 1, 3, 4

- **Hot key:** one tenant at 100k req/s overloads one Redis shard. For keys above a threshold, each
  gateway **grabs a batch of tokens** (say 5% of the bucket) and spends them locally. Far fewer Redis
  calls; over-allow is at most batch × gateways.
- **Multi-region:** one global Redis adds 60–150 ms per request, so no.
  - **Per-second limits:** enforce per region independently.
  - **Daily or monthly quotas:** enforce locally, and every 1 s each region shares its usage count
    (e.g. through DynamoDB Global Tables). Each region allows `limit − other regions' usage`. Over-allow
    is at most about 1 s of traffic.

---

## 6. Likely Follow-ups

**"Library, sidecar, or separate service?"** Library in the gateway: a separate service adds a hop
just to reach Redis. Use a sidecar only if many services in many languages need it.

**"Rate limiting vs. load shedding?"** Rate limiting is fairness per client against a contract. Load
shedding protects the backend from overload, whoever sends. You need both.

**"How do you roll out a new rule safely?"** Shadow mode first, check who would be denied, then
enforce. Alarm if denials jump right after a rule change; it's usually a config mistake.

**"How does this apply to a routing control plane?"** Rate-limit *changes pushed to the network*: N
route updates per second per device, M devices per minute per region. Here it fails **closed**:
"limiter down, push everything" is how a bad change reaches the whole network.
