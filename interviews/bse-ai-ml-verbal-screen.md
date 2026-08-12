# Meta BSE (GenAI) — AI/ML Knowledge Verbal Screen

Prep notes for **Section 3** of the Business Support Engineer – AI Focused
initial technical screen: **~10 minutes, verbal Q&A, no coding, no outside tools.**

It's a conversation, not a quiz. If you show hands-on ML experience the
interviewer skips fundamentals and goes deeper on LLMs. They weight **clear,
plain-English communication** heavily (it's a customer-facing role), so answers
below are written to be spoken in 2–4 sentences. Lead with the one-liner, then
add color if they probe.

> **Source note:** The exact verbal questions for this specific role are not
> publicly posted. Fundamentals phrasing is drawn from Meta ML Engineer
> interview guides (Double Pointer, Exponent); LLM questions are standard
> big-tech AI-screen questions (DataCamp, awesome-generative-ai-guide,
> InterviewQuery). Topic list mirrors Meta's official prep guide.

---

## Contents

- [ML Fundamentals](#ml-fundamentals)
  - [Overfitting vs. underfitting](#q-what-are-overfitting-and-underfitting)
  - [Preventing overfitting](#q-how-do-you-prevent-overfitting)
  - [Regularization / L1 vs L2](#q-what-is-regularization-l1-vs-l2)
  - [Cross-validation](#q-what-is-cross-validation)
  - [Bias–variance tradeoff](#q-explain-the-biasvariance-tradeoff)
  - [Supervised vs. unsupervised](#q-supervised-vs-unsupervised-learning)
  - [Evaluating a model](#q-how-do-you-evaluate-a-model)
  - [Generative vs. discriminative](#q-generative-vs-discriminative-models)
- [Large Language Models](#large-language-models)
  - [What is an LLM / how it works](#q-what-is-an-llm-and-how-does-it-work)
  - [Tokenization](#q-what-is-tokenization)
  - [Embeddings](#q-what-are-embeddings)
  - [Attention / self-attention](#q-what-is-attention)
  - [Transformer & encoder/decoder](#q-transformer-architecture--encoder-vs-decoder)
  - [Temperature & decoding](#q-what-does-temperature-do)
- [LLM Challenges & Solutions](#llm-challenges--solutions)
  - [Hallucination](#q-what-is-hallucination-and-how-do-you-reduce-it)
  - [RAG](#q-what-is-rag)
  - [RAG vs. fine-tuning](#q-rag-vs-fine-tuning-when-to-use-each)
  - [Prompt engineering / multi-shot](#q-what-is-prompt-engineering)
  - [Other challenges: cost, latency, memory](#q-what-are-the-main-challenges-with-llms-in-production)

---

## ML Fundamentals

### Q: What are overfitting and underfitting?

**Overfitting** is when a model learns the training data too well — including its
noise — so it performs great on training data but poorly on new, unseen data. It
has **low bias, high variance**. **Underfitting** is the opposite: the model is
too simple to capture the underlying pattern, so it does poorly on both training
*and* test data (**high bias, low variance**).

*How to spot it:* overfitting shows a big gap between high training accuracy and
low validation accuracy; underfitting shows both being low.

### Q: How do you prevent overfitting?

The core idea is to reduce model complexity or give it more/cleaner signal:
- **Regularization** (L1/L2) — penalize large weights
- **Dropout** — randomly drop neurons during training so it can't over-rely on any one
- **Cross-validation** — validate on multiple splits to catch it early
- **Early stopping** — stop training once validation loss stops improving
- **More / augmented training data**
- **Simpler model** or fewer features
- **Data normalization**

### Q: What is regularization? (L1 vs L2)

Regularization adds a penalty for model complexity to the loss function so the
model prefers smaller weights and generalizes better. **L2 (Ridge)** penalizes
the sum of squared weights — it shrinks weights toward zero smoothly. **L1
(Lasso)** penalizes the sum of absolute weights and can drive some weights
exactly to zero, so it also does **feature selection**.

### Q: What is cross-validation?

It's a way to estimate how well a model generalizes by splitting the data into
several folds. In **k-fold** CV you train on k−1 folds and validate on the
remaining one, rotating through so every fold is used for validation once, then
average the results. It gives a more reliable estimate than a single train/test
split and helps detect overfitting.

### Q: Explain the bias–variance tradeoff.

**Bias** is error from overly simple assumptions (leads to underfitting);
**variance** is error from being too sensitive to the training data (leads to
overfitting). Lowering one tends to raise the other, so the goal is the sweet
spot that minimizes total error on unseen data.

### Q: Supervised vs. unsupervised learning?

**Supervised** learning trains on **labeled** data — each example has a known
answer — to predict a label. Examples: a spam classifier, image recognition,
price prediction. **Unsupervised** learning works on **unlabeled** data to find
structure on its own. Examples: customer segmentation, clustering, anomaly
detection. *(Bonus: reinforcement learning learns from reward/feedback through
trial and error.)*

### Q: How do you evaluate a model?

It depends on the task. For **classification**: accuracy, precision, recall, F1,
and ROC-AUC — and I'd stress that accuracy alone is misleading with imbalanced
classes, where precision/recall matter more. For **regression**: RMSE, MAE, R².
And always evaluate on a **held-out test set** the model never saw during
training.

### Q: Generative vs. discriminative models?

A **discriminative** model learns the boundary between classes — it models
P(label | data) directly (e.g., logistic regression). A **generative** model
learns how the data is distributed, P(data, label), so it can generate new
samples (e.g., an LLM, or Naive Bayes). LLMs are generative.

---

## Large Language Models

### Q: What is an LLM, and how does it work?

At a high level, an LLM is a neural network trained on huge amounts of text to
**predict the next token** in a sequence. By doing that over and over it
generates fluent, human-like text. It's built on the **transformer**
architecture, and the key trick is the **attention** mechanism, which lets it
weigh how relevant every other token is when producing the next one.

### Q: What is tokenization?

Tokenization is breaking text into smaller units — **tokens** — that the model
actually processes. Tokens are usually subwords, not whole words (e.g.,
"tokenization" → "token" + "ization"). This keeps the vocabulary manageable and
lets the model handle rare or unseen words. *Fun tie-in: because models see
tokens, not characters, they're often bad at spelling or arithmetic.*

### Q: What are embeddings?

An embedding is a **numerical vector** that represents a token (or a whole piece
of text) in a high-dimensional space, where similar meanings end up close
together. That's what lets the model do math on meaning — e.g., "king" and
"queen" are near each other. Embeddings are also what power semantic search and
the retrieval step in RAG.

### Q: What is attention?

Attention lets the model, for each token, look at all the other tokens and decide
which ones matter most for the current prediction — so it captures context and
long-range relationships (like which noun a pronoun refers to).
**Self-attention** does this within a single sequence, and doing it in parallel
across the whole input is what makes transformers efficient and powerful.

### Q: Transformer architecture / encoder vs. decoder?

The transformer is the architecture behind modern LLMs; its core is stacked
attention layers. An **encoder** reads and builds a rich representation of the
input (good for understanding tasks like classification — e.g., BERT). A
**decoder** generates output one token at a time (good for generation — e.g.,
GPT-style models). Some models use both (encoder–decoder, e.g., translation).

### Q: What does temperature do?

Temperature controls **randomness** in the output. **Low** temperature (near 0)
makes the model pick the most likely tokens — more deterministic and focused,
good for factual tasks. **High** temperature makes it more diverse and creative
but also more error-prone. For a support/factual use case you'd typically lower
it.

---

## LLM Challenges & Solutions

### Q: What is hallucination, and how do you reduce it?

Hallucination is when the model generates something **plausible-sounding but
false** — because it's optimizing for likely text, not verified truth. Ways to
reduce it:
- **RAG** — ground answers in retrieved, authoritative sources
- **Fine-tuning** on high-quality domain data
- **Lower temperature**
- **Multi-shot / few-shot prompting** with good examples
- **Better dataset quality**
- **Human/user feedback loops** and citing sources so answers are verifiable

### Q: What is RAG?

Retrieval-Augmented Generation. Instead of relying only on what the model
memorized in training, you first **retrieve** relevant documents (usually via
embedding-based semantic search over a vector store) and feed them into the
prompt as context, so the model answers **grounded in that real information**. It
reduces hallucination, keeps answers current, and lets you use private/domain
data without retraining.

### Q: RAG vs. fine-tuning — when to use each?

**RAG** is best when you need **up-to-date or proprietary knowledge** and want to
cite sources — it's cheaper, faster to update (just change the documents), and
grounds answers in facts. **Fine-tuning** is best when you need to change the
model's **behavior, style, or format**, or teach it a specialized skill/domain
tone. They're complementary — a common setup fine-tunes for behavior and uses
RAG for knowledge.

### Q: What is prompt engineering?

Crafting the input to steer the model toward better output — clear instructions,
context, constraints, and examples. **Few-shot / multi-shot prompting** gives the
model example input→output pairs so it follows the pattern; **chain-of-thought**
asks it to reason step by step, which improves accuracy on complex tasks.

### Q: What are the main challenges with LLMs in production?

- **Hallucination / accuracy** — plausible but wrong answers
- **High compute cost** — expensive to train and serve
- **Latency** — big models can be slow to respond
- **Memory / context limits** — a fixed context window bounds how much they can consider at once
- **Domain gaps** — weaker on specialized topics not well-covered in training

The practical job is **managing the tradeoffs** — cost vs. quality vs. latency —
e.g., using a smaller/distilled model, caching, or RAG instead of a bigger model.

---

## 30-second closers (if asked "anything else?")

- **Why this matters for support:** grounding answers in RAG and lowering
  temperature are the levers that make an LLM assistant reliable enough to put in
  front of customers.
- **Staying current:** name a recent trend you actually follow (e.g., longer
  context windows, smaller efficient models, agentic tool use) — the guide
  explicitly values awareness of tradeoffs.

## Prep resources (from Meta's guide)
- Google's Machine Learning Crash Course
- 3Blue1Brown — Neural Networks playlist (visual intuition)
- Andrej Karpathy — "Intro to LLMs" (1-hour overview)
