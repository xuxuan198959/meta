# Interview 2 — Critical Thinking & Analytical (+ live prompt demo)

## The official round description

> **Verbatim** from *Interview Prep Guide — Business Support Engineer, Meta
> Business Agent* (`../Interview Prep Guide — Business Support Engineer, Meta
> Business Agent .pdf`, pp. 2–4). Reproduced unedited so the guide and the prep
> material can be read together. **Don't edit this section** — everything below
> the divider is commentary on it.

### Interview 2: Critical Thinking & Analytical

**What to Expect**

This 45-minute interview explores how you approach problems, work through
ambiguity, and make decisions under pressure. Expect a mix of experience-based
discussion and a practical case study that digs into troubleshooting and
analytical thinking. **The interview concludes with a live, hands-on
prompt-engineering demonstration**, where you'll share your screen and use a
publicly available AI tool to solve a real-world business problem. This portion is
important—please review the dedicated preparation section below carefully.

**Focus Areas**

- Structured and logical approach to problem-solving
- Ability to break down complex problems into manageable parts
- Troubleshooting methodology and root-cause analysis
- Decision-making with limited information
- Experience integrating or championing AI tools in your work

**How to Prep**

- Prepare examples of times you solved difficult problems, especially ones
  involving ambiguity or incomplete information.
- Reflect on experiences where you adopted, integrated, or championed AI tools or
  workflows—be ready to discuss outcomes and challenges.
- Practice articulating your thought process step-by-step when working through
  unfamiliar scenarios.
- Think about how you prioritize, escalate, and collaborate when facing roadblocks.

**Live Prompt-Engineering Demonstration — Read Carefully**

The final portion of this interview is a **live demo**. You'll share your screen
and use a publicly available AI tool to craft effective prompts and work through a
real-world business problem in real time. You'll be asked to **export your
prompting session as a PDF and send it to your recruiter** afterward, so please
test exporting in advance.

**Technical setup — complete at least 24 hours before your interview:**

- **Open an Incognito / Private browsing window** so your responses aren't
  influenced by prior history. (Chrome/Edge: Ctrl/⌘ + Shift + N; Safari: ⌘ + Shift
  + N; Firefox: Ctrl/⌘ + Shift + P.)
- **Navigate to your preferred allowed AI tool** in that window, and make sure you
  are **not** logged into a personal profile.
- **Test exporting the conversation as a PDF.** Universal method: Ctrl/⌘ + P →
  change destination to "Save as PDF" → Save. (Most tools also have a share/export
  menu.)
- **Close unnecessary apps and programs** before you begin.
- **Confirm you know how to share your screen** on the video-call platform and have
  a stable internet connection.

**Allowed tools**

- **General-purpose chat LLMs:** ChatGPT, Gemini, Claude.ai, Meta.ai.
- **Prototyping / "vibe coding" tools** (if producing a visual prototype): Figma
  Make, Claude Code, v0, Lovable.

**Not allowed**

- Bespoke or custom skills, gems, or prompts built specifically for the interview.
- Tools not available to the general public (e.g., local or custom models).
- Dictation services (e.g., SuperWhisper, Willow Voice, Wispr Flow). If the
  interviewer believes tailored tools/skills are in use, you may be asked to switch
  tools.

**Tips to prepare**

- Treat it as an operational challenge: be structured, use real examples, and show
  critical thinking about AI's opportunities and risks in business contexts.
- Practice iterating on prompts—start broad, then refine to get specific,
  actionable outputs; be ready to adjust when a first answer misses the mark.
- Practice narrating your approach out loud as you prompt, so your reasoning is
  visible.
- Log into your chosen tool and run a full practice session (prompt → refine →
  export to PDF) before interview day.

**Privacy note:** You may hide your AI tool chat history before the interview if
you wish—the interview evaluates your live problem-solving, not prior history. If
you hit any technical issues during setup, contact your recruiter **before**
interview day.

### General Tips *(guide, p. 6 — applies to every round)*

- **Be yourself.** We want to understand how you think and work—there are no trick
  questions.
- **Ask clarifying questions.** It's encouraged and shows thoughtful engagement.
- **Use concrete examples.** Draw from real experiences whenever possible.
- **Prepare questions for your interviewers.** This is also your chance to learn
  about the team and role.

---

## Prep notes

Everything from here down is prep material built on the description above.

**Round 2** is **45 minutes**, in three parts.

| Part | Approx. time | Format |
|------|--------------|--------|
| Experience-based discussion | ~10 min | Behavioral — ambiguity, prioritization, escalation, AI adoption |
| Troubleshooting case study | ~15–20 min | Verbal analytical case, no tools |
| **Live prompt-engineering demo** | ~15–20 min | **Screen share, real AI tool, exported to PDF afterward** |

**Only one of those is confirmed.** The guide says the interview "concludes with"
the demo — so it's last — and describes the rest as "a mix of experience-based
discussion and a practical case study." The split above is a reasonable inference,
not a schedule. Two practical consequences: the experience questions may be woven
through rather than front-loaded, and **the demo could start earlier or later than
you expect**. Don't budget your best material for a segment that might get
compressed.

The demo is the part with no public precedent and the part the guide flags as
"important — please review the dedicated preparation section carefully." It also
has a hard prerequisite: **complete the technical setup at least 24 hours
before.** Do that first, before any content prep, because it's the only part that
can fail for reasons unrelated to your skill.

> **Source note:** Nobody has publicly reported this round — it's a new format.
> Everything below is built from Meta's own prep guide for this role (the tool
> list, the export requirement, and the evaluation focus areas are verbatim from
> it), plus the Business Agent product context. Treat the scenarios as rehearsal
> material, not predictions.

---

## Contents

- [**The official round description**](#the-official-round-description) — verbatim from the guide
- [Pre-flight checklist (24h before)](#pre-flight-checklist-24h-before)
  - [Allowed and not allowed](#allowed-and-not-allowed)
  - [Which tool to pick](#which-tool-to-pick)
- [What the demo is actually scoring](#what-the-demo-is-actually-scoring)
- [The narration framework](#the-narration-framework)
- [Two concepts to be able to define](#two-concepts-to-be-able-to-define) — prompt, prompt engineering
- [What your own experience gives you here](#what-your-own-experience-gives-you-here)
- [The prompt scaffold](#the-prompt-scaffold)
- [Rehearsal scenario 1 — Partner-facing troubleshooting guide](#rehearsal-scenario-1--partner-facing-troubleshooting-guide)
- [Rehearsal scenario 2 — Triage a backlog of support tickets](#rehearsal-scenario-2--triage-a-backlog-of-support-tickets)
- [Rehearsal scenario 3 — Write the agent's system prompt](#rehearsal-scenario-3--write-the-agents-system-prompt)
- [Rehearsal scenario 4 — A business problem with no code in it](#rehearsal-scenario-4--a-business-problem-with-no-code-in-it)
- [Recovering when the model gives you a bad answer](#recovering-when-the-model-gives-you-a-bad-answer)
- [The troubleshooting case study](#the-troubleshooting-case-study)
  - [Where your own experience belongs in a hypothetical case](#where-your-own-experience-belongs-in-a-hypothetical-case)
- [The experience questions](#the-experience-questions) — five drafted answers

---

## Pre-flight checklist (24h before)

Straight from the guide. Do all of it, in one sitting, at least a day ahead.

- [ ] Open an **Incognito / Private window** (Chrome/Edge `⌘⇧N`, Safari `⌘⇧N`,
      Firefox `⌘⇧P`) so prior history can't influence responses.
- [ ] Navigate to your chosen tool in that window and confirm you are **not
      logged into a personal profile**.
- [ ] **Run a full practice session end to end**: prompt → refine → refine again
      → export.
- [ ] **Test the PDF export.** Universal method: `⌘P` → destination
      "Save as PDF" → Save. Most tools also have a share/export menu. Verify the
      PDF actually contains the full conversation and is readable — long chats
      sometimes clip.
- [ ] Confirm **screen sharing** works on the video platform, and know how to
      share a single window vs. the whole screen.
- [ ] **Close everything else.** Notifications, Slack, email, personal tabs. You
      are sharing your screen and the recruiter receives the transcript.
- [ ] Check internet stability; have a phone hotspot as backup.
- [ ] Know where the PDF will save to, so you're not hunting for it live.

If anything fails, contact the recruiter **before** interview day — the guide
says so explicitly, and flagging it early is neutral-to-positive.

> **Privacy note from the guide:** you may hide your AI tool chat history
> beforehand if you want. The round evaluates live problem-solving, not history.
> Using a fresh incognito session handles this anyway.

### Allowed and not allowed

**Allowed**
- General-purpose chat LLMs: **ChatGPT, Gemini, Claude.ai, Meta.ai**
- Prototyping / "vibe coding" tools, *if you're producing a visual prototype*:
  **Figma Make, Claude Code, v0, Lovable**

**Not allowed**
- Bespoke or custom skills, gems, projects, or prompts built for the interview
- Tools not available to the general public (local or custom models)
- Dictation services (SuperWhisper, Willow Voice, Wispr Flow)

If the interviewer suspects tailored tooling, you may be asked to switch tools —
another reason to work from a clean incognito session with nothing configured.

### Which tool to pick

Default to a **general-purpose chat LLM**, not a prototyping tool, unless the
prompt explicitly calls for a visual artifact. Reasons: the round is about
*prompting*, the chat transcript is the deliverable, and PDF export from a chat
UI is trivial while exporting from a prototyping tool is not.

**Meta.ai is worth a thought.** It's on the allowed list, it's Meta's own product
built on Llama, and the JD explicitly mentions building on Llama. Using it shows
product familiarity. But only pick it if you've actually rehearsed on it — do not
discover its quirks live. If your rehearsals go better on another allowed tool,
use that; nobody is scoring brand loyalty, and fumbling an unfamiliar UI on a
shared screen costs more than the goodwill is worth.

Whatever you choose, rehearse all four scenarios below on **that** tool.

---

## What the demo is actually scoring

Read the focus areas: structured problem-solving, breaking down complex problems,
troubleshooting methodology, decision-making with limited information. Note what
is *not* there: knowing prompt-engineering jargon.

The guide's own framing is the one to hold in your head: **"treat it as an
operational challenge."** Not a writing exercise, not a demo of clever phrasing —
an operational problem that happens to be solved with a model. Everything below
follows from that.

So:

- **The first prompt is not supposed to be perfect.** The guide says to "start
  broad, then refine" and to "be ready to adjust when a first answer misses the
  mark." An interviewer who sees one prompt produce one great answer learns
  nothing about you. **Plan to iterate at least three times.**
- **Your reasoning has to be audible.** They can see the screen but not your
  head. Silence while typing is the most common way to lose this round.
- **Critique the output.** Reading a model's answer and saying "this is 80% there
  but it invented a metric we don't have, and it's too long for a partner email"
  is the single highest-signal thing you can do. It shows you don't take model
  output at face value — which is precisely the "AI-native but critical" posture
  the JD describes.
- **Land on something usable.** Finish with a concrete artifact: a runbook, a
  triage rubric, a system prompt, a partner-facing email. Not a wall of text.
- **Manage the clock.** Aim for 4–6 exchanges in ~15 minutes. Don't over-refine
  one section while the overall deliverable is incomplete.

---

## The narration framework

Four beats per iteration. Say them out loud; they're short.

1. **Intent** — "I'm going to start deliberately broad, just to see how the model
   frames the problem, because I don't want to anchor it to my assumptions yet."
2. **Prompt** — type it. Read the key parts aloud as you go, or after.
3. **Critique** — "Okay. It got the structure right, but three problems: it's
   assuming we have data we don't, the tone is too formal for this audience, and
   it's missing the escalation path entirely."
4. **Refine** — "So I'll add the constraints it's missing and ask it to keep the
   structure it already produced."

Phrases worth having ready:

- "Let me state the goal before I prompt, so you can see what I'm optimizing for."
- "I'm giving it a role and an audience first — those two change the output more
  than anything else."
- "I deliberately didn't give it a format yet. I want to see what it thinks is
  natural before I constrain it."
- "That's a hallucination — it cited a metric we never defined. I'll constrain it
  to only use the fields I listed."
- "This is good enough to iterate on rather than restart. I'll keep the skeleton
  and fix the two specific problems."
- "In a real workflow I'd validate this against the actual data before sending it
  to a partner — the model's confidence here isn't evidence."

That last one matters. Showing you know where AI output needs human verification
is a hiring signal for a support role, not a hedge.

---

## Two concepts to be able to define

This round is a prompting demo and Round 3's prep list names "the building blocks
of a good system prompt" outright. There's a real chance someone asks you to
define the terms — and even if nobody does, stating a definition before you start
prompting is a strong way to frame the demo. Have both ready in a sentence or two.

**A prompt** is, in the everyday sense, the text you give a model. The more useful
definition, and the one to say out loud:

> A prompt is the *entire input sequence* the model sees on a single call.

A model is stateless. No memory between calls, no clock, no database. Everything
it can use comes from two places: its weights, and the tokens you hand it right
now. In a production system those tokens are assembled from several sources:

```text
system prompt      role, rules, output contract, guardrails
conversation       prior turns, replayed in full every call
retrieved context  RAG chunks pulled for this query
tool definitions   what functions exist, and their schemas
tool results       what came back from calling them
user message       what the customer just typed
```

That assembly *is* the prompt — internally there's no boundary between the parts.

**Why this framing earns you something:** it explains the entire Round 3 failure
list in one move. The agent gets "is the sale still on?" wrong because nothing in
the sequence states today's date. It quotes a policy that changed last month
because the retrieval index still holds the old chunk. It drops a constraint from
twelve turns ago because that text is now buried in a long context. It
hallucinates because there's a gap and the weights fill it with something
plausible. **A model doesn't know what it wasn't told** — say that sentence and
most of the diagnostic follow-ups answer themselves.

**Prompt engineering** is designing that input so the output is *reliable*, not
just good once. "Reliable" is the load-bearing word: anyone gets a good answer on
the third try; the job is an acceptable answer on the first try, across millions
of merchants, including the strange ones. Five activities:

1. **Specification** — role, task, audience, output contract. Most bad output is
   an underspecified request, not a weak model.
2. **Context engineering** — deciding which facts go in the window and which stay
   out. Now the harder half, which is why it has its own name.
3. **Guardrails** — what to do when information is missing. *"If the context
   doesn't contain the answer, say so and offer a human"* is the highest-value
   sentence in most production prompts.
4. **Demonstration** — a couple of worked examples when the format is unusual.
5. **Evaluation and iteration** — testing against real and adversarial cases. The
   part people skip, and the part that separates a practitioner from an enthusiast.

Those five are exactly the [six-block scaffold](#the-prompt-scaffold) below,
arranged as a template. The guide names the same six.

**What prompt engineering mostly isn't, anymore.** Magic phrasing. "You are a
world-class expert," "take a deep breath," offering the model a tip — real effects
on 2023-era models, largely dead weight now. Saying any of it live will date you.
What has *not* stopped mattering: supplying information the model can't have,
stating the output contract explicitly, and defining failure behavior.

**The follow-up worth having ready — prompt vs. RAG vs. fine-tuning.** Prompting
changes behavior; RAG supplies knowledge; fine-tuning changes the model's
defaults. Reach for them in that order: prompting is free and instant, RAG solves
"it doesn't know our data," and fine-tuning is for when you need consistent style
or format at scale and have the examples to teach it. You have unusual standing
to answer this one — you designed a full RAG path at Kaamel and can say why you
chose retrieval over fine-tuning for a corpus of policy documents that changes.

---

## What your own experience gives you here

Most candidates in this round are demonstrating prompting they've done in a chat
window. You've shipped a retrieval pipeline into production and watched customers
reject 15% of its output. That's a different category of credential, and it's
worth three or four deliberate moments in the round rather than one.

Where to spend them — each is one sentence, dropped mid-demo, then keep moving:

| When you're… | Say something like |
|---|---|
| Adding the GUARDRAIL block | "This is the block I care most about. On the compliance assistant I built, abstention when retrieval came back weak mattered more than answer quality — a blank is recoverable, a confident wrong answer to an auditor isn't." |
| Asked how you'd know it works | "I'd want an accept/edit/reject rate, not a self-assessment. On my questionnaire assistant that was the customer's own click in the review queue — 85% accepted." |
| The model invents a fact | "The fix that actually worked for us wasn't a better prompt — it was linking every answer back to the source record, so a reviewer could check it in two seconds. Customers didn't trust the first version because they couldn't see what it was based on." |
| Talking about human review | "I'd make review mandatory rather than a setting, wherever the output is irreversible." |
| Asked about limits | "Two different things get called 'wrong.' Ours split into controls that had *changed* — a freshness problem — and questions where no documented answer existed at all, which is an abstention problem. Different fixes." |

Two cautions. **Don't narrate your résumé** — one sentence, then back to the
screen; this is a demo round, not a behavioral round. And **keep the numbers
honest**: 60% and 85% are the two you have, they're good, and inflating them
invites a follow-up you can't survive. See the
[story bank](<./Story Bank - Rounds 4 & 5.md#a-questionnaire-assistant--the-ai-story>)
for what still needs verifying.

---

## The prompt scaffold

Use the **same six blocks** as the system-prompt anatomy in
[Interview 3 — Domain Expertise (GenAI)](<./Interview 3 - Domain Expertise (GenAI).md#system-prompt-anatomy>).
Reusing one structure across both rounds reads as method rather than improvisation.

```text
ROLE:         Who the model should be, and whose interests it serves
CONTEXT:      The facts it's allowed to use — and a statement that it may
              not use anything else
INSTRUCTIONS: The task, decomposed, in priority order
EXAMPLES:     One or two, if format matters
OUTPUT:       Format, length, audience reading level
GUARDRAILS:   What to do when information is missing; what never to assert
```

You don't have to type all six in the first prompt — in fact you shouldn't. Start
with ROLE + INSTRUCTIONS, then add blocks as the output reveals what's missing.
Narrating *which block you're adding and why* is the whole performance:

> "The output invented three statistics. That tells me my CONTEXT block was too
> thin and there was no GUARDRAIL about unknowns. I'll add both."

---

## Rehearsal scenario 1 — Partner-facing troubleshooting guide

*Likely prompt shape: "A business partner integrating the Business Agent keeps
reporting that their agent gives wrong order statuses. Use the AI tool to produce
something that helps them."*

This is the most on-the-nose scenario for the role. Rehearse it first.

**Iteration 1 — broad, to see the model's framing.**

```text
I support businesses integrating an AI customer-service agent into their
messaging channels. A partner reports the agent sometimes gives customers
incorrect order status. Before we write anything: what are the most likely
causes, organized by system layer?
```

*Narrate:* "I'm not asking for the deliverable yet. I want a cause list first, so
the guide I write is structured around real failure modes rather than my guesses."

**Iteration 2 — constrain to what we actually know.**

The model will produce a broad list, probably including causes that don't apply.
Say so, then narrow:

```text
Good list, but narrow it. Constraints:
- The partner's own order API is the source of truth; we call it per request.
- We do not cache order data.
- The agent has retrieval over their FAQ/policy docs, not over order data.
Re-rank the causes given those constraints, and drop the ones that are now
impossible. For each remaining cause, give the one log field or check that
would confirm it.
```

*Narrate:* "This is the important move — I'm eliminating whole branches with
facts. And I'm asking for discriminating evidence per cause, because a cause list
without a way to test it isn't actionable for the partner."

**Iteration 3 — turn it into the artifact.**

```text
Now write this as a self-serve troubleshooting guide for the partner's engineer.

AUDIENCE: a backend engineer at a mid-size retailer, not an AI specialist.
FORMAT: a numbered decision tree. Each step is one check, its expected result,
and where to go next. Max one page.
GUARDRAIL: only reference checks the partner can run on their own systems —
they have no access to our internal logs. If a step requires our logs, say
"contact support with your conversation ID" instead.
```

*Narrate:* "The audience and the access constraint are the two things that make
this usable. A guide that tells a partner to check logs they can't see is worse
than no guide."

**Iteration 4 — pressure-test it.**

```text
Review your own guide as if you were that partner engineer. Where would you
get stuck, and what's ambiguous? Then give me the revised version.
```

*Narrate:* "Self-critique prompting catches a lot. It's cheaper than me reading
it three times, and it usually finds the ambiguous step I'd have missed."

**Close** by reading the final artifact aloud and stating what you'd do before
actually sending it: verify the log field names are real, have one partner-facing
teammate read it for tone, and add the support contact path.

---

## Rehearsal scenario 2 — Triage a backlog of support tickets

*Likely prompt shape: "Here are 40 partner support tickets from this week. Figure
out what's going on and tell us what to prioritize."*

Tests analytical structure more than wordcraft.

**Iteration 1 — get a taxonomy, not a summary.**

```text
I'm going to paste a batch of support tickets from businesses using our AI
customer-service agent. First task: propose a categorization scheme that would
let me spot systemic issues, before you look at the content. What dimensions
should I classify each ticket on?
```

*Narrate:* "I want the axes before the analysis. If I let it summarize first
it'll give me a narrative, and narratives hide distribution."

Expect it to propose something like: failure mode, affected component, severity,
merchant segment, channel, first-seen date. Push it to include **"is this a
product defect or a policy/expectation issue"** — that's the Transcript 6
distinction from Round 3, and it's the one axis that stops you from over-counting
bugs.

**Iteration 2 — classify, with an explicit unknown bucket.**

```text
[paste tickets]

Classify each ticket on those dimensions. Output a table, one row per ticket.

GUARDRAILS:
- If a ticket doesn't contain enough information to classify a dimension, put
  "UNKNOWN" — do not infer.
- Do not merge tickets that merely sound similar; only group them if they
  describe the same observable symptom.
```

*Narrate:* "The UNKNOWN rule matters. Left alone the model will confidently
classify everything, and I'll end up with clean-looking data that's partly
fabricated."

**Iteration 3 — from counts to a recommendation.**

```text
Now aggregate: which categories have the highest volume, and which have the
highest severity? Then recommend a priority order for engineering.

Weight by: number of merchants affected (not number of tickets — one loud
merchant filing ten tickets is one merchant), whether there's a workaround,
and whether the trend is growing.

For each recommendation state your confidence and what additional data would
raise it.
```

*Narrate:* "Tickets-per-merchant is the trap here — the loudest partner isn't the
biggest problem. And I'm asking for confidence plus missing data because I'd be
taking this into a prioritization meeting, and I need to be honest about which
parts are solid."

**Close** by naming what you'd verify independently: pull actual error rates for
the top two categories to confirm the ticket volume matches the telemetry. If
tickets say one thing and metrics say another, the gap is itself the finding.

---

## Rehearsal scenario 3 — Write the agent's system prompt

*Likely prompt shape: "A small business is onboarding onto the agent. Use the AI
tool to draft the agent's instructions."*

Highest overlap with Round 3 — you can reuse the worked example from the
[system prompt anatomy](<./Interview 3 - Domain Expertise (GenAI).md#system-prompt-anatomy>)
section as your mental template. Don't paste it from memory verbatim; build it
live so the reasoning is visible.

**Iteration 1 — deliberately underspecified, to expose gaps.**

```text
Write a system prompt for an AI assistant that handles customer messages for a
small florist on WhatsApp.
```

*Narrate:* "I'm starting thin on purpose. The gaps in this output tell me what a
real onboarding checklist needs to collect from the merchant."

**Iteration 2 — critique it out loud, then fix.**

Whatever it produces will almost certainly miss: injecting the current date, the
behavior when a tool call fails, the abstention rule for missing information,
channel formatting (markdown renders as literal asterisks in WhatsApp), and the
handoff trigger. Name those gaps aloud — that critique *is* the interview — then:

```text
That's a good skeleton but it's missing the failure paths. Revise using this
structure: ROLE / CONTEXT / INSTRUCTIONS / EXAMPLES / OUTPUT FORMAT / GUARDRAILS.

Requirements:
- Inject today's date as a variable; the model has no clock and will otherwise
  get "is the sale still on" wrong.
- Answer only from provided context. If the context lacks the answer, say so and
  offer a human — never fill the gap.
- Any claim about a specific order, price, or stock level requires a tool call.
  If the tool fails, say so; never guess the result.
- Plain text only, no markdown — this renders in WhatsApp.
- Label the few-shot examples explicitly as examples so they aren't mistaken
  for facts about this business.
```

*Narrate the date and the markdown points specifically.* They're small, concrete,
and unmistakably from someone who has shipped this kind of thing.

**Iteration 3 — red-team it.**

```text
Act as an adversarial customer. Give me five messages that would make this
prompt produce a wrong, unsafe, or off-brand response. For each, say which
instruction failed to prevent it.
```

*Narrate:* "This is where I'd spend real time on a live merchant. Writing the
prompt is easy; finding where it breaks is the work."

Then close by patching the top two holes it finds.

---

## Rehearsal scenario 4 — a business problem with no code in it

*Likely prompt shape: "Merchants in a new market are churning off the agent in
their first month. Use the AI tool to figure out what to do about it."* Or:
summarize a quarter of partner feedback for a leadership review; draft the
onboarding email sequence for a new merchant segment; build a one-page brief on
why a launch slipped.

**Rehearse this one too, even though it feels off-theme.** The guide's phrase is
"a real-world **business** problem," not a technical one. Scenarios 1–3 are all
support-engineering shaped, and if the prompt turns out to be a go-to-market or
comms problem, having only technical rehearsals is how you end up improvising the
format you're being scored on. It's also the cheapest scenario to prepare —
15 minutes on your chosen tool.

The method doesn't change, which is the point worth demonstrating:

**Iteration 1 — refuse to answer the question yet.**

```text
I support businesses using an AI customer-service agent. Merchants in a new
market are churning in their first month. Before proposing anything: what are
the plausible causes, and what data would distinguish between them?
```

*Narrate:* "Same move as a technical case — causes and discriminating evidence
before recommendations. A list of fixes for an undiagnosed problem is guesswork
with formatting."

**Iteration 2 — force it to separate what it knows from what it's assuming.**

```text
Split that into: (a) things we could verify with data we plausibly already have,
(b) things needing new instrumentation, (c) things only a merchant conversation
would answer. Mark any claim you're inferring rather than deriving.
```

*Narrate:* "This is the same UNKNOWN discipline as the ticket triage. Business
analysis is where models are most fluent and least grounded, so I want the
inference boundary drawn explicitly."

**Iteration 3 — the artifact, with an audience.**

```text
Write this as a one-page brief for a product lead who has 3 minutes.
Lead with the recommendation, then the reasoning, then what would change my mind.
State confidence on each claim. No filler.
```

*Narrate:* "'What would change my mind' is the section I'd actually be judged on
internally — it's what makes a recommendation reviewable instead of a pitch."

**Close** on the same note as the others: what you'd verify before this went to
anyone. Here it's whether the churn is real or a measurement artifact — the same
real-change-vs-measurement-change distinction as
[Practice case B](#the-troubleshooting-case-study) below.

---

## Recovering when the model gives you a bad answer

The guide says explicitly to "be ready to adjust when a first answer misses the
mark." There's a reasonable chance the interviewer *hopes* you get a bad answer,
because recovery is more informative than success. Have a diagnosis reflex:

| What's wrong with the output | Root cause | The fix, named out loud |
|---|---|---|
| Invented facts, figures, or fields | CONTEXT too thin, no guardrail on unknowns | Add explicit context and "if you don't know, say UNKNOWN" |
| Generic, could-be-any-company | No ROLE, no audience | Add role + audience + one concrete detail |
| Right content, wrong shape | No OUTPUT block | Specify format, length, and structure |
| Too long | No length constraint, and you asked an open question | Constrain length *and* narrow the ask |
| Ignored part of your instruction | Too many instructions in one prompt | Split into two prompts, or number and prioritize them |
| Confidently wrong reasoning | Asked for a conclusion without steps | Ask it to lay out the reasoning first, then conclude |
| Drifted from earlier constraints | Long conversation, constraints fell out of attention | Restate the constraints; don't assume the thread remembers |

Two meta-moves worth having:

- **Don't restart from scratch when 70% is good.** Say "I'll keep this skeleton
  and fix two things" — that's what an experienced practitioner does, and
  restarting reads as not knowing how to steer.
- **Do restart when the framing is wrong.** If the model misunderstood the goal,
  patching makes it worse. Say "the framing is off, I'm going to restate the
  problem from the top rather than patch this" — deciding *which* situation
  you're in, and saying why, is the skill.

---

## The troubleshooting case study

The middle chunk of the round: a verbal analytical case, no tools. Expect
something like *"A partner says their customers are complaining that the agent
stopped responding. What do you do?"*

Use the same five-step structure as the
[RCA framework](<./Interview 3 - Domain Expertise (GenAI).md#the-rca-framework-use-this-live>)
in Round 3 — consistency across rounds is deliberate — but lead with scoping,
because in an operational case the first question is always *how bad is it*.

**The opening move, always:**

1. **Scope the blast radius.** One merchant or many? One channel or all? When did
   it start, and does it correlate with a deploy or a dependency change? What's
   the customer impact right now?
2. **Establish severity and communicate.** Before deep investigation: is this a
   sev that needs a status update to partners? Support engineering is judged on
   communication during an outage as much as on the fix.
3. **Then** diagnose: characterize → hypothesize across layers → name the
   discriminating evidence → remediate in three horizons.
4. **Close the loop.** Post-incident: what monitoring would have caught this
   sooner, and what's the follow-up action item?

**Practice case A — degraded partner integration.**
*"A large retail partner reports that since yesterday, roughly 1 in 5 of their
customers get 'I can't check that right now' instead of order status."*

Work it: 20% is a suspiciously round partial failure — think one bad host in a
pool, one region, a canary at 20%, or a rate limit being hit at peak. Check
whether the failures cluster by time of day (rate limiting) or are uniformly
distributed (bad instance). Ask whether the partner deployed anything, because
their API is the dependency and "our agent broke" is frequently "their endpoint
started returning 429s." The remediation split: immediate is a graceful message
plus handoff, short-term is backoff and circuit-breaking so we degrade cleanly,
long-term is capacity/quota negotiation with the partner and an alert on
per-partner error rate.

**Practice case B — a spike with no obvious cause.**
*"Handoff rate across all merchants jumped from 12% to 30% overnight. Nothing
was deployed."*

Work it: "nothing was deployed" is a claim to verify, not a fact — prompt
versions, model versions, index rebuilds, and config changes all ship outside the
main deploy pipeline, and that's exactly the attribution problem. Check whether
the spike is uniform across merchants (points to a shared component: model,
prompt template, retrieval index) or concentrated (points to a merchant cohort or
a region). Check whether it's a real behavior change or a *measurement* change —
someone modifying the handoff trigger logic or the metric definition produces an
identical-looking graph. Then check the handoff *reason* breakdown; if
"low confidence" tripled, suspect retrieval or a model change, and if "customer
requested" tripled, something upstream is annoying people.

That last distinction — real change vs. measurement change — is worth raising
unprompted in any metrics case. It's the mistake people actually make.

### Where your own experience belongs in a hypothetical case

**The case study is not an experience question.** They hand you a scenario you've
never seen and watch you think. Don't answer it with a story — "that reminds me of
something at Kaamel" is a way of avoiding the case.

But there are three or four places where one clause of real experience makes a
generic move land harder. Use them sparingly, mid-sentence, then keep working:

| Move in the case | The clause that upgrades it |
|---|---|
| "I'd check whether their endpoint started erroring" | "…their API is the source of truth and I've had 'our thing is broken' turn out to be the partner's endpoint returning 429s" |
| "I'd want per-partner error rates, not a global one" | "…global metrics hide a single tenant being completely down — I built the discrepancy dashboards at Meta for exactly that blind spot" |
| "Is this a real change or a measurement change?" | "…I've watched a metric 'move' because someone changed the definition upstream" |
| "I'd tell the partner before they tell us" | "…I've had the conversation where I told a customer our pipeline couldn't guarantee fidelity on certain documents. Better from me than from their auditor." |

The rule: **the case is the subject, the experience is an adjective.** One clause,
never a paragraph.

---

## The experience questions

Roughly the first 10 minutes, though they may be woven through instead. The
guide's four prep bullets map one-to-one onto four questions, and each maps onto a
story on the résumé. Longer versions live in the
[story bank](<./Story Bank - Rounds 4 & 5.md>); these are the round-2 cuts, which
are **shorter and more method-forward** than the Round 4 versions — this
interviewer is scoring how you think, not who you are.

> **On the drafted answers below.** They're written out so you can hear the shape
> and the closing lines, not so you can memorize them. Say each one aloud twice,
> then throw away the wording and keep the structure. A recited answer is audible
> and it kills the follow-up conversation, which is where the round is actually
> scored. Everything marked **[VERIFY]** needs checking against what really
> happened; everything marked **[FILL]** is yours to supply.

### 1. "A difficult problem you solved under ambiguity or incomplete information"

**Story E — the SOC 2 evidence pipeline.** The cleanest ambiguity story on the
résumé, because the *requirement itself* was undefined. "Auditor-ready" isn't a
spec, and nobody could say in advance which documents OCR would survive.

> "The clearest one is a document pipeline I built last year. Our customers were
> going through SOC 2 audits, and their evidence — policies, approval records,
> screenshots — existed only in Chinese. The auditors read English. The workaround
> was someone translating page by page, which was slow and, worse, inconsistent
> between whoever happened to do it.
>
> The hard part wasn't the technology, it was that the requirement was undefined.
> 'Auditor-ready' isn't a specification. Nobody could tell me how faithful was
> faithful enough, and nobody could tell me which documents would survive OCR —
> Chinese business documents come with red seals stamped across the text,
> handwritten sign-offs, and tables that don't survive naive extraction.
>
> So instead of trying to settle the requirement in the abstract, I made the
> unknown measurable. I ran a sample of real evidence through and sorted the
> output by how badly it degraded. That gave me document *classes* rather than one
> quality number. Clean digital documents went straight through. Anything with
> stamps, handwriting, or complex tables got routed to a human instead of being
> silently degraded. **[VERIFY the split.]**
>
> It replaced the manual workflow entirely **[FILL: hours per audit, or pages]**.
> But the part I'd actually point to is the principle: with a document pipeline,
> the win isn't accuracy on the average page. It's knowing which pages you're
> going to be wrong on *before* you're wrong on them. One reformatted document an
> auditor rejects costs more than ten pages of honest 'a person should check this.'"

**Why this closes well:** that last line is also the correct posture toward an AI
agent in production, and the interviewer will hear it without you saying so. Don't
explain the parallel — let them make it.

*Alternative if they want something older or more hardware-flavored:* Story G, the
Marvell bring-up, where the ambiguity was which layer owned the bug.

### 2. "A time you adopted, integrated, or championed AI tools"

The highest-stakes answer in the round — the guide names it here *and* in Round 4,
and the JD has an "AI native" bullet. Three mentions.

**Note that this question has two readings and you have strong material for both.**
*AI in the product* (the questionnaire assistant) and *AI in your own daily
workflow* (Claude, Cursor, MCP). Listen for which one they want; if it's ambiguous,
ask — *"do you mean AI in what I've built, or AI in how I work?"* is a good
clarifying question and the guide explicitly rewards asking.

#### 2a. AI in the product — the questionnaire assistant

Weight this toward **judgment over outcome**. The 60% and 85% are the setup. The
arc — a v1 customers rejected, and *why* — is the answer.

> "The main one is an AI questionnaire assistant I designed and built at Kaamel.
> Our enterprise customers get security questionnaires from *their* customers —
> hundreds of questions about controls, data handling, incident response — and
> answering one meant a security lead spending days digging through policy
> documents scattered across the company.
>
> I designed the whole retrieval path: ingestion, chunking, embeddings, the vector
> index, semantic retrieval, generation. We shipped a first version in mid-2024 on
> the OpenAI API, and customers didn't trust it. They said the quality was low —
> models were weaker then — but when I dug into it, quality wasn't really the
> problem. **The problem was that they couldn't see where an answer came from.**
> These answers go to their auditors. An unverifiable claim on a compliance
> document is legal exposure, so their reaction was completely rational: they'd
> rather pay a lawyer than use our tool.
>
> So the fix wasn't a better model. I built the traceability layer — every answer
> links back to the source record it was derived from, and the derivation is
> explained. Then review became mandatory rather than a setting, and the system
> abstains when retrieval comes back weak instead of filling the gap.
>
> That's what turned it around. Effort dropped about 60%, and 85% of answers were
> accepted as-is — measured by the customer's own accept, edit, or reject click in
> the review queue, not by us grading ourselves.
>
> The 15% is the part I find more interesting. It's two different problems wearing
> the same costume. Some were controls the company had *changed* — the answer was
> right last quarter and our index hadn't caught up. The rest were questions where
> no documented answer existed anywhere, so there was nothing to retrieve and the
> only correct behavior was to say so. One's a freshness bug, one's an abstention
> rule. A single accuracy number hides both."

**The line to make sure you say**, because it generalizes past this story and it's
the most quotable thing you have:

> "When someone doesn't trust an AI output, the fix is usually to make it
> checkable — not to make it better."

*On championing:* customer adoption came from traceability plus commercial pull —
discounted pricing, and free access for business partners in exchange for feedback
that fed the next iteration. **[FILL: anyone *internally* who distrusted it, and
what convinced them? That's the missing half of "championed."]**

#### 2b. AI in your own workflow

Don't undersell this — it's specific and it maps onto a JD preferred qualification
almost word for word (*"prompt/context engineering, agent orchestration"*).

> "ChatGPT, Claude, and Cursor, across design, planning, and coding — Claude most
> heavily, to the point where I regularly hit my daily limits.
>
> The way I actually use it: when I'm driving a new initiative — the questionnaire
> assistant is the example — I give it the requirement from the CEO or PM and have
> it break the product down into components. Then I go component by component and
> work through feasible solutions with it. What matters is that I treat the output
> as a draft, not an answer. I review it, confirm it with a proof of concept, and
> push back when it's wrong — which it is, regularly.
>
> The thing I've learned that changed my results most: **as a conversation gets
> long, the model loses earlier context, and the quality degrades without telling
> you.** So I manage context deliberately now rather than letting a thread sprawl.
> That's had more effect on output quality than any prompt wording.
>
> Beyond the chat interface I use Skills and MCP servers to extend what it can
> reach."

**Why this lands:** almost everyone says "I use Copilot and it saves time." Naming
context degradation as a failure mode you've adapted to — and having a practice
around it — is the difference between using a tool and understanding one.

*One caution:* if you cite trying the latest models as how you stay current, make
sure the model you name is actually current. Naming a version that's a generation
old undercuts the exact claim it's supporting.

*Near-certain follow-up — "where should we **not** use AI in a support workflow?"*

> "Anywhere a confident wrong answer is both asymmetric and irreversible. Refunds,
> policy commitments, anything legal or safety-related. The test I use is: if this
> is wrong, can we take it back? If not, the model drafts and a person sends. It's
> the same call I made on the compliance answers — which is why review there isn't
> a setting you can switch off."

Same reasoning as the abstention rule in
[Interview 3](<./Interview 3 - Domain Expertise (GenAI).md>) — and you've made that
exact call in production, which very few candidates can say.

### 3. "How you prioritize, escalate, and collaborate when blocked"

They want a **heuristic you actually use**, not "I use judgment." Lead with the
rule, then show it working.

> "My rule is that I escalate on blast radius and on new information — not on
> frustration. If the impact is spreading, or if I've learned something the owning
> team doesn't know yet, interrupting them is cheap compared to the cost of being
> wrong. If the only thing that's true is that I'm stuck, that isn't an escalation.
> That's me still working the problem.
>
> For prioritizing, it's customer impact times reversibility. An irreversible
> wrong action affecting one customer can outrank a cosmetic issue affecting a
> thousand.
>
> The example I'd give is from Meta. Several teams had each built their own path to
> the same underlying network data, and the numbers disagreed with each other. My
> first instinct was to escalate — get a decision from above about which one was
> right. I didn't, because I realized nobody had the information to make that
> decision yet, including me. So I built a dashboard comparing every existing path
> against a unified one, per dataset, per metric, live. That turned 'your numbers
> are wrong' into something people could point at together. The discrepancies got
> fixed instead of argued about, and we got the unified API to 100% of users.
> **[VERIFY: was the dashboard genuinely before the migration, or alongside it?]**
>
> What I took from that: the alternative to escalating isn't always doing it
> yourself. Sometimes it's building the thing that makes the decision obvious."

**[FILL — if you have a real escalation, a time you *did* interrupt someone and
why, lead with that instead.** It's a stronger answer here, and it doubles as the
production-incident story Round 4 needs. The dashboard story is excellent but it's
about *avoiding* escalation, so a sharp interviewer may push for the other case.]

### 4. "Working through an unfamiliar scenario step by step"

Less a story than a demonstration — they may simply hand you the case study here.
What's scored is **sequencing, and why that order**.

> "I'd give you my sequence and then an example of it.
>
> Scope before depth — how many are affected, since when, and what changed around
> that time. Then the cheapest discriminating check first: not the one nearest my
> hunch, but the one that eliminates the most possibilities for the least effort.
> Then separate what *changed* from what's always been true, because most incidents
> are a delta and finding the delta is faster than reasoning about the whole
> system. And I treat claims in the report as hypotheses — 'nothing was deployed'
> is something to verify, not a fact.
>
> Where I learned that was silicon bring-up at Marvell. A failure could be in the
> RTL, the board, the firmware, or in the test itself — and hardware and software
> each had a default assumption that it belonged to the other team. Arguing about
> ownership was slow and it didn't converge. What worked was finding the one
> observation that split the space. **[FILL: the specific check — swapping boards,
> running the same test on a known-good part, isolating with a scope.]** Once you
> can say 'this reproduces on two boards, so it isn't the board,' the conversation
> stops being about whose fault it is and starts being about the next check.
>
> That's the same shape as an agent giving a customer a wrong answer. It could be
> our stack or it could be the merchant's configuration, and the useful first move
> is whichever check tells you which one you're in."

**Why this is the strongest of the four for this round:** it's the only answer that
demonstrates the skill rather than describing it, and the closing sentence lands
you inside the job's actual daily question. If you only polish one, polish this.

### 5. Likely fifth question — "the hardest thing you've debugged"

Not in the guide's bullets, but this is a troubleshooting-focused round and it's a
natural ask. Don't reuse Marvell if you've already spent it on question 4.

**Strongest answer: the AWS us-east-1 outage**, October 2025 — Story H in the
[story bank](<./Story Bank - Rounds 4 & 5.md#h-the-aws-us-east-1-outage--the-incident-story>),
where the full method is written out. It's recent, it's a distributed-systems
failure, and the JD's first responsibility line is *"independently managing complex
outages."* Two beats to hit: **existing EC2 instances kept running while new
launches failed** — so the reflexive restart was the worst available move — and
**multi-AZ doesn't protect you from a regional control-plane failure.**

If they want something AI-flavoured instead, the better answer is a **retrieval bug
in the questionnaire assistant**: nothing errors, no stack trace, the answer is
simply wrong. Debugging a system that fails *softly* is a distinct skill and it's
the one this role actually needs. **[FILL: a specific instance.]**

The through-line to name whichever you pick: **the hardest bugs aren't the ones
that crash — they're the ones that return a plausible answer.**

### Delivery note for this segment

Answers here should run **90 seconds to two minutes** — shorter than the Round 4
versions of the same stories. Lead with the method, use the story as evidence,
then stop and let them probe. The interviewer is warming up toward the case study
and the demo; a five-minute narrative here eats the part of the round you're
actually being hired on.

Three habits for this segment specifically:

- **Say "I," not "we."** Every drafted answer above does. It's the single most
  common way strong candidates undersell themselves.
- **Give the number, then move on.** 60%, 85%, 100% of users, ~$7,000 per
  customer. State it once, flatly, without building up to it.
- **End on the principle, not the outcome.** Each draft above closes on what the
  experience taught rather than what it produced. That's what makes a story reusable
  by the interviewer when they write up their notes.
