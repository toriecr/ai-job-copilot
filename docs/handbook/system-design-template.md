# System Design Template — Support Bot over Internal Docs

Use this outline when an interviewer asks something like:

> *"Design a customer support bot that answers questions from our internal documentation."*

That prompt is common in **AI Engineer** and **LLM product** interviews. It's not asking for code — it's asking you to walk through architecture, tradeoffs, and production concerns out loud in ~15–30 minutes.

Your **ai-job-copilot** project is a miniature version of this same design.

---

## 1. Clarify requirements (2–3 min)

Ask before drawing boxes:

- **Users:** customers, internal support agents, or both?
- **Corpus:** help articles, API docs, policies, tickets — how big, how often updated?
- **Latency:** real-time chat vs async?
- **Accuracy bar:** wrong answer cost (refunds, legal, safety)?
- **Languages, PII, auth:** who can see what?

---

## 2. High-level architecture

```
User → API gateway → Orchestrator → [Retrieve from vector DB] → LLM → Response
                              ↓
                        Ingest pipeline (batch/on change)
                              ↓
                     Docs → chunk → embed → vector store
```

Name the main components: **ingestion**, **retrieval**, **generation**, **eval/monitoring**.

---

## 3. Ingestion pipeline

- Source connectors (Confluence, Zendesk, S3, etc.)
- **Chunking strategy** — fixed-size vs semantic/paragraph; overlap; metadata (title, URL, product area)
- **Embeddings** — model choice, re-embed on doc update
- **Vector DB** — Chroma/Pinecone/pgvector; one collection vs per-product indexes

---

## 4. Retrieval

- Embed user query → top-k similarity search
- **Hybrid search** (optional): keyword + vector for exact product names/SKUs
- **Reranking** (optional): cross-encoder on top-k for better precision
- Tune **k**, score thresholds, filters (product, date, access level)

---

## 5. Generation

- System prompt: stay grounded, cite sources, refuse when context insufficient
- Pass retrieved chunks + conversation history (watch **context window**)
- **Citations** in UI — builds trust, helps agents verify
- Fallback: escalate to human, or "I don't know"

---

## 6. Evals and quality

- Golden set of real support questions + expected sources/answers
- Track retrieval hit rate, answer contains checks, refusal behavior
- Human review loop on failures; regression tests in CI

---

## 7. Safety and guardrails

- No answers outside approved corpus for policy/legal topics
- PII redaction in logs; don't train on customer data without consent
- Rate limits, abuse detection, prompt-injection awareness
- Block or hand off on high-risk categories (medical, legal, billing disputes)

---

## 8. Production ops

- **Caching** — embed cache, frequent-query answer cache
- **Observability** — latency, token cost, retrieval scores, user thumbs down
- **Deployment** — API service, async workers for ingest, feature flags for prompt changes
- **Cost** — smaller model for routing, larger for synthesis; batch embed offline

---

## 9. Tradeoffs to mention

| Choice | Pros | Cons |
|--------|------|------|
| RAG vs fine-tune | Fresh docs, citations, cheaper updates | Retrieval quality is the bottleneck |
| Single vs multi-agent | Simpler | Router agent for billing vs tech vs returns |
| Sync ingest vs event-driven | Easier | Stale docs until pipeline runs |

Close with: *"I'd start with RAG + evals + citations, ship a narrow FAQ scope, then expand corpus and add tools (ticket lookup, order status) via function calling."*

---

## Practice prompt

From `ai-engineer-job-plan.md` Week 3:

> Practice out loud: **"Design a customer support bot over internal docs"** (10 min)

Time yourself. Hit sections 1 → 2 → 4 → 5 → 6 → 7. Skip deep detail on anything the interviewer doesn't care about.

---

## Related files

- `rag-pipeline.md` — core RAG steps this design uses
- `evals-basics.md` — quality layer
- `llm-tool-orchestration.md` — adding tools (lookup ticket, reset password) after basic RAG

---

*Stub — expand with diagrams and your portfolio numbers after Step 8.*
