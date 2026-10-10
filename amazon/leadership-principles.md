# Amazon Leadership Principles — Story Answers

## Bias for Action

#### "Tell me about a time you made a decision with incomplete information."

> **Situation** — Back in late 2023, shortly after I started at Kaamel, we were a small
> startup trying to decide what to build with AI. We had a lot of ideas, like a resume
> generator and a travel booking tool, but the market was too new to have real data,
> and we were worried about falling behind.
>
> **Task** — I took on recommending a direction. The data we wanted wasn't going to
> show up, so waiting for it just meant going in circles.
>
> **Action** — So I got whatever information I could quickly. I counted competitors in
> each area, and since our building was full of startups, I walked around and asked
> people what they were working on. It wasn't scientific, but it showed me fast which
> ideas everyone else was chasing too.
>
> Those crowded ideas didn't need any special expertise. Anyone could build a resume
> generator, so we couldn't win there. So I asked one question: where do we actually
> have an advantage? That led to compliance, SOC 2 with AI. It's harder to get into,
> and we had a lawyer on the founding team and customer connections through our CEO.
>
> But I didn't want to bet the company on my analysis alone. So we built a proof of
> concept quickly and showed it to a few customers who were also our partners. They
> used it for free, and in return gave us fast feedback. That loop let us iterate much
> faster. If the direction was wrong, we'd find out early and adjust, instead of after
> months of building.
>
> **Result** — The early feedback was tough, but it was about how we'd built it, not
> whether customers needed it. So we fixed the product and kept the direction. It's
> still our business today, and we're profitable, which for a company our size is
> a pretty good sign it was the right call.
>
> What I learned is that when you can't get the data you want, use what you can get,
> and then get real feedback as early as you can.

#### Follow-up: "What feedback did you get from the partners, and how did it change your design?"

> Honestly, the first feedback was pretty negative. Users said the answer quality was
> low, and a lawyer at one of our partners told me the AI just wasn't smart enough for
> this work.
>
> I couldn't act on that, so I asked her for concrete examples. She pulled up specific
> questions and answers, and what she kept saying was that she couldn't tell where the
> answers came from.
>
> When I went through them one by one, they were actually three different problems.
> Some were questions they had nothing written down for. Some were based on documents
> that were out of date. And some were correct, just not obvious to someone reading
> them. None of them were really the model not being smart enough.
>
> The real issue was trust. These answers go to their customers' auditors, so if they
> can't check an answer, they won't sign off on it. That changed the design in two
> ways. First, I put a source link on every answer, so a reviewer could click through to
> the exact passage and check it in seconds. That also let her sort her own examples:
> the missing and outdated ones were gaps in her company's documents, not the model.
> Second, I made human review a required step instead of an optional setting.
>
> After that, preparation effort dropped by 60%, and 85% of answers were accepted
> without changes.
>
> It changed how I design AI products in general. When people don't trust the output,
> making it easy to check usually matters more than making it smarter.

## Learn and Be Curious

#### "Describe a time you took on work outside your comfort area. How did you build the expertise?"

> **Situation** — When I joined Kaamel, I had two big gaps. I didn't know anything about
> SOC 2 compliance, and building products on LLMs was still really new for everyone.
>
> **Task** — I was responsible for designing and building the retrieval part of our
> compliance product, so I had to get up to speed on both pretty quickly.
>
> **Action** — Usually when I learn something new, I gather a lot of material and study
> it carefully. I didn't have time for that, so I mostly learned by asking the model
> questions. The problem is, when you're new to a topic, you can't tell when the model
> is wrong. So I relied on a few checks that didn't need expertise.
>
> The first was consistency. I kept track of what it told me, and if it contradicted
> itself, I knew something was off.
>
> The second was paying attention to its assumptions. At one point it suggested fixing a
> quality problem by trying different LLMs and comparing them. But we only had access to
> the OpenAI API, and the problem wasn't really about the model anyway. So I spelled out
> our constraints, and after that its suggestions got a lot more useful.
>
> The third was double-checking anything important. For SOC 2, I compared what it said
> against the published criteria, and for anything that needed judgment, I asked the
> lawyer on our founding team.
>
> **Result** — I designed and shipped the retrieval system, and it became the core of
> our security questionnaire assistant. It cut customers' preparation effort by 60%, and
> 85% of its answers get accepted without changes.
>
> What I took away is that the model is great for figuring out which questions to ask,
> but I still have to verify the answers myself.
