# Story Bank — Rounds 4 & 5

Companion to [Interview 4 — Hiring Manager](<./Interview 4 - Hiring Manager.md>) and
[Interview 5 — Cross-Functional](<./Interview 5 - Cross-Functional.md>). Those files are
the scaffold — focus areas, question banks, delivery rules. **This file is the
filled-in version.**

> **Rebuilt from [Interview 2](<./Interview 2 - Critical Thinking & Analytical.md>),
> 2026-08-31.** The earlier draft was inferred from the résumé; Part 1 of the Round 2
> prep replaced most of that inference with what actually happened. Where the two
> disagreed, Interview 2 wins. Three episodes that were only in Interview 2 are now
> stories here (**I**, **J**, and the real version of **H**), and the early hardware
> roles are gone entirely — **every story is Kaamel or Meta**, and hardware isn't
> mentioned in any drafted answer, including the career walkthrough.
>
> Two markers remain: **[VERIFY]** — plausible, needs to be true, correct it or cut
> it. **[FILL]** — only you have it. Don't walk in with a sentence you haven't checked.

**Reuse across rounds is fine.** Rounds 2, 4 and 5 are different interviewers. What
they compare is impressions, not transcripts — so the same story can carry Round 2 and
Round 4. What can't repeat is the same story twice *inside* one round.

---

## Contents

- [The story matrix](#the-story-matrix)
- [The seven stories](#the-seven-stories) *(was nine — D and E deleted)*
- [Round 5 — six drafted answers](#round-5--six-drafted-answers)
- [What's still open](#whats-still-open)
- [One-page cheat sheet](#one-page-cheat-sheet)

> **Round 4's drafted answers now live in
> [Interview 4 — Hiring Manager](<./Interview 4 - Hiring Manager.md#question-bank--every-question-with-its-answer>)**,
> along with its questions-only-you-get-asked section and its question→story map.
> The split: **this file holds stories, which get reused across both rounds; each
> interview file holds that round's answers, which don't.** Round 5's six drafted
> answers are still here — move them to Interview 5 if that asymmetry ever bites.

---

## The story matrix

| Story (handle) | Ambiguity | Customer focus | Quantified impact | Cross-team | Influence | Conflict | Feedback | AI adoption | Career "why" |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **A. Questionnaire assistant** (60% / 85%) | ✓ | ✓✓ | ✓✓ | | ✓✓ | ✓ | | ✓✓ | ✓ |
| **B. Unified data API** (Meta, 100%) | ✓ | | ✓ | ✓✓ | ✓✓ | ✓ | | | |
| **C. Cell-performance prediction** (Meta) | ✓ | ✓ | | ✓✓ | ✓ | ✓ | | ✓ | |
| **F. Compliance platform** ($7k/yr) | | ✓ | ✓✓ | | ✓ | ✓ | | | ✓ |
| **H. AWS us-east-1 outage** (Oct 2025) | ✓✓ | ✓✓ | | ✓ | | | | | |
| **I. The 2023 product-selection call** | ✓✓ | | ✓ | | ✓✓ | ✓ | | ✓ | ✓✓ |
| **J. Learning by conversation** (2023) | ✓ | | | | | | | ✓✓ | ✓ |
| **[NEW — slot 1]** *(see gaps below)* | | ✓✓ | | | | | ✓ | | |
| **[NEW — slot 2]** *(see gaps below)* | ✓✓ | ✓ | | | | | | | |

> ### ⚠ D and E are deleted — two open slots
>
> **D (carrier portal / maps)** and **E (SOC 2 OCR pipeline)** have been cut. Every
> pointer to them in this file and in the Round 4 / Round 5 docs is now marked
> **[GAP]**. Two new stories are needed, and they are not interchangeable — each one
> was load-bearing for a different thing:
>
> | Slot | Must cover | Why it can't just be dropped |
> |---|---|---|
> | **1 — replaces D** | Explaining something technical to a non-technical audience; adapting the same content for two audiences | **The most urgent of the two.** D was the *only* story here, it's a named Round 5 focus area, and it maps to a JD line (*"communicate complex AI concepts to diverse audiences"*). Round 5 answer #6 currently has no primary story. |
> | **2 — replaces E** | Prioritizing a customer over an internal goal; delivering bad news / stating an honest limit before the customer discovers it | A's adoption arc partly covers bad news, but A is already carrying three other slots. This slot exists so A isn't told four times in one loop. |
>
> Interim coverage until they're written: **C** can carry technical→non-technical
> (research scientists ↔ carriers), and **A**'s adoption arc can carry bad news.
> Both are stretches, and both mean repeating a story inside a single round.

Against the scaffold's rules, with D and E gone: **A**, **F** and **B** carry numbers;
**A**, **F**, **H** are recent; **B**, **C**, **H** involve people outside your team —
now exactly three, so the rule is met with zero margin; **A** and **J** are the AI
stories; and **A** and **H** both contain real failure — a v1 customers declined to
buy, and an outage a customer found before monitoring did.

**Feedback is still the one thin column**, and customer-facing communication is now
the second. See [What's still open](#whats-still-open) — write the feedback story
first, then slot 1.

---

## The seven stories

Each story is written in four parts. It's STAR without the separate *Task* step —
Meta's guide asks for *"situation, your actions, outcome"* in exactly those words, and
the fourth part is the one the guide doesn't ask for but interviewers reward.

| Part | What goes in it | The failure mode it guards against |
|---|---|---|
| **Situation** | One or two sentences: the setup, and *why it was hard*. | Three minutes of context before any action — the most common way these rounds are lost. |
| **Action** | What **you** did, and the judgment behind it. "I," not "we." | A story where the team did everything and your own contribution is invisible. |
| **Outcome** | The result, with a number if one exists. State it once, flatly. | An unresolved story, or a number inflated into a follow-up you can't survive. |
| **Learning** | What it changed about how you work, or what you'd do differently. | A clean win with nothing behind it. This is where seniority actually shows. |

**Situation is the part to cut, Learning is the part to land.** Out loud, the shape is
two sentences of setup → most of your time on Action → the number → the principle, then
stop and let them probe.

> **Don't confuse the labels with the handles.** Stories are lettered **A**–**J**; the
> four parts are spelled out. So "**A**" always means the questionnaire assistant, never
> "Action" — that matters most in [Story I](#i-the-2023-product-selection-call--judgment-on-thin-information),
> where the Action has two beats.

### A. Questionnaire assistant — *the AI story*

> Résumé: *"Built an AI questionnaire assistant that automates enterprise security and
> compliance assessments with RAG, cutting preparation effort by 60% … 85% AI answer
> acceptance rate after customer review."*

**The strongest story you have**, and strongest in the part most people would leave
out: a launch customers wouldn't buy, a discount that did nothing, a correct diagnosis
of why, and a measured recovery. Three separable arcs live in it — requirements,
adoption, and the 15% — so it can be told three ways without repeating itself.

**Situation** — Enterprise customers answer the same security-questionnaire questions by
hand, pulling from policy documents and past responses scattered across the company. The
answers go to *their* customers' auditors. It isn't a productivity tool with a quality
problem; it's a document with legal exposure attached.

**Action** — Three phases.

*Requirements.* What I was handed was "the answers have to be high quality and satisfy
the customer" — an adjective, not a spec, and the customers couldn't define it either.
So I asked them, and asked the lawyers who'd be on the hook if an answer was wrong. Not
"what does quality mean" — *what do you care about most.* Same answer every time: **is
it correct, and if this gets challenged, how do I defend it?** Nobody said
"traceability." Translating "defend" into four properties I could build and test was my
job:

- every answer grounded in the knowledge base, not the model's general knowledge;
- every answer traceable to the record it came from;
- when the knowledge base has nothing — no assumption; surface it as unknown and hand
  off to a person;
- human review in the loop, so every miss returns as signal.

*Launch, mid-2024 — and it didn't sell.* Models were weaker then and the stated
complaint was "answer quality is low." We had a price lever, so we used it. The
discount did **nothing** — not a small effect, none. That's what told me I'd misread
the objection. Going back to the actual concern: these answers go to auditors, and a
plausible answer they couldn't verify was legal exposure. They weren't declining to pay
for a mediocre tool; they were declining to put their name on something they couldn't
check.

*The fix, which was a product change and not a model change.* The system could already
trace every answer to its source record — the customer just couldn't see it.
**Provenance you can't see isn't provenance, it's a log.** So: surface the source on
every answer in the product; make human review mandatory rather than a setting; and
partner with a handful of customers, access in exchange for a real feedback loop. The
product decisions were mine. I influenced the pricing call but didn't own it.

**Outcome** — 60% reduction in preparation effort. 85% of answers accepted as-is,
measured by the customer's own **accept / edit / reject** click in the review queue, not
by our assessment of ourselves. The discount only started working once it was buying
*feedback* rather than *adoption*. With Drata it ended up fully reciprocal — they use
our product, we use theirs.

**Learning** — Two things. First: **you can't discount your way past a trust problem.
When someone doesn't trust an AI output, the fix is to make it checkable — not cheaper,
and usually not even better.** Second, the 15% that still got rejected splits into two
classes that need opposite fixes:

1. **Recently-changed controls** — the answer was right last quarter. A *freshness*
   problem: indexing and invalidation.
2. **Questions with no documented answer anywhere** — not a retrieval failure, there
   was nothing to retrieve. An *abstention* problem.

A single "accuracy" number hides both. Those two are, respectively, **stale data** and
**hallucination-where-the-agent-should-defer** — two of the five failure modes Meta's
own guide enumerates for
[Round 3](<./Interview 3 - Domain Expertise (GenAI).md>). You've shipped against both.

**Answers:** the AI-native question, biggest impact, owned end to end, a time you
failed, frustrated customer, where *not* to use AI, influence, half of "why this role."

**Follow-ups:**

- *"How did you measure the 85%?"* → The customer's own accept/edit/reject action. Their
  judgment, not ours.
- *"Traceability or mandatory review — which mattered more?"* → Traceability. Review is
  a cost you impose; traceability is what makes it cheap. Without it a reviewer
  re-derives the answer; with it they check a link in seconds. I didn't make them trust
  the output — I made verifying it faster than doing it themselves.
- *"Models got much better over that period — how do you know it was your changes?"* →
  **Expect this.** They did, and I won't claim the model didn't help. But the objection
  customers stated was verifiability, not fluency, and the 15% still rejected afterward
  weren't model failures either — stale controls and undocumented questions. A better
  model fixes neither.
- *"How did you choose the feedback partners?"* → **[FILL — one sentence on the
  criterion. "The hardest questionnaires, not the friendliest customers," if true.]**
- *"Would you fine-tune instead?"* → [see Interview 4](<./Interview 4 - Hiring Manager.md#the-jd-gap--fine-tuning>).

*On naming Drata:* fine if the partnership is public. If you're not certain, say "a
compliance-automation platform we partner with" and keep the reciprocity — that's the
part that carries the point.

### B. Unified data-fetch API — *the influence story*

> Résumé: *"Led a team to consolidate fragmented data-fetch APIs into a unified
> interface, building monitoring dashboards to surface cross-dataset discrepancies and
> rolling out the new API to 100% of users."*

**Situation** — Several teams each had their own path to the same network data, and the
numbers disagreed. [VERIFY: did carriers notice? If an external party saw inconsistent
numbers, lead with that — it's a much sharper opening than internal tidiness.] Every
team's own path worked fine from where they sat, and nobody owned the inconsistency.

**Action** — My instinct was to escalate for a ruling. I didn't, because **nobody had
the information to make that call, including me** — escalating would only have moved the
argument up a level.

The reframe is the whole story. The question I cared about wasn't *whose* numbers were
wrong, it was *why* they disagreed. Those sound similar and produce completely
different conversations: one asks people to defend themselves, the other asks them to
look at the same thing. So I built the discrepancy dashboard first — per dataset, per
metric, every path against the unified one, live. That made the discrepancy the subject
instead of the teams. Then I migrated consumers one at a time behind a flag rather than
asking for a cutover.

**Outcome** — 100% of users on the unified API. The discrepancies got fixed instead of
argued about.

**Learning** — **If all you have is a disagreement, go get the information first, then
escalate.** And keep the problem as the subject rather than the people — blame doesn't
reconcile a dataset. The dashboard should have been week one, not week [VERIFY: four?];
I spent the early part of that project in meetings a week of data would have ended.

**Answers:** influence without authority, cross-team collaboration, largest-scope
problem, convinced someone who disagreed, escalate-vs-keep-working, and the JD line
about *performance monitoring for partner integrations*.

### C. Cell-performance prediction with research scientists — *the XFN story*

> Résumé: *"Partnered with research scientists to ship a feature that flags
> underperforming network cells and predicts post-upgrade performance gains, helping
> carriers prioritize infrastructure investments."*

**Situation** — Research had a model that flagged weak cells and estimated the gain from
upgrading them. Carriers would spend capital on that number, so *accurate on average*
wasn't good enough — it had to be defensible to someone signing for it.

**Action** — I owned everything between the model and the carrier. Two things I pushed
for:
**ship the flagging before the prediction**, because flagging could be checked against
data carriers already had and would earn credibility for the harder claim; and
**surface the inputs and the uncertainty**, not a bare predicted number. [VERIFY: was
there real disagreement — did the scientists push back on showing uncertainty because
it would make the model look weak? If so that tension is the best part. If it was
smooth, tell it as a scoping story and don't invent the conflict.]

**Outcome** — Shipped; carriers used it to prioritize upgrades.

**Learning** — With a research partner the disagreement usually isn't about whether the
model is right. It's the gap between *accurate* and *decision-grade*, and closing that
gap is the product engineer's job.

**Why it's your strongest XFN story:** it's the Business Agent problem in miniature — a
model output going to an external party who will act on it, where calibration and
explainability matter more than raw quality. Say that connection out loud.

### ⚠ [GAP — slot 1] *replaces D: technical → non-technical, adapting to audiences*

**Deleted:** D, the carrier partner portal / network-performance maps.

Write the replacement to the same four-part scaffold. What it has to do, in priority
order:

1. **Two audiences, same content, different resolution.** The whole point of the slot.
2. **Show the translation act itself** — what they said vs. what you had to write down
   or draw. Generic "I avoided jargon" is worth nothing here.
3. **Ideally an artifact** someone else used — a doc, a guide, a diagram. The JD asks
   for guides explaining complex AI concepts to diverse audiences, and an artifact
   answers that JD line directly.

*Where this gets asked:* Round 5 answer #6 (its primary story — currently empty),
Round 5's audience-adaptation focus area, Round 4's "explain technical to
non-technical." **This is the higher-priority of the two slots.**

### ⚠ [GAP — slot 2] *replaces E: customer over internal goal, honest limits*

**Deleted:** E, the SOC 2 evidence OCR pipeline.

What the replacement has to do:

1. **A real cost you absorbed** to protect the customer — the internal goal you gave
   up has to be named, or it isn't a prioritization story.
2. **Bad news you delivered before it was discovered.** The structure that scores is
   *you told them, they didn't find out.*
3. **A stated limit**, not a hedge — "this doesn't work on X, here's the handoff."

*Where this gets asked:* Round 4's "prioritized a customer over an internal goal" and
"problem nobody asked you to fix," Round 5 answer #5's pure-bad-news alternative.

### F. Compliance platform replacing third-party tools — *business impact*

> Résumé: *"Shipped a compliance automation platform (Privacy Center, Cookie Banner,
> evidence management, audit workflows) that replaced third-party tools, saving
> approximately $7,000 per customer annually."*

**Situation** — Customers paid several point vendors for things adjacent to what our
platform already did. Build-versus-buy, with the trap that "we can build that" is cheap
to say and expensive to be wrong about.

**Action** — [FILL: how did you decide? What made *these* components worth building and
something else not? The decision process is the whole story — nobody cares that you
built a cookie banner.]

**Outcome** — ~$7,000 per customer per year eliminated.

**Learning** — [FILL]

**Answers:** quantified business impact, said no to a stakeholder (if you scoped
anything out), trade-offs.

### H. The AWS us-east-1 outage — *the incident story*

**19–20 October 2025.** AWS us-east-1 was down about 14 and a half hours. Kaamel ran
single-region, multi-AZ, in that region. Small company, no follow-the-sun rotation.

**Both decisions in this story are restraint** — you defer two erroring components,
then you stop engineering entirely. Most incident answers are heroics; this is judgment
about what *not* to do, which reads as senior.

**Situation** — A customer told us they couldn't log in. A customer — not our
monitoring.

**Action** — The logs were all on fire: SSO, the AI gateway, the database, all erroring.
That's the decision point. With three components failing the temptation is to chase all
three; I anchored on the one a user had actually reported. The others were hypotheses,
login was a confirmed impact. So I deferred them deliberately.

Login was failing to fetch a token from AWS Secrets Manager. We were multi-AZ in
us-east-1 and the outage took the whole region — **multi-AZ bought us nothing.** AWS had
acknowledged it with no ETA. So instead of waiting I asked what we had *outside* the
region: Secrets Manager in us-west-1, not actively in use, and the token was already
there. I cut login over and users could get in.

Then the second wave. They were in, but the AI gateway and the database were degraded —
over half our capacity gone and no cross-region copy of either. Nothing left to
engineer. But it wasn't a hard down; requests were succeeding intermittently. So the
job changed: I worked with colleagues to tell customers what was happening, that full
recovery depended on AWS, and that retrying genuinely did work some of the time.

**Outcome** — Login restored while the region was still down; the rest rode it out and
recovered with AWS. **[FILL if you want a number: customer-visible downtime, or
customers affected.]**

**Learning** — Two, and the second is the one to land:

- **Multi-AZ does not protect against a regional control-plane failure.** It protects
  against losing an AZ — power, network, hardware. This was regional and took every AZ
  with it.
- **When everything is erroring at once, start where a user told you it hurts. Logs
  tell you what's unhappy; a user tells you what's broken.**

**Name the luck.** The token *being* in us-west-1 was luck. Looking outside the region
wasn't. Say both — claiming the whole thing as foresight is the one way this loses
credibility, and volunteering the split buys the rest of it.

**Answers:** production incident, on-call pressure, incomplete information,
communicating during an outage, a time things went badly, reducing on-call load.

**Probes:**

- *"What actually caused it?"* → A latent race in DynamoDB's automated DNS management
  emptied the regional endpoint's DNS record; cascade into EC2 launches, NLB health
  checks, Lambda/ECS/EKS, STS and IAM. **The operational detail worth adding:** existing
  EC2 instances kept running — only *new launches* failed, so anyone who reflexively
  restarted destroyed a working machine they couldn't get back. Don't volunteer this
  unasked; it reads as rehearsed trivia.
- *"Why not work the database and gateway errors in parallel?"* → One person, and they
  were plausibly downstream of the same event. Serial beats parallel when you're alone,
  and confirmed impact outranks a suspicious log line.
- *"What would you have done differently?"* → **[FILL — have one real answer.
  Candidates: a status update posted before the investigation finished, or a documented
  degraded mode instead of improvising one.]**
- *"So you'd go multi-region?"* → Don't answer that as a reflex. "Multi-region is
  genuinely expensive for a small company — replication, consistency, cost, operational
  complexity. The question is what RTO and RPO the business actually needs and the
  cheapest architecture that meets it. Warm standby, cross-region backups with a
  documented manual failover, or DNS-level failover are all real answers depending on
  how much downtime is truly unacceptable."
- *"What would have caught this automatically?"* → **The close for any RCA in this
  loop.** External synthetic monitoring — a login probe run from outside the region. If
  your monitoring lives in the region that's down, it goes down with you. The real
  failure wasn't the outage; it was that a customer knew before we did. **This is also
  your answer to "how do you reduce on-call load."**

### I. The 2023 product-selection call — *judgment on thin information*

Not on the résumé, and it's the best evidence in the bank that you commit without
certainty. **Two beats.** They come from one body of work, so **never tell both to the
same interviewer** — pick the one the question asks for.

**Situation** — Late 2023, newly joined Kaamel. AI was obviously powerful, which was the
problem: too many ideas and no basis to choose. Resume generation, enterprise travel and
hotel booking, a dozen others — and real pressure, because the fear was falling behind
while we deliberated. There was no data. The market didn't exist yet in any measurable
form.

**Action —** *beat 1, killing a project as a new hire.* Work was already underway on an
AI resume generator. I was skeptical, and the reason was first-hand: I'd been job
hunting not long before and used ChatGPT to write my resume. **I was the target
customer, and I wouldn't have paid for it.**

But that's one person's experience, and as a new hire an opinion is the weakest thing
you can bring into a room. So I did the competitor study and the market sizing first,
and when I raised it I said plainly which part was evidence and which part was me. I
put the question on the product, not on the people who'd been building it. The project
was stopped.

**Action —** *beat 2, choosing the direction.* I went after the cheapest real evidence
available: I counted competitors in each area, and — our building was full of startups —
I walked around asking people what they were working on. Not rigorous, but a live sample
of everyone having the same idea we were, and I had it in [VERIFY: days? a week?]. Same
procedure I'd run on a hard bug: I couldn't get the measurement I wanted, so I took the
one I could get and used it to rule things out.

That reframed the question. The ideas we liked were crowded — and crowded *because*
they need no domain expertise. Anyone can build a resume generator, which is exactly
why we couldn't win one. So I wrote up each area against a single criterion: where do
we have a moat. That pointed at compliance — SOC 2 with AI. Less popular, harder to
enter, and we had the three things that mattered: a lawyer in the founding group with
real domain expertise, customer relationships through our CEO, and a market that was
going to expand, because China's economy runs on exporting and exporters need this.

**Outcome** — I did that analysis and made the recommendation. It's the business we're
in today, and we're a profitable small company — which at this size is the answer to
whether the call was right.

**Learning** — **When you can't get the information you want, get the information you
*can*, and use it to eliminate rather than to pick.** And low competition isn't always a
warning — sometimes it's the only evidence you have that something is hard to copy.

**Answers:** decision with limited information, influence without authority, pushed for
a change that wasn't your call, said no, a tense disagreement (beat 1), problem nobody
asked you to fix, how you make a case with no data, and the front half of "why AI."

**Probes:**

- *"Wasn't that risky, weeks into a new job?"* → The risk isn't disagreeing, it's
  disagreeing with nothing behind you. That's why the market study came before I opened
  my mouth, not after.
- *"How do you know that wasn't luck?"* → Separate the decision from the outcome. The
  reasoning was that we could only win where entry was hard, and hard entry meant domain
  expertise, of which we had exactly one kind. If the market had gone the other way that
  would still have been the right way to choose.
- *"What would have changed your recommendation?"* → Two things. If the walk around the
  building had turned up three teams already doing compliance, or if the domain
  expertise hadn't been in the founding group — a moat you have to hire for isn't a moat
  yet.
- *"What if you'd been wrong about the resume generator?"* → Then the study would have
  shown it and I'd have said so. I wasn't asking anyone to trust my judgment; I was
  putting the same information in front of everyone.

**The risk in Round 4.** This is a strategy story in an operational loop. It lands as a
differentiator if the *method* reads as engineering — enumerate, pick the criterion
that discriminates hardest, get cheap evidence, eliminate — and as a liability if it
sounds like you'd rather be founding a company than debugging a partner integration.
**"Same procedure I'd run on a hard bug" is the insurance. Don't cut it.**

### J. Learning by conversation — *learned something fast*

Replaces the old "vector databases and semantic chunking" answer, which was true but
generic. This one is about how you decide what to believe, which nobody else will say.

**Situation** — 2023, two things new at once: SOC 2, which I knew nothing about, and
building on LLMs, which barely existed as a discipline. I'd normally learn a domain by
collecting materials and studying systematically. Instead I learned by conversation with
the model.

**Action** — The risk isn't that the model is sometimes wrong. It's that **when you're
new you can't tell which parts are wrong — a novice can't grade the tutor.** So I leaned
on the checks that don't require expertise.

- **Consistency, the cheapest one.** Track what it told you earlier; contradictions are
  free to spot without knowing the domain.
- **Watch the premises, not just the answers.** It once told me to fix a quality problem
  by switching between LLMs and comparing them. We only had the OpenAI API, so switching
  was never an option — and the problem wasn't model-related anyway. I stated the
  constraint rather than just rejecting the suggestion. **Constraints aren't context,
  they're the search space.** Until you state them it keeps optimizing somewhere you
  don't live.
- **Anything load-bearing, go find the published document and check it echoes.** Plus
  the lawyer in our founding group for the domain calls.

**Outcome** — Competent enough to design and ship the retrieval path within [VERIFY:
months?], in two domains I'd started from zero in.

**Learning** — **Use the model to find the questions, never to settle them.**

**Answers:** learned something quickly, how you stay current, AI in your own workflow,
"isn't that outsourcing your thinking," adaptability.

**Probes:**

- *"Isn't that outsourcing your thinking to a chatbot?"* → **Expect this.** It moved my
  effort from reading to verifying, and verifying is the harder half. Studying
  systematically means studying *uniformly*, because you can't yet tell what matters.
  Conversation finds the ten percent that's load-bearing — then you verify that properly.
- *"How do you decide what's worth verifying?"* → Where something smells wrong, or where
  being wrong is expensive and hard to reverse. I can't verify everything, so I verify
  what the rest rests on.
- *"How do you work now?"* → ChatGPT, Claude and Cursor across design, planning and
  coding. On a new initiative I hand it the requirement, have it break the product into
  components, then work through them one at a time — output is a draft, not an answer.
  The thing that changed my results most: **as a conversation gets long the model loses
  earlier context and quality degrades without telling you**, so I manage context
  deliberately instead of letting a thread sprawl. More effect than any prompt wording.

---

## Round 5 — six drafted answers

30 minutes, 4–6 questions, so **2–3 minutes each**.

**Name the other party's legitimate motive in every one of these.** It's the single
highest-signal habit in the round, and four of the six have an obvious one.

### 1. Worked with a team outside your own — what was your role?

**Story C.** Research scientists owned the model; I owned everything between the model
and the carrier. My contribution was arguing for sequencing — flagging first, because
it could be checked against data carriers already had, then the prediction once the
feature had credibility — and for surfacing the inputs and uncertainty behind a
prediction rather than a bare number. Their motive was legitimate: they were measured
on model quality, and showing uncertainty makes a good model look hedged. Close on:
*"the gap between accurate and decision-grade is the product engineer's job, and it
only gets found by someone sitting between the two teams."*

### 2. Convinced someone who initially disagreed

**Story B**, and lead with the mechanism. Their objection wasn't really "your API is
worse" — it was "mine works, and migrating is risk with no upside for me," which is a
legitimate position. So I stopped arguing about who was correct. The question I put in
front of everyone wasn't *whose numbers are wrong*, it was *why do they disagree* — and
the discrepancy dashboard made that checkable per metric instead of arguable. Then I
made migrating cheap: one consumer at a time, behind a flag, old path still live. What
I conceded: **[VERIFY — did you keep someone's field naming, add an endpoint you didn't
want, extend the timeline? Name something. Nobody is persuaded by someone who concedes
nothing.]**

### 3. Depended on another team and they were behind

**Story C** is the best available home — the model was upstream of everything I owned.
**[FILL: a specific slip and what you did.]** The shape that scores: you found out early
because you were checking, not because they told you; you re-sequenced your own work
around it (the flag-before-predict split is genuinely this); and you went to them with
a reduced ask — *"I need only this one field by Thursday"* — rather than a complaint.
Escalation, if any, was a later and deliberate step with a stated reason.

*If C won't stretch:* **H** works as a dependency story where the dependency was AWS —
you can't escalate to a provider, so the moves are what you own outside the blast
radius and what you tell customers meanwhile.

### 4. Tense working relationship / heated disagreement

**Story I, beat 1** — the resume generator. This is the honest one: weeks into the job,
telling a team that the thing they'd been building should stop. Real tension, and no
manufactured villain.

What makes it work in this round:

- **Their motive was legitimate.** They'd committed real work to it and the market
  looked wide open at the time. I wasn't smarter than them; I'd happened to be the
  target customer.
- **A mechanism, not an opinion.** The competitor study and market sizing existed
  before I said anything, and I labeled out loud which part was evidence and which part
  was me — *"I was the target customer and I wouldn't have paid for it"* is a data point
  of one and I said so.
- **The question went on the product, not the people.**
- **Afterward:** [FILL — did you work with the same people on the compliance product?
  If so, say it. Working with them again, well, is the proof.]

*Note:* the guidance not to resolve conflict by escalating still holds — this resolved
by evidence, and the decision was the founders' to make.

### 5. A frustrated customer / delivering bad news

**Story A**, the adoption arc. Customers had told us the answer quality was low, we
discounted, and it changed nothing. The bad-news conversation was internal first —
telling the company our read on the objection was wrong and the price lever was dead —
and then external: going back to customers to ask what would actually make this usable,
which means hearing "I'd rather pay a lawyer" without arguing.

What I did with it: treated it as a product problem rather than a persuasion problem.
Surfaced the source record on every answer, made human review mandatory instead of a
setting, and traded access for a real feedback loop with a few customers. Close on what
changed in the relationship — with Drata it ended up reciprocal, they use our product
and we use theirs, which is a different thing from a customer accepting a discount.

*Alternative for pure bad news:* **⚠ [GAP — slot 2]**. This was Story E, now deleted.
Until the replacement is written this question has only one answer, A, which is also
the answer to "frustrated customer," "time you failed," and the AI question. **Writing
slot 2 is what stops A from being told four times in one loop.**

### 6. Adapting communication for different audiences

**⚠ The primary story for this answer was D, which is deleted. See
[GAP — slot 1](#-gap--slot-1-replaces-d-technical--non-technical-adapting-to-audiences).**
This is the emptiest answer of the six and the one most clearly named in the round's
focus areas — write slot 1 before rehearsing Round 5.

What survives, and it's the sharper half anyway — the **second beat from A**: at Kaamel
the audience split is a security lead who wants the source passage versus a founder who
wants the acceptance rate, and the requirements work on the assistant was exactly this.
What the customer said was *"defend it"*; what I had to write down was *"traceable to
the source record."* Translating between those two vocabularies was the job.

Two problems with leaning on it alone: it's a *second* beat with no first beat in front
of it, and A is already the primary story for three other questions. It's a bridge, not
an answer.

Mention the documentation angle — the JD asks for guides explaining complex AI concepts
to diverse audiences — if you have an artifact people used. **[FILL]** *(an artifact
here would also make a strong spine for slot 1 itself)*

---

## What's still open

### The one that matters — difficult feedback you received

Named explicitly in Meta's prep guide, near-certain in Round 4, and nothing in the
résumé or in Interview 2 can produce it. **Write this first.** Requirements and the
three likely places are in
[Interview 4](<./Interview 4 - Hiring Manager.md#-tell-me-about-difficult-feedback-you-received-what-did-you-do-with-it>).

The guide also asks for feedback in **both directions**, and the giving half is more
likely in Round 5. Mentoring and code review at Kaamel is the obvious source. **[FILL]**

### Two whole stories — the D and E replacements

D and E are deleted. **Slot 1** (technical → non-technical, adapting to audiences) and
**slot 2** (customer over internal goal, honest limits) both need new stories written
to the four-part scaffold; requirements for each are in
[the seven stories](#the-seven-stories), and the consequences of leaving them empty are
marked **[GAP]** throughout this file.

**Priority: slot 1 ranks second overall, behind only the feedback story.** It's a named
Round 5 focus area, it maps to a JD line, and Round 5 answer #6 has no primary story
without it. Slot 2 ranks below the smaller details — A covers it as a stretch.

### Smaller details, in value order

| # | Detail | Unlocks |
|---|---|---|
| 1 | Who adopted the assistant *internally*, and what convinced a skeptic on the team | "Championed," the guide's word — customer adoption is covered, team adoption isn't |
| 2 | How you picked the feedback partners | Story A's last probe |
| 3 | What you'd have done differently during the outage | Story H's most likely follow-up |
| 4 | Whether carriers actually noticed the disagreeing numbers | Story B's opening — much sharper if an external party saw it |
| 5 | A concrete slip on the research-model dependency | Round 5 #3, currently the weakest of the six |
| 6 | The build-vs-buy reasoning on the compliance platform | Story F, currently outcome-only |
| 7 | Whether you worked with the resume-generator team afterward | Story I beat 1's close |
| 8 | A specific instance of the retrieval bug (plausible wrong answer, no error) | The AI-flavored debugging story, if they ask for one |

### One position, not a story

**Weekend on-call.** Be honestly comfortable with it or don't take the role. The
follow-up worth preparing is the good one — *"what's your approach to reducing on-call
load over time?"* — and you have two pieces of evidence: the discrepancy dashboards at
Meta, and external synthetic monitoring from the AWS outage. Both are about making
problems visible before a human has to notice them.

---

## One-page cheat sheet

Print this. Handles only — reading full answers is audible over video.

```text
A  Questionnaire assistant  "high quality" -> 4 testable properties (ask the lawyers)
                            launched, wouldn't sell, DISCOUNT DID NOTHING
                            objection was verifiability -> surface the source
                            60% / 85% accepted · the 15% = stale controls + no answer
B  Unified data API         not whose numbers are wrong, WHY they disagree
                            dashboard first · problem as subject · 100%
C  Cell prediction          flag before predict · show the uncertainty
F  Compliance platform      build vs buy · $7k/customer/yr
H  AWS us-east-1 Oct 2025   customer told us, not monitoring · 3 things erroring,
                            chased the confirmed one · multi-AZ bought us nothing
                            us-west-1 token (say it was luck) · then stop, and talk
I  2023 product call        no data -> count competitors, walk the building
                            crowded BECAUSE no expertise needed -> compliance
                            beat 1: killed the resume generator as a new hire
J  Learning by conversation a novice can't grade the tutor · consistency, premises,
                            published docs · find questions, never settle them

FEEDBACK  ____________________  <- still blank (write first)
SLOT 1    ____________________  <- replaces D: two audiences, same content
                                   (write second — Round 5 #6 has nothing without it)
SLOT 2    ____________________  <- replaces E: customer over internal goal,
                                   bad news you delivered before they found out
GAP 22-23 family, 18 months, one sentence, land forward
FAILURE   A's launch · H's detection
FINE-TUNE haven't; chose RAG for freshness + traceability. Say the reasoning.

Why this role: AI in production, where it breaks, in front of customers ·
diagnosis is my half · 10M convos/wk, support layer being built now
Rules: headline first · "I" not "we" · 2-3 min · then stop
```
