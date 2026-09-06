# Interview 5 — Cross-Functional

## The official round description

> **Verbatim** from *Interview Prep Guide — Business Support Engineer, Meta
> Business Agent* (`../Interview Prep Guide — Business Support Engineer, Meta
> Business Agent .pdf`, p. 6). Reproduced unedited so the guide and the prep
> material can be read together. **Don't edit this section** — everything below
> the divider is commentary on it.

### Interview 5: Cross-Functional

**What to Expect**

This 30-minute behavioral interview explores how you collaborate with people across
different teams and communicate in diverse settings. Expect to discuss past
experiences working with stakeholders, partners, and colleagues—the interviewer
wants to understand how you navigate cross-functional environments and build
productive working relationships.

**Focus Areas**

- Collaborating effectively across teams and partnering with diverse stakeholders
- Communicating clearly and adapting your message to different audiences and
  contexts
- Balancing competing priorities and perspectives to reach shared outcomes
- Building alignment and gaining commitment from others through compelling
  reasoning
- Handling challenging interpersonal dynamics with professionalism and composure

**How to Prep**

- **Gather cross-team stories:** Identify 2–3 examples where you worked with people
  outside your immediate team to drive an improvement, resolve an issue, or deliver
  a project. Be ready to explain your specific role and contribution.
- **Reflect on influence moments:** Think about times you needed to persuade someone
  who was initially hesitant or had a different viewpoint—how you presented your
  case and what data or examples built your credibility.
- **Consider challenging dynamics:** Prepare to discuss situations involving
  difficult colleagues, conflicting priorities, or tough feedback—both giving and
  receiving—focusing on how you maintained respect and moved toward resolution.
- **Practice concise storytelling:** Use a clear structure (situation, your actions,
  outcome), keep responses focused, and highlight how you adjusted your
  communication style for different audiences.

### General Tips *(guide, p. 6 — applies to every round)*

- **Be yourself.** We want to understand how you think and work—there are no trick
  questions.
- **Ask clarifying questions.** It's encouraged and shows thoughtful engagement.
- **Use concrete examples.** Draw from real experiences whenever possible.
- **Prepare questions for your interviewers.** This is also your chance to learn
  about the team and role.

---

## Question bank — every question with its answer

One question, one answer. **Three are marked ★** — the cross-team opener, the
influence answer, and the tense-relationship answer — because they're the most
likely to be asked and they set the frame.

> **These are written to be said out loud, not read.** Short sentences, one idea
> each, plain words. If a phrase feels awkward in your mouth, change it — keep the
> thread and the numbers, the wording is yours.

---

### Collaboration

#### ★ "Tell me about a project where you worked with a team outside your own. What was your specific role?"

> At Meta, several teams each had their own path to the same network data, and the
> numbers disagreed. It wasn't anyone's project. I found the gaps and verified them
> myself before I said anything — I wanted to walk in with specific cases, not a
> complaint.
>
> Then I called the meeting: the engineers who owned each path, the PM, and the people
> actually consuming the numbers. My role in that room was narrow on purpose. I wasn't
> there to decide whose pipeline was wrong — I owned the question of *why* they
> disagreed, and I owned making that visible. So I built the discrepancy dashboard
> first: per dataset, per metric, every path against the unified one, live. That made
> the discrepancy the subject instead of the teams.
>
> The negotiation was with the PM and the users. The unified API was months out and they
> needed their numbers to agree now. So we committed to two tracks — I'd improve the
> existing APIs first, knowing I'd throw that work away, and build the unified one in
> parallel, migrating consumers one at a time behind a flag rather than asking anyone
> for a cutover.
>
> Their teams owned their own migrations. I owned the interface, the dashboard, and the
> sequencing. 100% of users ended up on the unified API, and the discrepancies got fixed
> instead of argued about.

#### *Follow-up:* "What if they hadn't agreed?"

> I'd make the reasoning explicit, because the two tracks answer different concerns.
> The quick fix is there so the numbers are right inside a window people can live with.
> The unified API is there to lower the total cost of ownership — one path to maintain
> instead of five that drift apart again.
>
> If someone wanted to drop one, I'd ask for the reason, and I'd hold it to a real bar:
> either a fact I didn't have, or an alternative that resolves both concerns. Dropping
> the quick fix leaves people wrong for months. Dropping the unified API saves a quarter
> and buys the same problem back.
>
> And if it is a fact I didn't have, I change the plan. That's the point of asking.

#### "How do you build a working relationship with a team you've never worked with?"

> Three things, in order.
>
> First, learn their area before I ask them for anything — what they're measured on, and
> enough of their domain to follow a conversation without needing it translated. Most
> cross-team friction isn't personality. It's that the thing I need is neutral or
> negative for their goals and I didn't know it. It's also why I've deliberately kept my
> knowledge broad rather than deep in one place. For cross-team work, breadth is the
> useful shape — I don't have to be their expert, I have to be able to hold up my end.
>
> Second, spend time with them before I need something from them. A conversation that
> isn't a request costs twenty minutes and changes every conversation after it. Then
> make the first ask small and specific — "I need this one field by Thursday" gets
> answered; "can your team support this project" gets a meeting.
>
> Third, and this is the one that actually works — put a shared artifact in front of
> both of us early. When I was consolidating the data APIs at Meta, the dashboard
> comparing every team's numbers did more for those relationships than any meeting did.
> It moved the conversation off whose team was wrong and onto why the data disagreed.
>
> Then I do what I said I'd do on the small thing. Most of it is that.

#### "Describe a time you depended on another team to deliver and they were behind."

> My baseline is that cross-team work only holds if two things are agreed up front: the
> plan and timeline for each deliverable, and that risk gets raised the moment it
> appears. A delay I hear about at the last minute is the real failure. Early, I can
> replan, rescope, or rebalance who's carrying what. Late, all I can do is apologize.
>
> The hardest version is a priority change, and I had one at Kaamel. Another team owned
> the data embedding work the AI assistant depended on. Mid-stream our CEO needed a
> proof of concept demoed to secure funding, and they were the team who could build it.
> Their priority changed effectively overnight, and the embedding work wasn't going to
> land on our date.
>
> Nobody was wrong there. Funding beats my schedule.
>
> So we did two things, and neither of them was waiting. We went to the customer and
> negotiated a deadline extension rather than ship something incomplete on the original
> date. And instead of holding the date open for the original team to come back — they
> stayed on the PoC the whole way through — I was one of the people who picked up the
> embedding work directly. That's what actually made the new date.
>
> That's usually my move when another team slips for a legitimate reason. Escalating
> gets me a ruling I already know the answer to. Covering the gap gets the thing built.
>
> The part that mattered most came after. We ran a retro, and the conclusion wasn't
> "communicate better" — it was that a request like that PoC is foreseeable. Surface
> that kind of requirement early and it gets planned for, instead of arriving as a
> surprise that costs another team their date.

#### "Tell me about working with someone in a very different function."

> The lawyers at our customers, during requirements for the questionnaire assistant.
>
> What I was handed was that the answers had to be high quality and satisfy the
> customer. That's an adjective. And the lawyer who'd be on the hook if an answer was
> wrong couldn't define it either — she knew a bad answer when she saw one and couldn't
> give me the rule in advance.
>
> So I stopped asking what quality meant and asked what she cared about most. Same
> answer from everyone I asked: is it correct, and if this gets challenged, how do I
> defend it?
>
> Nobody said the word traceability. That translation was my job, and it's the part
> people skip when they work across functions. She gave me a word from her world —
> defend — and I had to turn it into four things I could build and test. Every answer
> grounded in the knowledge base rather than the model's general knowledge. Every answer
> traceable to the record it came from. No assumption when the knowledge base has
> nothing. And human review in the loop.
>
> Then I took the translation back to her and checked it in her terms, not mine.
>
> That turned out to be the whole product. Traceability wasn't a quality feature. It was
> the reason customers were willing to buy at all.

---

### Influence

#### ★ "Tell me about a time you convinced someone who initially disagreed."

> Same project — the network data with five paths to it and numbers that disagreed. The
> person I had to convince was the PM, and what he disagreed with was the two-track plan.
> His position was: ship the quick fix, get the numbers agreeing, move on.
>
> He wasn't being short-sighted. The complaint he was hearing was "our numbers are
> wrong." The quick fix answers that complaint. Everything after it is invisible to the
> people complaining — from where he sat, the unified API was months of engineering no
> user would ever see.
>
> So I didn't argue that my design was better. That argument goes nowhere with a PM,
> because he isn't evaluating designs, he's allocating time.
>
> I put it in the terms he actually owns — total cost of ownership. The quick fix makes
> five paths agree today; it doesn't make them one path. Every schema change, every new
> metric, every backfill after that gets done five times and verified five times, and the
> discrepancies come back the next time anyone touches one. The dashboard made that
> concrete rather than theoretical — he could see the drift, so "they'll drift again"
> wasn't me predicting, it was a pattern he was already looking at.
>
> Then I made it not a choice. Two tracks. He gets the quick fix on his date — I did that
> work first, knowing I'd throw it away — and the unified API gets built behind it,
> migrating one consumer at a time behind a flag, so it's never a launch he has to
> schedule or a risk he has to carry.
>
> He agreed. And I don't think it was the cost argument by itself. It was that I took his
> deadline off the table before I asked him for anything.

#### "How do you make a case when you don't have data yet?"

> Late 2023, just joined Kaamel. We had to pick what to build with AI, and the market
> didn't exist yet in any measurable form.
>
> So I went after the cheapest evidence available. I counted competitors in each area,
> and our building was full of startups, so I walked around asking people what they were
> working on. Not rigorous, but a live sample, and I had it in days. Same thing I'd do on
> a hard bug — if I can't get the measurement I want, take the one I can get and use it
> to rule things out.
>
> It reframed the question. The ideas we liked were crowded, and crowded *because* they
> need no domain expertise. Anyone can build a resume generator, which is exactly why we
> couldn't win one. So I judged each area on one criterion — where do we have a moat.
> That pointed at compliance, SOC 2 with AI: harder to enter, and we had a lawyer in the
> founding group and customer relationships through our CEO.
>
> That's the business we're in today, and we're profitable.

#### "Describe a time you pushed for a change that wasn't your call to make."

> A few weeks into Kaamel, the team was already building an AI resume generator and I
> thought we should stop. I had no authority to make that call and I'd been there
> almost no time.
>
> My reason was first-hand. I'd been job hunting not long before and used ChatGPT to
> write my resume. I was the target customer, and I wouldn't have paid for it.
>
> But that's one person, and a new hire's opinion is the weakest thing you can bring
> into a room. So I did the competitor study and the market sizing before I said
> anything. When I raised it, I said plainly which part was evidence and which part was
> me, and I put the question on the product rather than on the people who'd been
> building it.
>
> The project was stopped. But the decision was the founders' to make, and that's the
> distinction I'd draw. I wasn't asking anyone to trust my judgment — I was putting the
> same information in front of everyone who did have the call.
>
> The risk isn't disagreeing. It's disagreeing with nothing behind you.

#### "Tell me about a time you were overruled. What did you do next?"

> The discount on the questionnaire assistant. We launched in mid-2024 and customers
> wouldn't buy it. They said the answer quality was low, and the response was to cut the
> price. I didn't own pricing — I influenced it, I didn't decide it.
>
> What I did next is the part I'd stand behind. I didn't relitigate the decision; I made
> sure we'd find out quickly whether it was right. The discount did nothing. Not a small
> effect — none.
>
> That's a better outcome for me than winning the argument would have been, because now
> it wasn't my read against anyone's. A price change that moves nothing means price was
> never the objection.
>
> So I went back to customers and asked what they were actually worried about. These
> answers go to their customers' auditors. A plausible answer they couldn't verify
> wasn't an inconvenience, it was legal exposure. They weren't declining to pay for a
> mediocre tool. They were declining to put their name on something they couldn't check.
>
> The fix was a product change, not a price change and not a model change. Surface the
> source record on every answer, make human review mandatory instead of a setting, and
> trade early access to a few customers for a real feedback loop. 85% of answers are now
> accepted as-is, on the customer's own accept-edit-reject click.
>
> When a decision is reversible and someone else owns it, the useful move is usually to
> make it measurable rather than to keep arguing.

---

### Communication

#### "Describe a time you had to explain something technical to a non-technical audience."

> Customers weren't buying the questionnaire assistant, so I went to talk to a lawyer at
> one of them — she'd be the person on the hook if an answer was wrong.
>
> Her feedback was that the answer quality was suspicious, and maybe AI just wasn't
> smart enough for this work. I can't act on that, so I asked for concrete examples. She
> pulled up specific questions and answers, and what she said was that she couldn't
> understand where they came from.
>
> When I went through them, they were three different problems. Some were questions we
> had nothing in the knowledge base for. Some had information that was out of date. And
> some were correct given what was in the knowledge base — just not intuitive to someone
> reading them.
>
> She didn't have the vocabulary for that. Context, knowledge base, model — none of
> those meant anything to her. So I didn't explain the architecture. I gave her one
> distinction: is the model wrong, or do we simply not have the answer written down
> anywhere? Those look identical in the output and they're opposite problems. One is our
> system. The other is her company's documentation.
>
> Then I stopped explaining and showed her. We surfaced the source link on every answer.
> Once she could click through to the passage an answer came from, she could sort her
> own examples without me — and for the correct-but-unintuitive ones, the link did the
> entire job.
>
> With a non-technical partner the win usually isn't a better explanation. It's finding
> the one distinction they actually need, and then making the evidence visible so they
> don't need me in the room.

#### "How do you adjust your communication for an executive versus an engineer versus a partner?"

> I think about what decision the person has to make, and give them the smallest thing
> that makes it.
>
> Same product, three versions. Our founder wanted the acceptance rate and the shape of
> what was still failing — he's allocating people, so he needs one number and one trend.
> A customer's security lead wanted the source passage behind an individual answer,
> because he's defending that specific answer to an auditor. The engineers on my team
> needed the failure taxonomy: the rejected answers split into controls that had changed
> since we indexed them, and questions nobody at the company had ever documented. Those
> need opposite fixes.
>
> Same fact at three resolutions. The mistake is handing any of them someone else's
> version. A founder given a retrieval taxonomy tunes out. A security lead given an
> aggregate acceptance rate can't do anything with it.
>
> The other half is vocabulary. With a non-technical partner I pick the one distinction
> they need and drop everything else. With that lawyer it was: is the model wrong, or do
> we not have the answer written down anywhere? That was all she needed.
>
> And where I can, I stop explaining and show them. A source link they can click does
> more than a good analogy.

#### "Tell me about a time you were misunderstood. What did you do?"

> Early in the data consolidation at Meta. I went to the teams owning each data path and
> told them their numbers didn't agree with each other. What they heard was that I was
> saying their numbers were the wrong ones.
>
> Which was fair. I hadn't been careful, and I didn't actually know who was right —
> nobody did. But "your data disagrees with theirs" and "your data is wrong" are one
> word apart in the room and completely different accusations.
>
> The first thing I did was stop having the conversation in words. I built the
> discrepancy dashboard — per dataset, per metric, every path against every other, live.
> That took me out of the middle of it. Nobody had to accept my characterization of
> anything; they could look.
>
> The second thing was changing the question I was asking out loud. Not whose numbers
> are wrong — why do they disagree. That was the question I actually cared about, and I
> hadn't been saying it clearly.
>
> After that the room changed. It went from people defending their own path to people
> looking at the same chart, working out which transformation explained the delta. The
> discrepancies got fixed instead of argued about, and the unified API went to 100% of
> users.
>
> Being misunderstood usually means I picked a frame that made someone the subject when
> the problem should have been.

#### "Tell me about documentation or a guide you wrote that others actually used."

> Two, and the useful one is the less obvious one.
>
> The straightforward one is the requirements spec for the questionnaire assistant. What
> I was handed was "high quality answers." What the team needed was something buildable
> and testable. So the document turned the customers' word — defend — into four
> properties: grounded in the knowledge base rather than the model's general knowledge,
> traceable to the source record, no assumption when there's nothing to retrieve, and
> human review in the loop. That's what we built against, and what we pointed back at
> later when there was pressure to cut a corner.
>
> The less obvious one is that the most-used thing I've written wasn't prose. At Meta
> the discrepancy dashboard was documentation. It was the standing answer to "which of
> these numbers do I trust," and teams used it long after the migration, without me in
> the room. A living artifact that answers the question beats a document describing the
> answer, because the document goes stale and nobody notices.
>
> The rule I follow writing for a mixed audience: lead with the decision the reader has
> to make, put the mechanism underneath it, and keep the two separated — so a
> non-technical reader can stop after the first part and still be correct.

---

### Competing priorities

#### "Two teams need conflicting things from you. How do you handle it?"

> First I check whether it's actually a conflict, because a lot of the time it's a
> sequencing problem wearing a conflict costume. If I can serve both in an order, that's
> not a decision, it's a schedule.
>
> The data layer at Meta looked like a conflict and wasn't one. The unified API was the
> right answer and it was months out; the users wanted their numbers to agree now. So I
> improved the existing APIs first to close the gaps — work I knew I'd throw away — and
> built the unified one in parallel. Both got done. Serving the users first meant
> absorbing temporary work; it didn't mean skipping the right thing.
>
> A real one at Kaamel. The AI assistant was a commitment to customers. Mid-stream our
> CEO needed a proof of concept demoed to secure funding, and the team who could build it
> was the team that owned the data embedding the assistant depended on. So two things
> landed on me at once: deliver the assistant, and swarm in to cover the embedding gap
> that opened when they moved.
>
> Neither ask was refusable. Funding beats my schedule, and the assistant was a promise
> to a customer.
>
> So I stopped trying to choose between the two and chose which variable to give up
> instead — scope, quality, or the date. I picked up the embedding work, and the date was
> what I gave up, because it was the only one of the three that was recoverable. Then I
> went to the customer and negotiated a new date early, rather than shipping something
> incomplete on the original one or missing it quietly.
>
> We made the new date. And the cost was real — the customer waited. I'd rather say that
> than pretend both landed for free.
>
> That's the rule underneath both: say the cost out loud. "I'm doing this first, and
> here's what it delays for you" is a much better relationship than quietly
> deprioritizing someone.

#### "Describe a time you had to say no or push back on a request."

> At Meta, the PM wanted to ship the quick fix on the data discrepancies and move on. I
> pushed back on the second half of that, not the first. The quick fix was right — people
> needed correct numbers now. What I wasn't willing to agree to was stopping there.
>
> And it wasn't really a disagreement about priorities. It was a gap. Total cost of
> ownership isn't in a PM's field of view — he's looking at ship dates and user-visible
> value, and by both of those measures the quick fix wins and the unified API is months
> of work no user ever sees.
>
> So instead of arguing for my design, I filled the gap. Five separate paths to the same
> data means every schema change, every new metric, every backfill gets done five times
> and verified five times — and the discrepancies come back the next time anyone touches
> one. The quick fix makes five paths agree today; it doesn't make them one path. That
> cost was invisible on his roadmap and it was going to come out of engineering time
> every quarter, forever.
>
> Once he could see it, he wasn't opposed. We committed to two tracks — his date for the
> quick fix, the unified API built behind it.
>
> Pushing back well is usually less about holding a position than about making the thing
> I can see visible to the person who can't.

#### "Tell me about a trade-off you made between speed and quality."

> Both directions, and the pair is the honest answer.
>
> Where I chose speed and got it wrong: we launched the questionnaire assistant in
> mid-2024 with the answers good and the trust problem unsolved. The system could
> already trace every answer back to its source record — the customer just couldn't see
> it. Surfacing that was work we hadn't done, and we shipped anyway because the output
> looked strong. Customers wouldn't buy it. Provenance you can't see isn't provenance.
>
> Where I chose quality and would again: human review stayed mandatory rather than
> becoming a setting. That's slower for the customer, every time, permanently. But those
> answers go to auditors, and if a confident wrong answer is irreversible, the model
> drafts and a person sends.
>
> The distinction I use is whether what I'm trading away is recoverable. A rough feature
> is recoverable — you iterate. Trust isn't. You don't get it back on the second attempt.
>
> And on an AI product I'd put traceability and transparency outside the trade entirely.
> They aren't polish you sequence after launch. An answer nobody can check isn't a
> cheaper version of one they can — it's a different product, and it's the one people
> won't act on. That's what actually went wrong at our launch. We thought we were trading
> polish for speed, and we were shipping without the part that made the thing worth
> buying.

---

### Difficult dynamics

#### ★ "Tell me about a difficult colleague or a tense working relationship."

> The PM I worked with on the data layer at Meta. In any single meeting he was fine — the
> difficulty was a pattern.
>
> His instinct was always the quick fix. Patch it, ship it, move on. And in any one
> instance he had a case: it's faster, users are unblocked, and the systematic version
> costs months. You can't point at a single one of those decisions and call it wrong.
>
> The problem was that they accumulated. Every quick fix left one more path to maintain,
> and that cost never showed up anywhere he was looking — it came out of engineering
> time, quarter after quarter. By the time it's visible, you're spending most of your
> capacity keeping things alive instead of building.
>
> And I was making it worse. My habit — this is exactly the feedback my manager had given
> me — was to route around someone like that instead of saying anything. So it never got
> discussed. I'd absorb it and get quietly frustrated, which is how a working
> relationship goes bad without a single argument in it.
>
> So I changed what I treated as the problem. It wasn't that he made bad calls. It was
> that total cost of ownership had never been put in front of him — and that isn't his
> failing. A PM is measured on shipped, user-visible value. Maintenance cost appears on
> nobody's roadmap. He was optimizing the thing he was being asked to optimize.
>
> So I taught it instead of arguing it. Five separate paths to the same data means every
> schema change, every new metric, every backfill gets done five times and verified five
> times. Here's what we're paying for that today, here's what it looks like in a year.
>
> That did more for the relationship than winning any single argument would have. We
> ended up with a shared vocabulary for the trade-off, and after that he'd raise it
> himself.

#### "Describe a time you had to give someone critical feedback."

> The PM on the data-layer work at Meta. His default on every problem was the quick fix —
> patch it, ship it, move on. Any one of those calls was defensible; the pattern was tech
> debt that came out of engineering time quarter after quarter.
>
> The feedback I gave him was that he was making those calls without one of the numbers.
> Five separate paths to the same data means every schema change, every new metric, every
> backfill gets done five times and verified five times. Here's what we're paying for
> that today, and here's what it looks like in a year if every quick win adds to it.
>
> I gave it early, and I put it on the work rather than on him. That's the part I'd
> underline: he could check the cost himself, so he didn't have to concede anything about
> his own judgment to agree with me. Feedback that lands isn't feedback that's softened —
> it's feedback the person can verify.
>
> He took it. We did the quick fix so users weren't blocked, then the unified API. And
> after that he'd raise the maintenance question himself, which is the only real evidence
> that feedback worked.

#### "Tell me about difficult feedback you received."

> My manager at Meta told me I didn't give constructive feedback. I'd see a problem in
> how someone was working, or a collaboration heading the wrong way, and I'd work around
> it instead of saying it. He framed it as a leadership weakness, not a style
> preference.
>
> My honest reaction was that it wasn't really my job. My view then was that if you're
> strong technically, people skills are a nice-to-have.
>
> What changed my mind wasn't the feedback, it was the next year of evidence. The same
> problems kept coming back, because I'd never named them the first time. The clearest
> case was the PM on the data-layer work. I'd been quietly working around his instinct to
> patch and move on for months — absorbing the cost rather than raising it. Nothing was
> ever wrong enough to have a fight about, and the relationship was deteriorating anyway.
> That's the part I hadn't understood: routing around someone isn't neutral. It just
> moves the cost somewhere it doesn't get discussed.
>
> So I worked on it deliberately. Say it close to when it happens instead of saving it
> up, and keep the subject on the work rather than the person. With him that meant
> putting the maintenance cost of five separate data paths in front of him early instead
> of building around him. We did both tracks, and after that we had a shared way of
> talking about the trade-off.
>
> Where I've come out is that this isn't optional for anyone who wants real impact. You
> can be the strongest engineer in the room and still be the bottleneck.

#### "Describe a time you had to deliver bad news to a partner or stakeholder."

> The AWS us-east-1 outage last October. Fourteen and a half hours. The AI gateway and
> the database were both degraded, we had no cross-region copy of either, and full
> recovery was going to happen on AWS's schedule, not ours.
>
> So the news was the worst kind: this is broken, a large part of it isn't in our
> control, and I can't give you a time. I said exactly that, and I didn't invent an ETA —
> a made-up estimate is a second failure on top of the first.
>
> But a status update on its own is useless to a customer. What they need is what they
> can still do. Full recovery wasn't in our hands; the blast radius was — so I brought the
> analysis and the options along with the news.
>
> The biggest one: customers couldn't log in at all. Login needed a secret out of Secrets
> Manager, and Secrets Manager in us-east-1 was down — but there was a copy in us-west-1,
> so I pointed the login workflow at that one and got people back into the product. That
> moved the outage from "you have nothing" to "these specific functions are degraded,"
> which is a completely different conversation to have with a customer. Past that,
> retrying genuinely succeeded some of the time — a workaround rather than reassurance.
>
> That's the difference between reporting someone's problem back to them and shrinking
> it. Factual and frequent, and every update carries either something they can act on or
> something we've narrowed.
