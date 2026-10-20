# Question Bank — AWS SDE II Onsite (Control Plane, Scalable Intent Driven Routing)

**Legend:** 📣 = candidates reported it in a 2025–2026 Amazon loop (with a link). ★ = do first.
🌐 = relevant to routing/networking. ✅ = already solved in the Meta [`README.md`](../README.md).

## What's confirmed

**The team.** The posting is [job 10535019](https://www.amazon.jobs/en/jobs/10535019/software-development-engineer-control-plane-aws-scalable-intent-driven-routing-sidr)
in Santa Clara, posted 2026-09-09, with a base range of $165.2K–$223.6K. SIDR is part of AWS Network Infrastructure. It builds
the control plane that steers traffic across Amazon's network fabrics, including data center
fabrics, the links between data centers, and internet peering, using both stored and real-time network
state, with SDN alongside traditional routing. The postings ask for Java, C++ or C#, OOD and SOA, and say
**"networking background not required."**

**Format** (Amazon's [SDE II prep page](https://www.amazon.jobs/content/en/how-we-hire/sde-ii-interview-prep) plus candidate reports):
- Every round opens with **2–3 LP questions (about 15–25 min)**. The rest is technical.
- Coding is in **LiveCode**: no compiler, no autocomplete, and "syntactically correct code, no pseudo code".
  System design uses the **Bluescape** whiteboard.
- The US AWS round names are **DS&A**, **Problem Solving**, **Logical & Maintainable**, plus System Design.
  One round is the **Bar Raiser**, which is usually unlabeled and not always last.
- **No AI tools** were reported in any loop. AI shows up as *behavioral questions* instead (see the LP section).
- Being **downleveled to L4** after a weak system design or Bar Raiser round is a common reported outcome.

**Limits on the evidence.** I found **no reports from SIDR or any other AWS networking team** for 2025–26.
About 85% of the recent reports are from India, and Glassdoor and 1point3acres blocked access. Links marked
"post N" are `leetcode.com/discuss/post/N/`. 🌐 items without 📣 are inferred from the team's charter.

---

## Round 1 — DS&A

They want the best data structure, a correct complexity analysis, and full working code.

### Reported more than once (2025–26)

| Problem | LC | Reports | Sources |
|---|---|---|---|
| ★ 📣 LFU Cache (or variant) | 460 | 3 | posts [8575075](https://leetcode.com/discuss/post/8575075/), [8524405](https://leetcode.com/discuss/post/8524405/), [6863327](https://leetcode.com/discuss/post/6863327/) |
| ★ 📣 Find Median from Data Stream (**AWS Seattle, Aug 2026**) | 295 | 2 | [8488182](https://leetcode.com/discuss/post/8488182/), [8315111](https://leetcode.com/discuss/post/8315111/) |
| ★ 📣 Course Schedule II / topological sort ✅ 🌐 | 210 | 3 | [8286346](https://leetcode.com/discuss/post/8286346/), [6674923](https://leetcode.com/discuss/post/6674923/), [8423184](https://leetcode.com/discuss/post/8423184/) |
| ★ 📣 Binary search on the answer (Ship Packages, Koko) | 1011, 875 | 4+ | [8512004](https://leetcode.com/discuss/post/8512004/), [6961911](https://leetcode.com/discuss/post/6961911/), [8315111](https://leetcode.com/discuss/post/8315111/) |
| ★ 📣 Multi-source BFS (Rotting Oranges, Safest Path in a Grid) | 994, 2812 | 3 | [6891316](https://leetcode.com/discuss/post/6891316/), [7554515](https://leetcode.com/discuss/post/7554515/), [8499681](https://leetcode.com/discuss/post/8499681/) |
| ★ 📣 LRU Cache | 146 | 2 | [8536211](https://leetcode.com/discuss/post/8536211/), [6585102](https://leetcode.com/discuss/post/6585102/) |
| 📣 Merge Intervals | 56 | 2 | [8564500](https://leetcode.com/discuss/post/8564500/), [8286346](https://leetcode.com/discuss/post/8286346/) |
| 📣 Max concurrent load sweep (Car Pooling, max bandwidth) 🌐 | 1094 | 2 | [7562840](https://leetcode.com/discuss/post/7562840/), [7670163](https://leetcode.com/discuss/post/7670163/) |
| 📣 Reorganize String | 767 | 2 | [8513742](https://leetcode.com/discuss/post/8513742/), [8286346](https://leetcode.com/discuss/post/8286346/) |
| 📣 Search in Rotated Sorted Array | 33 | 2 | [8575909](https://leetcode.com/discuss/post/8575909/), [7622801](https://leetcode.com/discuss/post/7622801/) |
| 📣 Max Profit in Job Scheduling | 1235 | 2 | [7562840](https://leetcode.com/discuss/post/7562840/), [6962158](https://leetcode.com/discuss/post/6962158/) |

### Reported once in 2026

- **AWS Seattle (Aug):** Shortest Unsorted Continuous Subarray (581). **AWS Dublin (Aug):** Minimum Window Substring (76).
- Container With Most Water → Trapping Rain Water (42) → **Cheapest Flights Within K Stops (787) 🌐**, all in one round.
- Largest Rectangle in Histogram (84), Dungeon Game (174), Longest Consecutive Sequence (128),
  Top K Frequent (347, done with in-place heapify), Copy List with Random Pointer (138), Find K Pairs with Smallest Sums (373),
  Next Greater Element, Longest Happy String (1405), Reverse Nodes in k-Group (25).

### Team-relevant, not reported 🌐

Network Delay Time (743, Dijkstra), Critical Connections (1192), Redundant Connection (684, Union-Find).

---

## Round 2 — Problem Solving

Story-wrapped or custom prompts. They grade how you reason: clarify the problem, start with brute force,
optimize, and test by hand. Expect extensions halfway through.

| Prompt | Underlying pattern | Source |
|---|---|---|
| ★ 📣 🌐 **Tasks with types and dependencies; same-type tasks need a cooldown of k. Find the minimum total time.** (AWS phone screen, May 2026) | Topological sort + Task Scheduler (621) | [8191929](https://leetcode.com/discuss/post/8191929/) |
| ★ 📣 🌐 **Service that checks the heartbeat of other services** (L5 loop, Apr 2025) | Heap/hash map with timeouts; structure and trade-offs | [6623435](https://leetcode.com/discuss/post/6623435/) |
| ★ 📣 Parking garage: cars need 1–3 consecutive spaces; `park(size)` takes the leftmost fit, plus `leave(start, size)` (L5, Oct 2026) | Like Design Memory Allocator (2502) | [8550034](https://leetcode.com/discuss/post/8550034/) |
| ★ 📣 `getToken()` returns the lowest free integer; `returnToken(t)` frees it (L5, Feb 2025) | Min-heap + counter | [6674923](https://leetcode.com/discuss/post/6674923/) |
| 📣 🌐 Currency conversion (AWS Canada, Jul 2026) | Evaluate Division (399), weighted graph | [8388897](https://leetcode.com/discuss/post/8388897/) |
| 📣 Reduce a firmware buffer to 0 by removing from either end (Alexa, Oct 2026) | LC 1658, prefix sum / sliding window | [8567817](https://leetcode.com/discuss/post/8567817/) |
| 📣 Next "good time" after HH:MM, then rewrite as production-quality code (Bar Raiser, Sep 2026) | Simulation + clean code | [8522985](https://leetcode.com/discuss/post/8522985/) |
| 📣 Given brute-force code, explain what it does and optimize it (Bar Raiser, May 2025) | Code reading | [6961911](https://leetcode.com/discuss/post/6961911/) |
| 📣 Encode/decode a blob-like object, then extend it (USA, Jun 2025) | Serialization (like 297/271) | [6924985](https://leetcode.com/discuss/post/6924985/) |
| 📣 Bus Routes with a Dijkstra cost follow-up (Mar 2025) 🌐 | BFS → Dijkstra | LC 815 |

**Routing-flavored follow-ups to rehearse:** "A link fails; update without recomputing everything." "Return the
path, not just the cost." "Break ties deterministically." "The graph has 1M nodes."

---

## Round 3 — Logical & Maintainable (OOD in real code)

Candidates describe it as: *"LLD, but you code it. No pseudocode. Skeleton classes first, then implement the
important methods."* ([8252377](https://leetcode.com/discuss/post/8252377/)). It's graded on naming,
SOLID, extensibility, edge cases and clarifying questions. Blind says "50% SOLID, 50% OOD… 300% naming"
([thread](https://www.teamblind.com/post/amazon-logical-and-maintainable-round-7h0f48md)). You don't need to finish.

| Problem | Reports | Design idea | Sources |
|---|---|---|---|
| ★ 📣 **Amazon Locker** (assign by size, pickup code, expiry; also a reverse "drop-off store" variant) | 5 | Size matching, state machine | [7754949](https://leetcode.com/discuss/post/7754949/), [7228788](https://leetcode.com/discuss/post/7228788/), [6623435](https://leetcode.com/discuss/post/6623435/), [6585102](https://leetcode.com/discuss/post/6585102/), [8499681](https://leetcode.com/discuss/post/8499681/) |
| ★ 📣 **File search with composable filters (Unix `find`, AND/OR)** (**AWS Dublin, Aug 2026**) | 2 + variant | Specification + Composite | [8464434](https://leetcode.com/discuss/post/8464434/), [8522985](https://leetcode.com/discuss/post/8522985/), [8353900](https://leetcode.com/discuss/post/8353900/) |
| ★ 📣 Notification system (multi-channel; urgent → all channels, else user preference) | 2 | Strategy + routing rules | [8536211](https://leetcode.com/discuss/post/8536211/), [8423184](https://leetcode.com/discuss/post/8423184/) |
| ★ 📣 Pub/Sub (subscribe by event type; 10k msg/s, concurrency) | 2 | Observer, thread safety | [8513742](https://leetcode.com/discuss/post/8513742/), [7600153](https://leetcode.com/discuss/post/7600153/) |
| ★ 📣 Logger / in-memory logger with a fixed flash buffer | 2 | Ring buffer, levels, sinks | [8523912](https://leetcode.com/discuss/post/8523912/), [8567817](https://leetcode.com/discuss/post/8567817/) |
| ★ 📣 🌐 **Idempotent order processing that handles duplicates from network retries** | 1 | Idempotency keys, state machine | [7622801](https://leetcode.com/discuss/post/7622801/) |
| 📣 E-commerce order validation flow before it goes downstream (**AWS Seattle, Aug 2026**, Bar Raiser) | 1 | Chain of Responsibility | [8488182](https://leetcode.com/discuss/post/8488182/) |
| 📣 🌐 Network Request Cache (interviewer wanted the LRU underneath) | 1 | LRU + TTL | [6961911](https://leetcode.com/discuss/post/6961911/) |
| 📣 🌐 DNS resolver with health check (compiled list) | — | Cache + health checker + failover | [8519189](https://leetcode.com/discuss/post/8519189/) |
| 📣 Rate limiter, sliding-window log (AWS Dublin phone screen) | 1 | Strategy pattern | [8464434](https://leetcode.com/discuss/post/8464434/) |
| 🌐 Routing table: `add(prefix, nextHop)`, `remove`, `lookup(ip)` with longest-prefix match | — | Binary trie | inferred |
| 🌐 Versioned config store with `rollback` and diff | — | Immutable snapshots | inferred |

Also reported once: vending machine, coffee machine, Splitwise, parking lot, pizza ordering (Decorator), delivery slot booking, bank app with concurrency.

---

## Round 4 — System Design

Often the hiring manager's round. The prompt is deliberately vague ("Design Netflix. That's it."). You lead:
functional requirements → non-functional requirements → entities → API → high-level design → deep dives.
Interviewers push on **failure modes, retries, idempotency, duplicate and out-of-order events, consistency and
observability**. Weak depth here is the top reason candidates get downleveled.

### Reported (US/AWS first)

| Question | Where / when | Source |
|---|---|---|
| ★ 📣 🌐 **Primary DB + read replicas: failure detection, failover, consistency during failover, client re-routing** | Seattle, May 2026 | [Reddit](https://www.reddit.com/r/OfferEngineering/comments/1unrane/) |
| ★ 📣 🌐 **Heartbeat / health-monitoring service** | US L5, Apr 2025 | [6623435](https://leetcode.com/discuss/post/6623435/) |
| ★ 📣 🌐 **High-rate update stream (inventory, tens of thousands/sec) with duplicate and out-of-order events** | Sep 2026 | [Reddit](https://www.reddit.com/r/OfferEngineering/comments/1wm2krn/) |
| ★ 📣 **Distributed rate limiter** (token bucket, sliding window, Redis) | 5+ reports, 2026 | [8512004](https://leetcode.com/discuss/post/8512004/), [7710904](https://leetcode.com/discuss/post/7710904/), [8426283](https://leetcode.com/discuss/post/8426283/) |
| ★ 📣 🌐 **Job scheduler with dependent jobs** (Kahn's algorithm, retries, backoff) | 2026 | [8554896](https://leetcode.com/discuss/post/8554896/), [8487224](https://leetcode.com/discuss/post/8487224/) |
| 📣 Multi-device sync (Kindle-style): stale writes, conflict resolution, idempotent APIs | L5 Bar Raiser, Aug 2026 | [Reddit](https://www.reddit.com/r/OfferEngineering/comments/1vho844/) |
| 📣 Book marketplace: find the best price across sellers | **AWS Seattle, Aug 2026** (HM) | [8488182](https://leetcode.com/discuss/post/8488182/) |
| 📣 Artifact repository (like JFrog): scale, metrics, malicious artifacts | AWS Dublin, Aug 2026 | [8464434](https://leetcode.com/discuss/post/8464434/) |
| 📣 Real-time error-log monitoring at 1M writes/sec, with a backpressure deep dive | 2026 | [7710904](https://leetcode.com/discuss/post/7710904/) |
| 📣 Metrics collection and aggregation | Ads NYC, Apr 2025 | [Reddit](https://www.reddit.com/r/interviewpreparations/comments/1jykqnt/) |
| 📣 🌐 Sync device configuration from an old device to a new one | compiled list | [8519174](https://leetcode.com/discuss/post/8519174/) |
| 📣 Others: Netflix, BookMyShow seat concurrency, news feed, Instagram, voting system (America's Got Talent), notification fan-out | various | see compiled lists |

### Team-specific, inferred from the job posting 🌐

- ★ **Push routing config to 100K routers safely**: staged waves, health gates, automatic rollback, blast radius, offline devices.
- ★ **Intent-based network controller**: desired vs. actual state, reconciliation loop, idempotency, conflicting intents.
- **Traffic engineering**: compute paths from live link state, rebalance when a link fails or congests (shortest path / max-flow).

### Outline: config distribution to 100K routers

- **Functional requirements:** submit a change; roll it out to target devices; see per-device progress; roll back.
- **Non-functional requirements:** *safety* (never reach the whole fleet at once), *availability* (the data plane forwards traffic even if the control plane
  is down), eventual consistency (converge within minutes), *auditability*, scale (100K devices).
- **Entities:** ConfigVersion (immutable), RolloutPlan (waves), DeviceState (desired version, actual version, health).
- **High-level design:** API → versioned config store → rollout orchestrator → regional distributors → device agents, which report actual state back.
- **Deep dives:** waves of 1 device → 1% → one Availability Zone → one region → global, gated on health checks with auto-rollback.
  Devices keep their last known good config (static stability). Devices pull, and versioned, idempotent applies
  handle reconnects. Send deltas instead of full configs, and rate-limit each wave.

---

## Round 5 — Bar Raiser

A senior interviewer from outside the team. It's usually unlabeled and not always last. They ask "why?" repeatedly,
check how your metrics were actually measured, and **count heavy hint-taking against you**
([8554896](https://leetcode.com/discuss/post/8554896/)). The best roundup is
[8531532](https://leetcode.com/discuss/post/8531532/), "Bar Raiser Snapshots, till Sep 2026".

**The usual SDE II mix:** 25–40 min of LPs plus one of the following:
- **Coding (most common).** 📣 Insert/Delete/GetRandom O(1) (380), Find the Safest Path in a Grid (2812),
  Dijkstra 🌐, reconstruct a sequence via topological sort, LCA in an N-ary tree plus weighted shortest path 🌐,
  LFU, Reorganize String, Reverse Nodes in k-Group, Car Pooling, a deliberately vague merge-intervals variant.
- **Design.** 📣 Kindle sync, distributed rate limiter, notification system, vending machine, order validation (AWS Seattle).
- **Resume deep dive (30–40 min).** Architecture choices, trade-offs, what *you* did, how you measured impact.

**Follow-ups to have answers for in every story:** "What did *you* do?" · "How was that metric measured?" ·
"Why not the alternative?" · "What would you do differently?" · "Is it still in place?"

---

## Leadership Principles — what SDE II candidates actually got

LPs aren't tied to particular rounds, so prepare all of these. This is a tally across about 30 reported 2025–26 loops:

| Rank | LP | Reports | Questions reported |
|---|---|---|---|
| 1 | ★ **Have Backbone; Disagree and Commit** | ~13 | A senior made a decision you disagreed with · conflict with a PM or manager · you were right against seniors · influencing someone who preferred another approach |
| 2 | ★ **Dive Deep** | ~12 | Debugging a production issue to root cause · solving a scaling issue by digging into internals · a hard issue and what you'd do better |
| 3 | ★ **Deliver Results** | ~11 | Tight deadline · limited resources · deciding without exploring every option |
| 4 | ★ **Ownership** | ~10 | A problem outside your scope · a process you improved on your own · going above and beyond |
| 5 | ★ **Customer Obsession** | ~10 | Above and beyond for a customer · a feature they didn't know they needed · pushing back on a customer |
| 6 | Learn and Be Curious | ~7 | Learned something recently and applied it · upskilled beyond the day job |
| 7 | Bias for Action | ~7 | Quick decision with incomplete information · acting on a vague one-line requirement · a calculated risk |
| 8 | Invent and Simplify | ~6 | A simple solution to a complex problem · something innovative |
| 9 | Failure / critical feedback | ~4 | A time you failed · critical feedback you received |
| 10 | Highest Standards, Earn Trust, Think Big | ~2–3 each | Standards vs. delivery · long-term vs. short-term trade-off |

### New in 2026: GenAI behavioral questions (about 6 loops)

- How do you use AI in your daily work?
- How do you verify AI-generated code is correct?
- Tell me about a time AI-generated code or output was wrong.
- When do you trust an LLM, and when don't you?
- Tell me about using GenAI to solve a business problem, with a measurable result.

Your Kaamel compliance-AI work (source links on every answer, required human review) answers most of these directly.

### Must-have stories for an infrastructure team

- **An outage or incident:** how you detected it, what you did to stop the impact, the root cause, and the fix that prevented it from happening again. This also covers Dive Deep.
- **A disagreement you won with data**, and **one you lost and committed to anyway.**
- **A failure** you own fully, with a lesson you've since applied.
- **A GenAI story** with numbers.

---

## Prep order

1. ★ items in Rounds 1–2, in a plain editor on a 30-minute timer, talking aloud.
2. ★ Logical & Maintainable problems: Locker, `find`, Pub/Sub, Logger, idempotent processing.
3. Full write-ups for: health monitoring / failover, config distribution to routers, rate limiter, job scheduler.
4. STAR stories for LP ranks 1–8 plus GenAI, so nothing gets reused across 5 rounds.

## Sources

- Compiled 6-month lists (India-heavy, about 300 items): [8519174](https://leetcode.com/discuss/post/8519174/), [8519184](https://leetcode.com/discuss/post/8519184/), [8519189](https://leetcode.com/discuss/post/8519189/)
- The only US AWS SDE II loop found with full questions (Seattle, Aug 2026): [8488182](https://leetcode.com/discuss/post/8488182/)
- Round-type differences: [Blind, AWS SWE II virtual onsite](https://www.teamblind.com/post/aws-swe-ii-virtual-onsite-difference-in-coding-rounds-1yaaqm3k)
- Some Reddit posts (r/OfferEngineering, r/amazonsdeprep) are marketing for prep companies. Treat them as lower confidence.
