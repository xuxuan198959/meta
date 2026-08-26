# Agent Architecture — Deep Dive

Companion to [Q1 of Interview 3](./Interview%203%20-%20Domain%20Expertise%20(GenAI).md#q1--reference-architecture).
That section is the **4-minute spoken answer**. This is the depth behind it, for
when the interviewer says *"go deeper on retrieval"* or *"how would you actually
deploy this?"*

For each layer: **what it does → one service or many → AWS stack → what's tricky
→ how it fails and how you'd know.**

> **Interview calibration.** Don't volunteer this volume of detail. Give the
> 4-minute sketch, then let them pull. The signal being scored is *"can you name
> the components and how they interact"* — depth is the follow-up, not the
> opener. Sections marked 🎤 are worth saying unprompted because they're the ones
> that make you sound like you've operated one of these.

---

## Contents

- [Service decomposition — the honest answer](#service-decomposition--the-honest-answer)
- [Deployment view on AWS](#deployment-view-on-aws)
- [Layer 1 — Channel gateway](#layer-1--channel-gateway)
- [Layer 2 — Session & conversation state](#layer-2--session--conversation-state)
- [Layer 3 — Orchestrator / agent loop](#layer-3--orchestrator--agent-loop)
- [Layer 4 — System prompt & merchant config (control plane)](#layer-4--system-prompt--merchant-config-control-plane)
- [Layer 5 — Retrieval / RAG](#layer-5--retrieval--rag)
- [Layer 6 — Tool calling / integration gateway](#layer-6--tool-calling--integration-gateway)
- [Layer 7 — Model serving](#layer-7--model-serving)
- [Layer 8 — Output guardrails](#layer-8--output-guardrails)
- [Layers 9/10 — Delivery & human handoff](#layers-910--delivery--human-handoff)
- [Layer 11 — Observability & eval plane](#layer-11--observability--eval-plane)
- [Cross-cutting: the latency budget](#cross-cutting-the-latency-budget)
- [Cross-cutting: what a trace must carry](#cross-cutting-what-a-trace-must-carry)
- [Symptom → layer triage table](#symptom--layer-triage-table)
- [The five bugs that actually hurt](#the-five-bugs-that-actually-hurt)

---

## Service decomposition — the honest answer

🎤 **Eleven boxes on the diagram is not eleven services.** If asked "is this one
service or many," the answer that scores is: *start as a modular monolith, split
at seams where one of four things diverges.*

| Split when… | Example |
|---|---|
| **Scaling profile differs** | Webhook ingest is spiky and sub-second; the agent loop is slow and concurrency-bound. Different autoscaling signals entirely. |
| **Blast radius differs** | A merchant's broken API must not be able to take down message ingest. |
| **Deploy cadence differs** | Prompts change daily; the channel gateway changes monthly. |
| **Statefulness differs** | The indexer is batch and restartable; the agent loop holds a live conversation. |

That yields roughly **six deployables plus shared stores**:

| Service | Contains layers | Shape |
|---|---|---|
| **Message gateway** | 1, 9 | Stateless. Two workers: inbound (ack + enqueue) and outbound (send + retry + rate limit). |
| **Agent runtime** | 3, 4-read, 8 | The core. Long requests, IO-bound, high concurrency per instance. |
| **Retrieval service** | 5 (query path) | Low-latency read. Separate from the indexer. |
| **Indexing pipeline** | 5 (write path) | Async/batch. Restartable, backfillable. |
| **Integration gateway** | 6 | Egress to merchant APIs. **The most important isolation boundary in the system.** |
| **Control plane** | 4 (write path) | Merchant config + prompt versions. Low traffic, high blast radius. |

Plus: the **agent desk** (10) is a separate product surface with its own UI and
staffing model, and the **observability/eval plane** (11) is fully async and off
the request path.

🎤 The one seam worth defending unprompted is the **integration gateway**. Every
merchant API is a distributed dependency you don't control, can't version, and
can't fix. Isolating it means one slow tenant burns its own bulkhead instead of
the shared connection pool.

---

## Deployment view on AWS

```text
             Meta platform webhooks (WhatsApp / Messenger / IG)
                              │
                        [WAF] │
                              ▼
                   API Gateway (HTTP API)
                              │  verify X-Hub-Signature-256, ack 200 fast
                              ▼
                    SQS FIFO  (MessageGroupId = conversation_id)
                              │
                              ▼
        ┌──────────── ECS Fargate: agent-runtime ────────────┐
        │                                                     │
        │   DynamoDB (conversation state) ◄── ElastiCache ────┤ per-conv lock,
        │   S3 (transcript archive)            (Redis)        │ idempotency keys
        │                                                     │
        │   AppConfig ──► prompt + merchant config (versioned)│
        │                                                     │
        │   ──► OpenSearch Serverless   (hybrid BM25 + k-NN)  │  retrieval
        │   ──► integration-gateway (Fargate) ──► PrivateLink/NAT ──► merchant APIs
        │   ──► Bedrock  (model + Guardrails)                 │
        └─────────────────────────────────────────────────────┘
                              │
                    SQS (outbound) ──► Fargate sender ──► Meta Send APIs
                              │
                              ▼
     structured JSON logs ──► CloudWatch ──► Firehose ──► S3 (Parquet) ──► Athena
                                     └──► OpenSearch (transcript search)
                                     └──► CloudWatch Alarms / dashboards
```

Sensible defaults, and why:

| Concern | Choice | Why this one |
|---|---|---|
| Webhook ingest | API Gateway HTTP API → Lambda | Ack in milliseconds, scales to zero, no capacity planning for spikes |
| Queue | SQS **FIFO**, group = `conversation_id` | Serializes turns within one conversation, parallel across conversations. Standard SQS + a Redis lock also works and is cheaper at high volume |
| Agent runtime | ECS Fargate, async Python | Requests are seconds-long and IO-bound; you want hundreds of concurrent turns per task. Lambda's 15-min cap is fine but per-request pricing on long LLM waits is not |
| Long / resumable flows | Step Functions (Standard) or Temporal | Only if a turn can pause for human input or a slow external job. Otherwise skip — it's real complexity |
| Conversation state | DynamoDB, PK `conversation_id`, SK `turn_ts`, TTL attr | Single-key access, predictable latency, TTL gives you retention policy for free |
| Hot session + locks | ElastiCache Redis | `SETNX` with TTL for the per-conversation mutex; idempotency key set |
| Retrieval | OpenSearch Serverless | Hybrid BM25 + k-NN in one engine with server-side metadata filtering. pgvector on Aurora is fine below ~10M chunks and simpler to operate |
| Embeddings + LLM | Bedrock | Managed, provisioned throughput for baseline + on-demand burst. SageMaker + vLLM if you need a self-hosted Llama |
| Guardrails | Bedrock Guardrails + Comprehend | Content policy, denied topics, PII redaction, and a **contextual grounding check** out of the box |
| Config rollout | AppConfig | Validators, gradual deployment, and **automatic rollback on a CloudWatch alarm** — exactly what you want for prompt pushes |
| Merchant credentials | Secrets Manager, per-tenant, rotated | Never a shared token across tenants |
| Egress | NAT with fixed EIPs, or PrivateLink | Merchants allowlist your IPs; you need them stable |
| Analytics | Firehose → S3 Parquet → Athena/Glue | Cheap at 10M conversations/week; OpenSearch for interactive transcript search |

---

## Layer 1 — Channel gateway

**What it does.** Terminates webhooks from the WhatsApp Business Platform,
Messenger Platform, and Instagram Messaging API. Verifies the signature,
normalizes wildly different per-channel payloads into one canonical inbound
envelope, acks `200` immediately, enqueues. The outbound half does the reverse:
formats per channel, respects per-channel rate limits, retries, tracks delivery
receipts.

**One service or many.** One stateless service with per-channel adapter modules —
channels share 90% of the logic. But **inbound and outbound are separate
workers**: inbound must ack in milliseconds and never block; outbound is a retry
queue with rate limiting and ordering constraints. Different failure modes,
different scaling.

**AWS.** API Gateway HTTP API → Lambda for inbound. WAF in front. SQS FIFO out.
Fargate workers for outbound with a Redis token bucket per (merchant, channel).
Secrets Manager for app secrets and verify tokens.

**Tricky parts.**

- **Verify the signature against the raw body.** Parse-then-verify is a real
  vulnerability; JSON round-tripping changes bytes.
- **The ack budget is single-digit seconds.** Meta retries anything that isn't a
  fast `200`. You cannot do LLM work inline — ack, enqueue, return. This forces
  the async architecture; it isn't a style choice.
- **Retries mean duplicate inbound messages.** Idempotency on the platform
  `message_id` is mandatory, not defensive. 🎤 *This is where the duplicate-reply
  failure mode usually starts.*
- **Ordering.** Two messages from one customer arriving in parallel workers
  produce interleaved replies. FIFO group by conversation, or a per-conversation
  lock.
- **Per-channel semantics genuinely differ.** WhatsApp has a 24-hour customer
  service window — outside it you can only send pre-approved templates. IG has
  different attachment types and different reply-to semantics. Normalizing this
  away entirely is a trap: some of it has to surface to the orchestrator.
- **Late and out-of-order webhooks.** A retry can arrive after you've already
  replied to a later message.

**Failure modes → detection.**

| Failure | Signal |
|---|---|
| Duplicate replies | Outbound count grouped by inbound `message_id` — alarm on any `> 1` |
| Dropped messages | Inbound accepted vs conversations with a reply, per 5-min window |
| Ack too slow → platform retries | p99 webhook handler duration; platform retry rate |
| Template/window rejection | Send API error-code breakdown by channel |
| Signature failures | Count by merchant — a spike means a rotated secret |

---

## Layer 2 — Session & conversation state

**What it does.** Conversation history, customer identity and its link to the
merchant's CRM, dedupe/idempotency keys, in-flight agent state (pending tool
call, escalation status), and consent/PII flags.

**One service or many.** Usually a **shared library over a datastore**, not its
own service — an extra network hop on the hottest path buys little. The *store*
is the tier that matters. Wrap it in a state service only once three or more
services need write access.

**AWS.** DynamoDB on-demand, `PK = conversation_id`, `SK = turn_ts`, TTL
attribute for retention. Redis for the hot session, the per-conversation mutex,
and the idempotency key set. S3 for the full transcript archive (cheap, and it's
what feeds replay and eval). Aurora Postgres if the agent desk needs relational
queries over conversations.

**Tricky parts.**

- **History growth vs the context window.** A 40-turn conversation doesn't fit
  cheaply. You need an explicit policy — rolling window plus a running summary —
  and you need to store the summary as a first-class field, not regenerate it
  every turn.
- **Concurrency.** Two turns processed at once corrupts state. Redis `SETNX`
  with a TTL, or a DynamoDB conditional write on a version attribute. The TTL
  must exceed your max turn duration or you'll release the lock mid-turn.
- **Session boundaries.** "Same conversation" after 6 hours of silence? A new
  session with a summary of the old one is usually right, and it's a real
  product decision, not an implementation detail.
- **Idempotency key TTL must exceed the platform's retry window** — otherwise a
  late retry looks brand new.
- **PII.** Retention limits, right-to-delete, and the rule that raw PII never
  enters the vector index or the log tier.

**Failure modes → detection.**

| Failure | Signal |
|---|---|
| "The agent forgot what I told it" | Resolution rate vs turn depth — a cliff at the truncation boundary is diagnostic |
| Lock contention / timeouts | Lock acquisition failures, turn duration p99 |
| Duplicate processing | Idempotency-key hit rate (should be low and stable; a spike means upstream retries) |
| **Cross-customer context leak** | Assert `customer_id` on every loaded history record matches the session. Any mismatch is a Sev-0 page, not a dashboard line |
| State store throttling | DynamoDB throttled-request count |

---

## Layer 3 — Orchestrator / agent loop

**What it does.** 🎤 *This is the actual agent* — everything else is plumbing.
It assembles the prompt, calls the model, parses and validates tool calls,
executes them, feeds results back, and terminates on a final answer or a budget.
It also owns the escalation decision.

```text
loop:
  prompt = system_prompt(merchant) + summary + recent_turns + tool_results
  resp   = model(prompt, tools=enabled_tools(merchant))
  if resp.is_final:            break
  if steps >= MAX_STEPS:       escalate("step budget");  break
  if tokens >= MAX_TOKENS:     escalate("token budget"); break
  if elapsed >= WALL_CLOCK:    escalate("timeout");      break
  validate(resp.tool_call) or  reprompt_once()
  tool_results += execute(resp.tool_call)   # idempotency key required
```

**One service or many.** Its own service, unambiguously. Requests run for seconds
to tens of seconds, are IO-bound, and need high concurrency per instance. If a
turn can *pause* — waiting on a human approval or a slow merchant job — promote
the loop to a durable execution engine rather than holding a thread.

**AWS.** ECS Fargate, async Python (FastAPI/asyncio), consuming from SQS.
Autoscale on queue depth and in-flight turns, not CPU — CPU stays near idle while
you wait on Bedrock. DLQ for poison messages. Step Functions Standard or Temporal
on EKS only if you need durable pause/resume.

**Tricky parts.**

- **Three budgets, not one.** Steps, tokens, and wall-clock. Any one of them
  alone leaves a hole: a cheap two-step loop can still hang on a slow tool.
- **What you do at the budget is a product decision.** Silently stopping is the
  worst option. Escalate with a reason code.
- **Partial failure mid-loop.** Tool 2 of 3 fails — do you retry the tool or the
  turn? Retrying the turn re-executes tool 1. 🎤 *This is why every
  side-effecting tool needs an idempotency key derived from the turn, not
  generated fresh on each attempt.*
- **Never execute model output directly.** Schema-validate tool arguments and
  reject on failure; the model will occasionally invent a parameter or a tool
  that doesn't exist.
- **Streaming vs guardrails.** You can't unsend a token. Either buffer the
  response and pay the latency, or stream with only inline cheap checks and
  accept a narrower safety net. Say which trade you're making.
- **Prompt assembly is where most bugs live** — silent truncation, an unfilled
  template variable, merchant config that failed to load and fell back to a
  default. Log the assembled prompt's hash and length every turn.
- **Cost.** Every loop step is another full-context model call. Prompt caching on
  the stable prefix (system prompt + merchant config) is the single biggest
  lever on both cost and time-to-first-token.

**Failure modes → detection.**

| Failure | Signal |
|---|---|
| Looping / never terminating | Steps-per-turn histogram; alarm when p99 reaches `MAX_STEPS` |
| Hallucinated tool calls | Tool-arg schema validation failure rate |
| Turn latency regression | Per-hop latency breakdown, not just total |
| Cost blowup | Tokens per conversation, p50 and p99, by merchant |
| Wrong tool / no tool when needed | Hardest to detect directly — surfaces via handoff reason codes and the offline golden set |
| Poison messages | DLQ depth (should be zero; any growth is a page) |

---

## Layer 4 — System prompt & merchant config (control plane)

**What it does.** Per-merchant role, policies, hours, tone, catalog pointers,
enabled tools, escalation thresholds, guardrail settings. Versioned and rolled
out gradually.

**One service or many.** Separate service, separate store, and — the part people
miss — **a separate release process**. 🎤 *A prompt push is a production deploy
with the widest blast radius in the system, and it usually has none of the
safeguards a code deploy has.* Fixing that asymmetry is a strong thing to say.

**AWS.** DynamoDB or Aurora for structured config; S3 with versioning for prompt
templates; **AppConfig** for the rollout — it gives you schema validators, a
gradual deployment strategy, and automatic rollback wired to a CloudWatch alarm.
Secrets Manager for merchant API credentials. An in-process cache with a short
TTL so you're not reading config on every turn.

**Tricky parts.**

- **Caching vs freshness.** A merchant updates their hours — how long until the
  agent knows? Pick a TTL and state it (60s is usually fine), plus an
  invalidation path for urgent changes.
- **Validation before rollout.** Reject a prompt version that drops a required
  guardrail section or exceeds a size cap.
- **Version pinning per merchant + instant rollback.** Every served turn records
  which prompt version produced it.
- **Multi-tenancy done right:** one template with per-merchant variables, plus a
  *bounded* free-text customization slot. Merchant-authored text must never be
  able to override the guardrail section — treat your own tenant's config as
  untrusted input. That's prompt injection with a business relationship.
- **Big catalogs don't belong in the prompt.** They belong in retrieval or a
  tool call.

**Failure modes → detection.**

| Failure | Signal |
|---|---|
| Bad prompt regresses quality | Golden-set eval as a CI gate, canary cohort, and AppConfig alarm-triggered rollback |
| Config not propagating | Config version observed in traces vs the published version |
| **Merchant misconfiguration** (no technical bug) | Complaint rate attributed by merchant and config version — this is the Transcript 6 pattern |
| Guardrail section overridden | Assert required sections present in the assembled prompt every turn |

---

## Layer 5 — Retrieval / RAG

**What it does.** Two subsystems that people wrongly treat as one:

- **Indexing (write path)** — ingest catalog, FAQs, policy docs; chunk; embed;
  upsert; and *handle deletes*.
- **Query (read path)** — embed the query, hybrid search (BM25 + vector),
  hard-filter by `merchant_id`, rerank, return top-k **with citations**.

**One service or many.** Two deployables, always. Batch/streaming indexer versus
a low-latency query service — opposite scaling profiles and opposite SLOs. A
bulk reindex must not degrade live query latency.

**AWS.** OpenSearch Serverless for hybrid retrieval with server-side filtering,
or Aurora pgvector below roughly 10M chunks. Embeddings via Bedrock. Indexing:
S3 → EventBridge → SQS → Fargate workers, with DynamoDB Streams or Kinesis for
catalog CDC, and Step Functions for bulk reindex. Bedrock Knowledge Bases if you
want the whole thing managed and can live with less control over chunking.

**Tricky parts.**

- 🎤 **Freshness is the number one issue, and the fix is partly architectural:**
  anything transactional — price, stock, order status, active promos — should
  **not be in the index at all**. It goes through a live tool call. Retrieval is
  for stable content: policies, descriptions, how-tos. Every chunk carries a
  `source_updated_at`, and index lag is a monitored SLO.
- **Tenant isolation.** `merchant_id` is a hard server-side filter. Never a
  filter the model composes, never something enforced only in application code
  that a bug can skip.
- **Chunking decides answer quality more than the embedding model does.** A
  policy chunked mid-clause loses the "except" and produces a confidently wrong
  answer. Chunk on semantic boundaries and repeat the section header into every
  chunk.
- **Deletes.** A discontinued product left in the index is a promise the merchant
  can't honor. Tombstone on delete; reconcile the index against the source
  nightly.
- **Hybrid weighting.** Pure vector search misses exact SKUs and order numbers;
  BM25 catches them. Support traffic is full of exact identifiers.
- **Evaluate retrieval separately from generation.** Recall@k on a labeled set.
  Without it you cannot distinguish a retrieval miss from a generation failure —
  and those have completely different fixes.

**Failure modes → detection.**

| Failure | Signal |
|---|---|
| Retrieval miss | % of turns with zero results above the score threshold; top-1 score distribution shifting; "I don't have that information" rate |
| **Stale answer** | Index lag: `max(now − source_updated_at)` over served chunks, per merchant. Alarm on the tail |
| Cross-tenant leak | Assert `merchant_id` on every returned chunk; any mismatch pages |
| Chunking regression | Recall@k on the golden set, gated in CI |
| Index/query skew | Embedding model version recorded on both write and read; alarm on mismatch |
| Bulk reindex hurting live traffic | Query p99 during indexing windows |

---

## Layer 6 — Tool calling / integration gateway

**What it does.** All egress to inventory, orders, booking, payments, and
merchant-owned APIs. Owns the tool schema registry, per-merchant enablement,
credentials, rate limits, timeouts, circuit breakers, idempotency, and an audit
log of every side-effecting call.

**One service or many.** 🎤 **Its own service, and the boundary worth defending
loudest.** This is where third parties you don't control can hurt you, and where
irreversible things happen. For strong isolation, a Lambda per tool family; for
throughput, a Fargate service with per-tenant bulkheads.

**AWS.** Fargate or Lambda. NAT with fixed EIPs (or PrivateLink) because
merchants allowlist your addresses. Secrets Manager per merchant with rotation.
DynamoDB for the idempotency key table and the audit log. Step Functions with
compensating steps for multi-call transactional flows.

**Tricky parts.**

- **Do the timeout math out loud.** If the chat budget is ~5s and the loop may
  take 3 steps, each tool gets roughly 1s — not the SDK's 30s default. Aggressive
  timeout, one retry with jitter, then degrade.
- 🎤 **Idempotency for side effects.** The key must derive from
  `(conversation_id, turn, tool, hash(args))` so a retry at *any* level — queue
  redelivery, loop retry, gateway retry — collapses to one booking. Generating a
  fresh UUID per attempt is the bug that double-books customers.
- **Bulkheads + circuit breakers.** One slow merchant must not drain a shared
  connection pool. Separate pools per tenant tier; open the breaker on error
  rate, and treat breaker state changes as events you can alert on.
- **Every tool needs a defined degraded answer.** "I can't check inventory right
  now — I can have someone confirm within the hour" is a good outcome. Guessing
  is not. The default must never be to let the model improvise.
- **Partial success needs compensation.** Payment captured, booking failed. Who
  reverses it, and does the customer find out from the agent or from their bank?
- **Merchant APIs change without notice and aren't versioned.** Schema-validate
  every response and alarm on drift — this catches breakage before customers do.
- **Least privilege per tenant.** No shared tokens, no credential reuse across
  merchants.

**Failure modes → detection.**

| Failure | Signal |
|---|---|
| Tool errors / timeouts | Error rate, timeout rate, latency p99 **broken out by merchant** — aggregates hide one broken tenant completely |
| Cascading slowness | Circuit-breaker open events; pool saturation; queue depth upstream |
| **Duplicate side effects** | Idempotency-key collisions, and a direct count of duplicate bookings/charges per conversation |
| Merchant API drift | Response schema validation failure rate, by merchant and endpoint |
| Silent degradation | Ratio of degraded responses to total — a slow climb is a merchant integration rotting |
| Auth expiry | 401/403 rate per merchant; credential age vs rotation SLA |

---

## Layer 7 — Model serving

**What it does.** Inference. In practice tiered: a small fast model for routing,
intent, and classification; a larger one for generation.

**One service or many.** Treat the provider as an external dependency behind
**your own thin model-router service** — so you can swap models, run A/Bs,
enforce per-tenant quotas, centralize prompt caching, and account for tokens in
one place. Adding that indirection later is painful.

**AWS.** Bedrock with provisioned throughput for the predictable baseline plus
on-demand for burst; SageMaker endpoints with vLLM if self-hosting Llama.

**Tricky parts.**

- **Throughput limits show up as 429s during exactly the traffic spike you cared
  about.** Provision the baseline, keep a fallback model for burst, and make the
  fallback path a tested code path rather than a theoretical one.
- **Low temperature is not determinism.** Your evals must tolerate variance;
  exact-match assertions on model output will flake forever.
- **Pin model versions.** A silent provider-side update changes behavior with no
  deploy on your side. Pin, then re-run the golden set before migrating.
- **Context growth is a cost curve, not a cliff** — it degrades quietly. Watch
  tokens per conversation over time.
- **Prompt caching** on the stable prefix is the biggest single lever on latency
  and cost. Structure the prompt so the volatile part is at the end.

**Failure modes → detection.**

| Failure | Signal |
|---|---|
| Throttling | 429 rate, retry count, fallback-model invocation rate |
| Latency | TTFT and total generation p50/p95/p99 |
| Cost regression | Tokens per conversation, alarmed on a rolling baseline |
| Over-refusal | Refusal rate, and its correlation with prompt version |
| Output-format breakage | JSON/schema parse failure rate |
| Quality drift after a version change | Golden-set score, compared across model versions |

---

## Layer 8 — Output guardrails

**What it does.** Content policy, PII scrubbing, format validation, a
**grounding check** (every factual claim traceable to a retrieved document or a
tool result), and a confidence gate that routes to a human.

**One service or many.** Hybrid, and the split is by cost: cheap deterministic
checks (regex, format, denied-phrase, "does this quote a price?") run in-process
on every turn; expensive model-based checks (NLI-style grounding) run as a
service call, and only on **high-risk turns** — anything asserting a price,
discount, date, availability, or commitment.

**AWS.** Bedrock Guardrails covers content policy, denied topics, PII redaction,
and contextual grounding. Comprehend for PII detection if you need it separately.
Lambda for the deterministic rule pass.

**Tricky parts.**

- **A grounding check is another model call** — it can double your latency if you
  run it on everything. Risk-tier it.
- **Streaming conflicts with output guardrails**, structurally. Decide and say so.
- **False positives cost real money too.** Over-blocking produces dead-end
  conversations that look fine on your safety dashboard and terrible to the
  customer.
- **Define the ladder for what happens on a block:** rewrite → one retry →
  canned safe response → escalate. Log which rung fired; the distribution is a
  health metric.
- 🎤 **You cannot measure a guardrail's recall from inside the guardrail.** Only
  a sampled post-hoc audit of *passed* outputs tells you what it's missing. Say
  this — it's the observation that separates people who've shipped one.

**Failure modes → detection.**

| Failure | Signal |
|---|---|
| Upstream regression | Block rate by reason code — a spike is usually a symptom, not a guardrail problem |
| Over-blocking | Block rate vs containment rate; conversations ending in a canned response |
| Guardrail misses (recall) | Sampled human audit of passed outputs; unsupported-claim rate |
| Latency added | Guardrail duration as a share of turn latency |
| PII leakage | Scanner over the outbound corpus, not just the inbound |

---

## Layers 9/10 — Delivery & human handoff

**What it does.** Outbound send with retries, per-channel rate limits, and
ordering; and the escalation path that moves a conversation to a human with full
context.

**One service or many.** Send is a worker in the gateway family. The **agent desk
is a separate product** — UI, routing, queueing, staffing, its own SLOs.

**AWS.** SQS outbound + Fargate senders with a Redis token bucket per
(merchant, channel) + DLQ. Amazon Connect for a managed contact center, or a
custom desk on ECS with AppSync/WebSocket for live updates.

**Tricky parts.**

- **Send can fail after the model has "answered."** Your logs say you replied;
  the customer saw nothing. Reconcile outbound intent against delivery receipts —
  the gap is a real and invisible failure class.
- **Retries fight ordering.** Retrying message 1 after sending message 2 reads as
  incoherent.
- 🎤 **Handoff is a feature, not a failure.** Trigger on low confidence, repeated
  tool failure, refunds/complaints/sentiment, and explicit request — not just the
  last one.
- **Transfer context, don't cold-start the human.** Transcript, what the agent
  tried, what it's unsure about, and why it escalated.
- **Don't promise a human who isn't there.** Off-hours and queue overflow need
  honest messaging and a callback path.

**Failure modes → detection.**

| Failure | Signal |
|---|---|
| Silent send failure | Outbound attempted vs delivery receipts, per channel |
| Ordering breaks | Out-of-order delivery count |
| Handoff rate wrong **in either direction** | Too high = agent isn't useful; a sudden drop = agent got overconfident. Both are alerts |
| Handoff quality | Time-to-human, abandonment while queued, human re-work rate |
| Rate-limit exhaustion | 429s from the Send API by merchant |

---

## Layer 11 — Observability & eval plane

**What it does.** A structured trace per turn, sampled human review, offline
eval, and clustering of flagged conversations into trending issues. 🎤 *For a
support engineer this isn't a supporting layer — it's the job.*

**One service or many.** Fully async, entirely off the request path. Logging must
never be able to delay or fail a reply.

**AWS.** Structured JSON logs → CloudWatch Logs → Firehose → S3 Parquet →
Athena/Glue for analysis; OpenSearch for interactive transcript search; X-Ray or
OpenTelemetry with `trace_id = conversation_id:turn`; CloudWatch metrics and
alarms; Step Functions/Batch for scheduled eval runs.

**Tricky parts.**

- **PII versus debuggability.** You need transcripts to do RCA and you're not
  allowed to keep them freely. Redact at write time, keep a short-TTL raw tier
  behind tight access control, and make the redaction reversible only through an
  audited path.
- **Sampling.** At ~10M conversations/week, 100% tracing is expensive. Sample the
  happy path; keep **100% of flagged, escalated, errored, and low-confidence
  turns**.
- **Replay.** Can you re-run last Tuesday's conversation against today's prompt?
  Only if you stored the exact inputs — retrieved chunk IDs, tool responses,
  config version. Design for it up front; it's nearly impossible to retrofit.
- **Baselines and seasonality** for alerting — covered in
  [Q4 of the round 3 doc](./Interview%203%20-%20Domain%20Expertise%20(GenAI).md#q4-bonus--detecting-issues-at-scale).

---

## Cross-cutting: the latency budget

Worth sketching live — it's concrete, and it forces every other number in the
design. Target ~5s to first response:

| Hop | Budget | Note |
|---|---|---|
| Webhook ack + enqueue | 50ms | Must be trivial; platform retries otherwise |
| Queue + state load | 100ms | DynamoDB single-key read + Redis |
| Config load | ~0 | Cached in-process, short TTL |
| Retrieval | 300ms | Includes embedding the query |
| Tool call | 800ms | **Per call**, and the loop may make several |
| Model generation | 2–3s | Dominates. Prompt caching cuts TTFT |
| Guardrails | 200ms cheap / +800ms if the grounding model runs | Risk-tier it |
| Send | 200ms | |

Two consequences fall straight out of this table: a 3-step loop with a 30s tool
timeout cannot meet the budget, and a grounding check on every turn cannot
either. That's why the tool timeout is ~1s and the grounding check is risk-tiered
— 🎤 deriving those numbers from a budget rather than asserting them is the
difference between a design and a list.

---

## Cross-cutting: what a trace must carry

🎤 If the trace is missing any of these, some class of RCA becomes impossible.
This list *is* the answer to "how would you debug a flagged transcript."

```json
{
  "trace_id": "conv_abc:turn_7",
  "conversation_id": "conv_abc",
  "merchant_id": "m_123",
  "customer_id_hash": "…",
  "channel": "whatsapp",
  "inbound_message_id": "wamid…",
  "prompt_version": "v42",
  "config_version": "m_123@v9",
  "model": "…", "model_version": "…",
  "index_version": "catalog-2026-08-25T04:00Z",
  "prompt_tokens": 3200, "completion_tokens": 180, "cached_prefix_tokens": 2900,
  "retrieval": [
    {"chunk_id": "c_991", "score": 0.81, "source_updated_at": "2026-08-01T…"}
  ],
  "tool_calls": [
    {"tool": "check_inventory", "args_hash": "…", "idempotency_key": "…",
     "latency_ms": 740, "status": "ok", "degraded": false}
  ],
  "guardrails": {"grounding": "pass", "policy": "pass", "action": "none"},
  "steps": 2,
  "latency_ms": {"total": 4100, "retrieval": 290, "tools": 740, "model": 2600},
  "outcome": "answered",
  "escalation_reason": null
}
```

The four version fields — `prompt_version`, `config_version`, `model_version`,
`index_version` — are what let you say *"quality dropped at 14:00, and prompt v42
rolled out at 13:58"* instead of *"something got worse last week."* Attribution
is the whole game.

---

## Symptom → layer triage table

The RCA workhorse. Given a customer complaint, this is how you narrow it.

| Symptom | Candidate layers | The discriminating check |
|---|---|---|
| Quoted a wrong price / stock | 5 stale index · 6 tool failed or returned stale · 7 hallucination | Did the trace show a tool call? Did it return? **Does the number in the response match the tool result?** If no tool call at all → the model invented it; if the tool returned a different number → generation ignored it; if the tool wasn't available → check retrieval `source_updated_at` |
| Duplicate replies | 1 webhook retry · 2 no dedupe · 3 loop | Count inbound `message_id`s vs outbound. **Many identical inbound → layer 1/2. One inbound, many outbound → layer 3** |
| Agent loops, never resolves | 3 budget · 6 tool erroring repeatedly | Steps-per-turn at the cap plus per-step tool status. A tool failing identically each step means the loop is retrying a dead dependency |
| "I don't have that information" too often | 5 recall · 4 over-restrictive prompt · 8 over-blocking | Retrieval hit rate first — zero-result rate is unambiguous. If retrieval was fine, diff the prompt version and check guardrail block reasons |
| Invented a policy or promise | 8 grounding gap · 5 miss | Was a grounding check run on this turn? Are the asserted claims present in any retrieved chunk? |
| Slow | 6 or 7, almost always | Per-hop latency breakdown. Tool p99 by merchant separates "our problem" from "their problem" |
| Forgot earlier context | 2 truncation/summarization | Turn depth vs the truncation boundary; was a summary present in the assembled prompt? |
| Answered about the wrong customer/order | 2 or 5 isolation | `merchant_id`/`customer_id` assertions on state reads and retrieved chunks. **Sev-0** |
| Double booking / double charge | 6 idempotency | Idempotency key present and stable across retries? Audit log for two calls with the same `args_hash` |
| Everything got worse at once | 4 prompt · 7 model · 5 index | Overlay the metric break on the four version timelines. This is the fastest RCA in the whole system, and it only works if you logged the versions |
| One merchant is broken, aggregate looks fine | 4 config · 6 their API | Slice every metric by `merchant_id` before concluding anything. 🎤 *Aggregate dashboards hide the entire long tail, and this is a long-tail product* |
| Nothing is broken | — | The merchant's configured policy genuinely says that. Attribute to config version and route to the merchant, not to engineering |

---

## The five bugs that actually hurt

If you only remember five things going into the round:

1. **Missing idempotency on side effects** — double bookings and double charges.
   Irreversible, customer-visible, and legally interesting. The key must derive
   from the turn, not be generated per attempt.
2. **Stale retrieval on transactional data** — the fix is architectural, not a
   tuning knob: transactional facts don't belong in the index at all.
3. **No bulkhead around merchant APIs** — one slow tenant degrades everyone, and
   the aggregate dashboard looks fine while it happens.
4. **Unversioned prompt pushes** — the highest-blast-radius change in the system,
   usually shipped with none of the safeguards a code deploy gets.
5. **Traces without version and tenant fields** — every other bug on this list
   becomes unattributable, and RCA degrades into guessing.
