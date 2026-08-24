# Story Bank — Rounds 4 & 5, built from the résumé

Companion to [Interview 4 — Hiring Manager](<./Interview 4 - Hiring Manager.md>) and
[Interview 5 — Cross-Functional](<./Interview 5 - Cross-Functional.md>). Those files are the
scaffold — focus areas, question banks, delivery rules. **This file is the filled-in
version**, drafted from `Shu.pdf`.

> **How to use this, and what it is not.** Stories here are built from three
> sources: the résumé, the screening questionnaire Shu submitted, and answers she's
> given since. Where all three agree the detail is solid; where only the résumé
> speaks, it's inference. Two markers appear throughout:
>
> - **[VERIFY]** — a plausible detail that needs to be true. Correct it or cut it.
> - **[FILL]** — something the résumé cannot supply. Only you have it.
>
> Do not walk into the room with a sentence you haven't checked. An interviewer
> who probes one layer past a fabricated detail ends the round. Read each story,
> rewrite it in your own words, and delete anything you can't defend.

---

## Contents

- [The story matrix, filled in](#the-story-matrix-filled-in)
- [The eight stories](#the-eight-stories)
- [Round 4 — the three polished answers](#round-4--the-three-polished-answers)
- [Round 4 — the two questions only you get asked](#round-4--the-two-questions-only-you-get-asked)
- [Round 4 — question → story map](#round-4--question--story-map)
- [Round 5 — six drafted answers](#round-5--six-drafted-answers)
- [What's still open](#whats-still-open)
- [One-page cheat sheet](#one-page-cheat-sheet)

---

## The story matrix, filled in

| Story (handle) | Ambiguity | Customer focus | Quantified impact | Cross-team | Influence | Conflict | Feedback | AI adoption | Career "why" |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **A. Questionnaire assistant** (RAG, 60%, 85%) | ✓ | ✓ | ✓ | | ✓ | | | ✓✓ | ✓ |
| **B. Unified data API** (Meta, 100% rollout) | ✓ | | ✓ | ✓✓ | ✓✓ | ✓ | | | |
| **C. Cell-performance prediction** (Meta + research) | ✓ | ✓ | | ✓✓ | ✓ | ✓ | | ✓ | |
| **D. Carrier partner portal** (maps, Mapbox) | ✓ | ✓✓ | | ✓ | | | ✓ | | ✓ |
| **E. SOC 2 OCR pipeline** (PaddleOCR + translate) | ✓✓ | ✓ | ✓ | | | | | ✓ | |
| **F. Compliance platform** (replaced vendor, $7k/yr) | | ✓ | ✓✓ | | ✓ | ✓ | | | ✓ |
| **G. Marvell regression automation** (SoC, XFN debug) | ✓ | | | ✓✓ | | ✓ | | | ✓ |
| **H. AWS us-east-1 outage** (Oct 2025, 14.5 hrs) | ✓✓ | ✓✓ | | ✓ | | | | | |

Reading the matrix: **feedback is the one thin column left** — see
[What's still open](#whats-still-open). Everything else has at least two entries.

Against the rules in the scaffold doc: three stories carry numbers (A, F, and B's
100%), four are recent (A, E, F, H), four involve people outside your team (B, C,
D, G), A is the AI story, and **A and H both contain real failure** — A has a v1
customers rejected, H has an outage found by a customer rather than by monitoring.
The "slate of clean wins" problem is solved.

---

## The eight stories

Format is the scaffold's: Situation / Action / Outcome / Learning. Keep the
situation to two sentences out loud.

### A. Questionnaire assistant — *the AI story*

> Résumé: *"Built an AI questionnaire assistant that automates enterprise security
> and compliance assessments with RAG, cutting preparation effort by 60% … 85% AI
> answer acceptance rate after customer review."*

**This is the strongest story you have** — and unusually, it's strongest in the
part most people would leave out. It has a v1 that customers rejected, a diagnosis
of *why* that wasn't about model quality, a fix that was a product change rather
than a prompt change, and a measured recovery. That's a complete arc. Tell all
of it; the failure is what makes the success credible.

**S** — Enterprise customers were answering the same security-questionnaire
questions by hand, pulling from policy documents and past responses scattered
across the company. The answers go to *their* customers' auditors — so this isn't
a productivity tool with a quality problem, it's a document with legal exposure
attached.

**A** — Two phases, and the second is the story.

*v1, mid-2024, on the OpenAI API.* I designed the whole retrieval path: ingestion,
chunking, embeddings, vector index, semantic retrieval, generation. Customers
found the quality low — and models were genuinely weaker then — but that wasn't
the real problem. **The system had no transparency.** A customer looking at a
generated answer could not tell what ground truth it came from. Their objection
was completely rational: an unverifiable claim on a compliance document is legal
risk, so they'd rather pay a lawyer than use our tool. They told us so.

*v2 — the fix wasn't a better model.* I built the traceability layer: every answer
is **linked back to the source record in the database**, with the derivation
explained on the backend. Then human review became mandatory rather than a
setting, and the system abstains when retrieval comes back weak instead of filling
the gap.

**O** — 60% reduction in preparation effort. 85% of answers accepted as-is —
measured by the customer's own **accept / edit / reject** click in the review
queue, not by our assessment of ourselves. Trust recovered enough that customers
adopted it, helped along by discounted pricing, and by giving it free to business
partners in exchange for feedback that fed the next iteration.

**L** — The 15% that got rejected splits into **two distinct classes, and they
need opposite fixes:**

1. **Recently-changed controls.** The company had changed a control and the
   knowledge base still held the old version. The answer was right last quarter.
   That's a *freshness* problem — an indexing and invalidation fix.
2. **Questions with no documented answer anywhere.** Not a retrieval failure at
   all — there was nothing to retrieve. That's an *abstention* problem: the correct
   behavior is to say so and route to a person, not to synthesize something
   plausible.

Learning to tell those apart is what changed how I think about these systems. A
single "accuracy" number hides both of them.

**Why this matters beyond the story:** those two classes are, respectively,
**stale/expired data** and **hallucination-where-the-agent-should-defer** — two of
the five failure modes Meta's own guide enumerates for
[Round 3](<./Interview 3 - Domain Expertise (GenAI).md>). You have shipped against
both. Say so when a transcript shows one; it converts a textbook answer into a
first-hand one.

**This story answers:** the AI-native question, "biggest impact," "owned something
end to end," "a time you failed," "difficult customer," "where should we *not* use
AI," and half of "why this role."

**A sub-beat worth pulling out separately** — for *"tell me about a time you had
to learn something quickly."* Vector databases and semantic chunking/indexing were
**new to you on this project**; you learned both from scratch to build the
knowledge base. Recent, honest, and directly relevant to the role.

**Follow-ups to have ready:**

- *"How did you measure the 85%?"* → The customer's own accept/edit/reject action
  in the review queue. It's their judgment, not ours.
- *"What convinced the skeptical customers?"* → Not persuasion — traceability.
  Once they could see the source behind each answer, they could verify in seconds
  instead of trusting blindly. **The general principle to state: when someone
  doesn't trust an AI output, the fix is usually to make it checkable, not to make
  it better.**
- *"Where would you not use it?"* → Anywhere the cost of a confident wrong answer
  is asymmetric and irreversible. Compliance attestations qualify — which is
  exactly why the human step is not optional. Same reasoning as the abstention
  rule in [Interview 3](<./Interview 3 - Domain Expertise (GenAI).md>).
- *"Would you fine-tune instead?"* → See the
  [fine-tuning question](#the-jd-gap--fine-tuning) — it's a stated minimum
  qualification and you need an answer ready.

### B. Unified data-fetch API — *the influence story*

> Résumé: *"Led a team to consolidate fragmented data-fetch APIs into a unified
> interface, building monitoring dashboards to surface cross-dataset discrepancies
> and rolling out the new API to 100% of users."*

**S** — Several surfaces in the partner portal each had their own path to the same
underlying network data, and they disagreed with each other. [VERIFY: did carriers
actually notice the disagreement? If so, lead with that — an external party seeing
inconsistent numbers is a much sharper opening than internal tidiness.] Nobody
owned the inconsistency, and every team's own path worked fine from where they sat.

**A** — I led the consolidation. The engineering was the easy half; the hard half
was that I had no authority over the teams who would have to migrate. Arguing about
which numbers were correct went in circles, so I built the **discrepancy dashboard
first** — per dataset, per metric, old path versus unified path, live. That
converted an opinion argument into a shared artifact people could point at. Then I
migrated consumers one at a time behind a flag rather than asking for a cutover.

**O** — 100% of users on the unified API. Discrepancies got fixed instead of
debated.

**L** — The dashboard should have been week one, not week [VERIFY: four?]. I spent
the early part of that project in meetings that a week of data would have ended.

**This story answers:** influence without authority, cross-team collaboration,
largest-scope problem, "convinced someone who disagreed," and it maps directly onto
the JD line about *performance monitoring for partner integrations*.

### C. Cell-performance prediction with research scientists — *the XFN story*

> Résumé: *"Partnered with research scientists to ship a feature that flags
> underperforming network cells and predicts post-upgrade performance gains,
> helping carriers prioritize infrastructure investments."*

**S** — Research had a model that could flag weak cells and estimate the gain from
upgrading them. Carriers would use that to decide where to spend capital, so a
number that was merely *accurate on average* wasn't good enough — it had to be
defensible to someone spending money on it.

**A** — I worked between the scientists and the carrier-facing surface. Two things
I pushed for: **ship the flagging before the prediction**, because flagging could be
checked against data carriers already had and would earn trust for the harder
claim; and **surface the inputs and the uncertainty**, not a bare predicted number.
[VERIFY: was there real disagreement here? If the scientists pushed back on showing
uncertainty — "it'll make the model look weak" — that tension is the best part of
the story. If it was smooth, don't invent it; tell it as a scoping story instead.]

**O** — Shipped; carriers used it to prioritize upgrades.

**L** — Working with a research partner, the disagreement usually isn't about
whether the model is right. It's about the gap between *accurate* and
*decision-grade*, and that gap is the product engineer's job to close.

**Why this is your strongest XFN story:** it is the Business Agent problem in
miniature — a model output going to an external party who will act on it, where
calibration and explainability matter more than raw quality. Say that connection
out loud if the opening presents itself.

### D. Carrier partner portal — *customer orientation, technical → non-technical*

> Résumé: *"Built interactive network-performance maps for a carrier-facing partner
> portal (React, GraphQL, Relay, Mapbox), featuring dynamic metric bucketing,
> customizable color legends, and region-drawing tools."*

**S** — Carriers needed to see network performance geographically, but "what counts
as bad coverage" differs by carrier, by market, and by whether you're a network
planner or an executive. A fixed set of thresholds and colors was wrong for
everybody.

**A** — Rather than picking the buckets myself, I made the bucketing and legend
configurable and gave them region-drawing so they could ask their own question
instead of the one I'd anticipated. [VERIFY: did this come out of watching a
carrier use an earlier version? If a specific piece of partner feedback caused this
design, that's the story — "I built the thing I thought they wanted, watched them
fight it, and rebuilt it" is a *much* better answer and it also fills the
went-badly slot.]

**O** — [FILL: adoption, usage, or a specific carrier reaction.]

**L** — When a partner keeps asking for one more variant of a view, the real
request is usually control, not the variant.

**This story answers:** customer/stakeholder orientation, explaining technical work
to non-technical audiences, adapting to different audiences (planner vs. exec).

### E. SOC 2 evidence OCR pipeline — *ambiguity, and honest limits*

> Résumé: *"Developed a document intelligence pipeline (PaddleOCR + Google Translate
> API) that converts Chinese SOC 2 evidence into auditor-ready English while
> preserving layout."*

**S** — Audit evidence existed only in Chinese; auditors read English. The manual
workaround was slow and the output was inconsistent between people doing it.
"Auditor-ready" was the hard constraint — an auditor rejects a document that looks
reformatted, so layout had to survive translation.

**A** — Built the OCR → layout-reconstruction → translation pipeline. The judgment
call was **scope by document class**: [VERIFY] clean digital documents went straight
through; scanned pages with stamps, seals, tables, or handwriting were routed to
human review rather than being silently degraded. I'd rather hand back "these 12
pages need a person" than a document an auditor rejects.

**O** — Replaced a manual workflow. [FILL: hours saved per audit, or pages
processed.]

**L** — With a document pipeline, the win isn't accuracy on the average page — it's
knowing which pages you're going to be wrong on, before you're wrong on them.

**This story answers:** working with incomplete information, quality bar,
initiative, and it's a second AI-adoption example if the first gets used early.

### F. Compliance platform replacing third-party tools — *business impact*

> Résumé: *"Shipped a compliance automation platform (Privacy Center, Cookie
> Banner, evidence management, audit workflows) that replaced third-party tools,
> saving approximately $7,000 per customer annually."*

**S** — Customers were paying for several point vendors for things adjacent to what
our platform already did. Build-versus-buy, with the trap that "we can build that"
is easy to say and expensive to be wrong about.

**A** — [FILL: how did you decide? What made *these* components worth building and
something else not? The decision process is the whole story — the interviewer does
not care that you built a cookie banner.]

**O** — ~$7,000 per customer per year eliminated.

**L** — [FILL]

**This story answers:** quantified business impact, "said no to a stakeholder" if
you scoped anything out, trade-offs.

### G. Marvell SoC regression automation — *cross-functional under pressure*

> Résumé: *"Built Python automation tools for SoC integration, validation, and
> regression workflows, and collaborated with cross-functional hardware and software
> teams to debug and validate complex SoC platforms under aggressive release
> schedules."*

**S** — Silicon bring-up, hard tape-out dates, and a failure that could be in the
RTL, the board, the firmware, or the test itself. Hardware and software teams each
had a default assumption that it was the other one's problem.

**A** — [FILL: one specific bug. The one you remember. Who thought it was whose
fault, what you did to discriminate between the hypotheses, how it resolved.]

**O** — [FILL]

**L** — [FILL]

**Why this story is worth reviving even though it's old:** it is the closest thing
on the résumé to the actual job — a multi-party system where the first question is
*whose layer is this*, under a clock, with people who don't work for you. It's the
natural answer to "tell me about a tense working relationship" and to "how do you
work an issue when another team says it isn't theirs." Both are likely XFN
questions and you have nothing else that fits as well.

### H. The AWS us-east-1 outage — *the incident story*

**S** — On **19–20 October 2025**, AWS us-east-1 went down for about 14 and a half
hours. Kaamel ran single-region, multi-AZ in us-east-1. Our EC2 and database were
both affected, and **we found out from a customer**, not from monitoring. Small
company, no follow-the-sun rotation, customers waiting.

**The facts of the outage, so you can speak precisely** — this was public and
well-documented, and getting it right signals you actually understand what
happened rather than remembering that "AWS broke":

- **Root cause:** a latent race condition in DynamoDB's automated DNS management
  produced an empty DNS record for the regional endpoint, removing all its IP
  addresses.
- **The cascade:** DynamoDB DNS → EC2 (new instance *launches* failed) → Network
  Load Balancer health checks → Lambda, ECS, EKS, Fargate, STS and IAM
  authentication, Redshift.
- **The detail that matters operationally: existing EC2 instances kept running.
  Only new launches failed.** Anyone who reflexively restarted an instance that
  day destroyed a working machine they could not get back.

**A — what good looks like.** Rather than reciting what happened, walk the method.
This is the answer to give:

*First 5 minutes — establish scope, don't guess.*
- Confirm it's real and confirm it's not just us. Check the provider's status page
  **and** an independent source; during this event AWS's own Health Dashboard was
  itself degraded, which is a good thing to know out loud.
- Blast radius: all customers or one? All functions or a subset?
- The one discrimination that matters early: **is this our code or our
  dependency?** Nothing shipped on our side, so attention goes to dependencies.

*Next 10 minutes — communicate before you finish investigating.*
- Post a status update while you're still working: what we know, what we don't,
  when the next update comes. Going quiet while you dig is the most common
  unforced error, and support engineering is judged on this as much as on the fix.

*Then characterize precisely — which things fail and which don't.*
- Existing instances healthy, new launches failing, writes erroring, reads
  partially served. That precision is what tells you the safe moves. **Concretely:
  don't restart anything, and turn off autoscaling so nothing gets replaced with
  an instance that can't be launched.**

*Mitigate only what you control.*
- Fail static — degrade to read-only rather than erroring.
- Serve stale cache in preference to a 500.
- Queue writes for replay instead of dropping them.
- Shed non-critical background work to protect what's still up.

*Be honest about what you can't do.* You cannot fix a provider's regional control
plane. Saying "the ETA is not ours to give, here's how we're degrading gracefully
and here's what we'll do the moment it recovers" is the mature answer, and it's
better than inventing a timeline.

**O** — We rode it out and recovered with the region. **[FILL if you want a
number: customer-visible downtime, or how many customers were affected.]**

**L — the real lesson, and it's a good one.** **Multi-AZ does not protect against a
regional control-plane failure.** It protects against losing an availability zone —
power, network, hardware. This failure was regional and it took every AZ with it.
So the answer was to go multi-region.

Then show the trade-off thinking, because "we went multi-region" alone sounds like
a reflex:

> "Multi-region is genuinely expensive for a small company — replication,
> consistency, cost, operational complexity. The question I'd ask now is what RTO
> and RPO the business actually needs, and what's the cheapest architecture that
> meets it. Full active-active is one answer, but warm standby, cross-region
> backups with documented manual failover, or DNS-level failover are all real
> options depending on how much downtime is genuinely unacceptable."

**The support-engineering close — say this, it's the strongest line:**

> "The thing I'd fix first isn't the architecture, it's that a customer told us
> before our monitoring did. If your monitoring runs inside the region that's
> down, it goes down with you. External synthetic checks from outside the region
> are cheap, and they're the difference between finding out from your dashboard
> and finding out from your customer."

**This story answers:** production incident, on-call pressure, working with
incomplete information, communicating during an outage, a time things went badly,
and "what's your approach to reducing on-call load."

**Likely follow-up — "what would you have done differently in the moment?"** Have
one real answer. The honest candidates: escalating to a status page sooner,
or having a documented degraded mode ready instead of improvising one.
**[FILL]**

---

## Round 4 — the three polished answers

### 1. "Walk me through your career"

The thread — memorize the thread, not the words. **Every move has been toward
being closer to the failure and closer to the person hitting it.**

> I started in hardware. At Oracle I was validating enterprise server platforms,
> and at Marvell I was doing SoC integration — which in practice meant that my job
> was other people's bugs, on a deadline, with hardware and software teams each
> sure it was the other one's layer. I started writing Python to automate the
> regression side of that, and I liked the software half more than the hardware
> half.
>
> That took me to Meta in 2018, on a carrier-facing partner portal. I built the
> network-performance mapping surface, and then two things happened that shaped
> what I want to do. One, I ended up owning the shared data layer — several teams
> had their own fetch paths to the same data and they disagreed with each other, so
> I led consolidating them into one API and built the dashboards that showed where
> they diverged. Two, I worked with research scientists to get a prediction model
> in front of carriers who were going to spend real money on it. Both of those were
> the messy shared problem rather than the greenfield feature, and that's the work
> I kept choosing.
>
> Between Meta and Kaamel I took about a year and a half out for a family
> matter. That's the whole of it — I came back wanting to work on AI, which is
> what took me to Kaamel.
>
> Since late 2023 I've been the senior engineer at a small enterprise-AI company,
> which gave me the thing Meta couldn't at my level then: end to end. I design the
> system, I'm in the room with the customer, and I own it in production. Most of
> that has been building customer-facing AI — a RAG assistant that drafts security
> questionnaire responses, at 85% acceptance after human review, and a document
> pipeline for audit evidence. So I've spent two years on the specific problem of
> an LLM being confidently wrong in front of somebody's customer, and what you have
> to build around it.
>
> Which is why this role. It's the same problem at a scale I can't get anywhere
> else, and it's the diagnosis half — which is the half I've been best at since
> Marvell.

Two to three minutes. Time it. **Land on the last sentence** — do not trail off
into the present tense.

### 2. "Why this role? Why support engineering?"

Three concrete hooks, per the scaffold:

- **The problem space.** Agent failures are a new failure taxonomy and the tooling
  for them barely exists — stale merchant catalog, tool-call errors, hallucinated
  policy, loops, and the case where nothing is broken and the merchant configured
  it that way. *"I've already lived the small version of this: 15% of my RAG
  assistant's answers got rejected by reviewers, and figuring out what those 15%
  had in common was the most interesting engineering I did last year."*
- **The work.** Deep troubleshooting across a distributed system, plus being the
  person the partner actually talks to. Name the part you enjoy and be specific —
  the Meta discrepancy dashboards and the Marvell regression work are both evidence
  that you gravitate to diagnosis, not just delivery.
- **The moment.** Business Agent went global in June 2026 and business-AI
  conversations crossed ~10M/week. The support and observability layer for that is
  being built right now, not maintained.

**Do not say** "I want to work on cutting-edge AI."

### 3. "Tell me about difficult feedback you received"

**[FILL — the résumé cannot produce this one, and it is explicitly named in Meta's
own prep guide. Write it yourself before anything else in this file.]**

Requirements, from the scaffold: real criticism, not a humblebrag; you initially
disagreed or found it hard to hear; a concrete behavior change; evidence it stuck.

Where to look in your own history — these are the likely places given the résumé:

- **Meta, the consolidation project.** Leading a migration across teams you don't
  own is where engineers most often get told they moved too fast, over-engineered,
  or didn't bring people along. If someone told you that, that's the story.
- **Kaamel, mentoring interns / running code reviews.** People who are strong at
  the work often get feedback that their reviews are too blunt or too detailed. If
  an intern or a founder told you that, it's a good story *because* the fix is
  observable.
- **Any time a founder or customer told you you were solving the wrong problem.**

---

## Round 4 — the two questions only you get asked

Everything else in the scaffold's question bank is generic. These two are specific
to this résumé, they are both near-certain, and neither has a good improvised
answer. Write them out.

### "What happened between April 2022 and November 2023?"

A ~19-month gap between Meta and Kaamel, visible on the first page. Assume it gets
read even if it doesn't get asked. It was **family** — and that is a complete,
unremarkable answer that needs no elaboration.

The version to say, and then stop:

> "I took about a year and a half out for a family matter. Then I came back
> wanting to work on AI, and that's what took me to Kaamel."

Three rules, and they matter more than the wording:

- **Volunteer it once**, in the career walkthrough, at the point in the timeline
  where it belongs. Narrating a career and stepping over an 19-month hole is what
  creates suspicion; naming it in nine words removes the question entirely.
- **You owe no detail.** "A family matter" is the whole answer. A good interviewer
  will not probe, and if one does, "it's resolved, and I'd rather talk about the
  work" is a perfectly professional close. Nobody is entitled to more.
- **Don't apologize and don't over-explain.** No "unfortunately," no justifying
  the length. Twenty seconds, land forward into Kaamel, move on. The single most
  common way candidates make a gap into a problem is treating it like one.

Do not manufacture a productivity narrative around it — "I used the time to study
LLMs" would be false here, since vector databases and semantic chunking were new
to you on the Kaamel project itself. The plain version is stronger anyway.

### "You're a Senior SWE — why a support role?"

The unstated version: *is this a back door into Meta, and will you be bored and
gone in a year?* Support orgs get a lot of that and the HM is screening for it.
This is the highest-risk question in the loop for you specifically: you were a SWE
at Meta, you're a *Senior* SWE now, and on paper this reads sideways.

**Your actual motivation is AI**, and that's the right thing to lead with — but
it has to be *AI in production, where it breaks, in front of customers*, not AI as
a research interest. The difference decides whether this answer helps or hurts.

The four planks:

1. **Lead with the honest reason.** You want to work on AI, and this is a GenAI
   role — it's in the title. Say it plainly. Then immediately make it specific:
   not "AI is exciting" but "I've spent two years on the problem of an LLM being
   confidently wrong in front of somebody's customer, and I want to do that where
   it's hardest."
2. **The job is engineering, and quote the JD back.** *Build, launch, and optimize
   AI solutions using Llama and other LLMs, owning the full lifecycle from
   prototype to production.* *Develop performance monitoring systems for partner
   integrations.* *Leverage AI tools to accelerate troubleshooting.* That's not a
   ticket queue — and your Meta chapter is literally *"built monitoring dashboards
   to surface discrepancies,"* the same bullet.
3. **It's the work you're actually best at.** Validation at Oracle, integration
   debug at Marvell, the shared-data-layer cleanup at Meta, an AWS regional outage
   last year. The through-line is diagnosing systems under a clock with several
   parties involved. Framed as a *return* to your strongest skill, now pointed at
   AI systems, this is a deliberate move rather than a step down.
4. **You've done the customer-facing half and want it at scale.** Two years at
   Kaamel in the room with customers is what makes the partner-facing part of this
   job appealing rather than a tax.

**Reconcile it with what you already wrote.** Your screening questionnaire says
you're looking for *"product and tech stack"* and *"further career growth and
development."* Assume the hiring manager has that in front of them. Those are thin
answers, and the second is the kind of phrase that invites "growth toward what?"
Have the sharper version ready:

> "What I wrote was 'product and tech stack,' and what I meant by it is this: I
> want to work on an AI product that's actually in front of customers at scale,
> with a stack where the hard problems are real. At Kaamel I own that end to end
> but the scale is small. This is the same problem with several orders of
> magnitude more of it."

**Do not** say "I want to get into Meta and move to a product team later," and
avoid anything implying the role is a stepping stone. **Do not** say "I want to
work on cutting-edge AI" — that's a Research Engineer answer and it signals you'll
be unhappy in support within a year. The distinction to hold: you're interested in
AI *systems in production*, which is what this role is, rather than AI *research*,
which it isn't.

If asked directly about level or comp, that's the recruiter's conversation — say
so pleasantly and move on.

### The JD gap — fine-tuning

Worth its own heading because it's a **minimum** qualification and it isn't on the
résumé. The JD asks for *"knowledge on fine-tuning and optimizations of PyTorch
models and with at least one LLM such as LLaMA, GPT, Claude, Falcon."*

You have deep hands-on LLM experience — OpenAI API, Claude, RAG end to end — and
no PyTorch fine-tuning. Don't bluff it; a single follow-up about learning rates or
LoRA ends badly. Answer with the decision instead, which is genuinely the stronger
ground:

> "I haven't fine-tuned in production, and on the questionnaire assistant that was
> a deliberate call rather than an omission. The corpus was policy documents that
> change — a control gets updated and the answer changes with it. Fine-tuning bakes
> knowledge into weights, so every change means retraining, and you lose the thing
> I most needed, which was being able to point at the source passage behind an
> answer. Retrieval gave me freshness and traceability, and traceability was the
> whole reason customers started trusting the product. Where I would reach for
> fine-tuning is consistent format or style at volume — not knowledge."

That answer demonstrates the judgment the qualification is proxying for. Then be
straightforward that the hands-on gap is real and that you close gaps like this
quickly — vector databases and semantic chunking were also new to you eighteen
months ago.

---

## Round 4 — question → story map

Pick the story, then the one line that lands. Don't recite the whole S/A/O/L unless
they want it.

| Question | Story | The line |
|---|---|---|
| Proudest project / biggest impact | **A** | "60% less prep effort, and 85% accepted — but the 15% taught me more." |
| Owned something end to end | **A** | "Ingestion through human review; I designed all of it." |
| Largest-scope problem you drove | **B** | "No authority over any of the teams that had to migrate. 100% got there." |
| Prioritized a customer over an internal goal | **E** or **C** | "I'd rather hand back 12 pages that need a person than a document the auditor rejects." |
| Frustrated customer/partner | **A** | See [XFN #5](#5-a-frustrated-customer--delivering-bad-news). |
| Explain technical to non-technical | **D** or **C** | "A carrier planner and a carrier exec need the same data at different resolutions." |
| Problem nobody asked you to fix | **B** or **E** | "Every team's own data path worked fine from where they sat. That was the problem." |
| Learned something fast to unblock yourself | **A** | The pivot into RAG/vector systems. [VERIFY the timeline.] |
| Time you failed | **[FILL]** | Best candidates: **D** (built it, watched them fight it, rebuilt it) or the 15% in **A**. |
| Difficult feedback | **[FILL]** | — |
| Production incident / on-call | **[FILL]** = **H** | — |
| Escalate vs. keep working it | **G** or **[FILL]** | "Escalate on blast radius and on new information, not on frustration." |
| Where should we *not* use AI | **A** | "Anywhere a confident wrong answer is irreversible. That's why review isn't a setting." |

---

## Round 5 — six drafted answers

30 minutes, 4–6 questions, so **2–3 minutes each**. These are the six most likely
shapes. Each is drafted; each needs your verification pass.

### 1. Worked with a team outside your own — what was your role?

**Story C.** Research scientists owned the model; I owned everything between the
model and the carrier. My specific contribution was arguing for sequencing —
flagging first because it was checkable against data carriers already had, then the
prediction once the feature had credibility — and for surfacing the inputs and
uncertainty behind a prediction instead of a bare number. Close on: *"the gap
between accurate and decision-grade is the product engineer's job, and that only
gets found by someone sitting between the two teams."*

### 2. Convinced someone who initially disagreed

**Story B**, and lead with the mechanism. Their objection wasn't really "your API is
worse" — it was "mine works and migrating is risk with no upside for me," which is a
legitimate position. So I stopped arguing correctness and shipped the discrepancy
dashboard, which made the divergence visible per metric. Then I made migration cheap
— one consumer at a time, behind a flag, old path live. What I conceded: [VERIFY —
did you keep someone's field naming, add an endpoint you didn't want, extend the
timeline? Name something. *Nobody is persuaded by someone who concedes nothing.*]

### 3. Depended on another team and they were behind

**Story G** or **[FILL]**. The shape that scores: you found out early because you
were checking, not because they told you; you re-sequenced your own work around the
dependency; and you went to the other team with a reduced ask ("I need only this
one field by Thursday") rather than a complaint. Escalation, if any, was a later and
deliberate step with a stated reason — not the first move.

### 4. Tense working relationship / heated disagreement

**Story G** is the natural home — hardware vs. software during bring-up, each side's
default being that it's the other layer's bug. **[FILL the specific incident.]**

Guardrails from the scaffold, and they matter most here:
- Give the other side a legitimate motive. *"Their team was measured on schedule and
  mine on coverage"* makes the story more credible, not less.
- Don't resolve it by escalating, and don't resolve it by capitulating.
- Show a mechanism — an experiment, a shared metric, a time-boxed trial, something
  that made the disagreement checkable.
- Say what the relationship was like afterward. Working with them again, well, is
  the proof.

### 5. A frustrated customer / delivering bad news

**Story A.** [VERIFY the incident, but the shape is almost certainly real given an
85% acceptance rate — 15% means somebody was unhappy at some point.]

The shape: a customer found a generated answer that was wrong about a control they'd
recently changed. What I did — took it as a product bug rather than a user error,
traced it to [VERIFY: a stale document in the index? retrieval pulling an outdated
policy version?], and fixed the class rather than the instance: citations surfaced
on every answer, explicit abstention when retrieval confidence was low, and framing
the deliverable as a draft with evidence rather than an answer. Close on what changed
in the relationship: they went from spot-checking everything to trusting the review
queue, which is the only outcome that proves the fix landed.

Alternative for pure bad news: **Story E** — telling a customer the pipeline could
*not* guarantee fidelity on stamped and handwritten evidence, before they found out
from an auditor. Lead with: *"I'd rather have that conversation than have their
auditor have it."*

### 6. Adapting communication for different audiences

**Story D**, plus a second beat from **A**. Carriers' network planners wanted metric
definitions, bucket boundaries, and the ability to draw their own region; carrier
executives wanted one map that said where to spend. Same data, different resolution
— which is why configurable bucketing and legends were the feature rather than a
setting. Second beat: at Kaamel the same split shows up between a security lead
(wants the source passage) and a founder (wants the acceptance rate). Mention the
documentation/spec angle — the JD explicitly asks for guides that explain complex AI
concepts to diverse audiences — if you have an artifact people actually used. [FILL]

---

## What's still open

Four of the original five gaps are now closed — the incident is Story H, the gap
is answered, the failure story is Story A's v1, and the "learned something fast"
story is vector databases. **One real gap remains, plus a short list of details.**

### The one that matters — difficult feedback you received

Named explicitly in Meta's prep guide (*"think about constructive feedback you've
received and how you've applied it"*), near-certain in Round 4, and nothing in the
résumé, the questionnaire, or anything you've told me can produce it. **Write this
before rehearsing anything else.**

What a usable answer needs: real criticism rather than a humblebrag; a moment where
you initially disagreed or found it hard to hear; a concrete behavior change; and
some evidence it stuck.

Three places in your history where this kind of feedback usually lives:

- **Leading the consolidation at Meta.** Driving a migration across teams you don't
  own is where engineers most often get told they moved too fast, over-engineered,
  or didn't bring people along.
- **Running code reviews and mentoring interns at Kaamel.** People who are strong
  at the work often get told their reviews are too blunt or too detailed. The fix
  is observable, which makes it a good story.
- **Any time a founder or customer told you you were solving the wrong problem.**
  The v1 of the questionnaire assistant is *adjacent* to this — customers told you
  the product wasn't trustworthy — but that's product feedback, not feedback about
  you. If someone framed it as "you built what you thought was right without
  checking whether they'd trust it," that's the story, and it's a strong one.

### Smaller details, in value order

| # | Detail | Unlocks |
|---|---|---|
| 1 | Who else adopted the assistant *internally*, and what convinced any skeptic on the team | "Championed," which is the guide's word — customer adoption is covered, team adoption isn't |
| 2 | The specific discriminating check at Marvell (swapped boards? known-good part? scope?) | Story G's punchline |
| 3 | A number for the OCR pipeline — hours per audit, or pages processed | Story E's outcome |
| 4 | What you'd have done differently during the AWS outage | Story H's follow-up |
| 5 | Whether carriers actually noticed the disagreeing numbers at Meta | Story B's opening — it's much sharper if an external party saw it |
| 6 | The build-vs-buy reasoning on the compliance platform | Story F, currently outcome-only |

### One position, not a story

**Weekend on-call.** Be honestly comfortable with it or don't take the role. The
follow-up worth preparing is the good one — *"what's your approach to reducing
on-call load over time?"* — and you have two pieces of evidence: the discrepancy
dashboards at Meta, and the external-synthetic-monitoring lesson from the AWS
outage. Both are about making problems visible before a human has to notice them.

---

## One-page cheat sheet

Print this. Handles only — reading full answers is audible over video.

```text
A  Questionnaire assistant  v1 had no traceability -> customers chose lawyers
                            link answer to source -> trust -> 60% / 85% accepted
                            the 15% = stale controls + no documented answer
B  Unified data API         no authority · discrepancy dashboard first · 100%
C  Cell prediction + research  flag before predict · show the uncertainty
D  Carrier maps             configurable buckets · planner vs exec
E  SOC 2 OCR                route the hard pages to a human, don't degrade
F  Compliance platform      build vs buy · $7k/customer/yr
G  Marvell bring-up         whose layer is it · deadline · XFN debug
H  AWS us-east-1 Oct 2025   14.5 hrs · multi-AZ != multi-region
                            customer told us before monitoring did

FEEDBACK  ____________________  <- the one still blank
GAP 22-23 family, 18 months, one sentence, land forward
FAILURE   A's v1 · H's detection
LEARN FAST  vector DB + semantic chunking, from zero
FINE-TUNE  haven't; chose RAG for freshness + traceability. Say the reasoning.

Why this role: I want to work on AI in production, where it breaks, in front of
customers · diagnosis is my half · 10M convos/wk, support layer being built now
Rules: headline first · "I" not "we" · 2-3 min · then stop
```
