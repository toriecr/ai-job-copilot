# RAG Pipeline

**RAG** = **Retrieval-Augmented Generation**: retrieve relevant documents first, then generate an answer grounded in that context — instead of relying on the model's training memory alone.

Think of it as **open-book exam** for the LLM: you give it the right pages before it writes the answer.

---

## The five steps

```
Documents → chunk → embed → store → retrieve → generate
```

| Step | What happens | In this project |
|------|--------------|-----------------|
| **1. Load** | Read source files (Markdown, PDFs, etc.) | `load_docs.py` reads `docs/playbook/` and `docs/handbook/` |
| **2. Chunk** | Split long docs into smaller pieces with metadata | `chunk.py` — e.g. ~500 tokens per chunk, overlap between chunks |
| **3. Embed** | Turn each chunk into a vector (embedding) | `embed.py` — OpenAI `text-embedding-3-small` |
| **4. Store** | Save vectors in a vector DB for similarity search | `store.py` — Chroma at `data/chroma/` |
| **5. Retrieve + generate** | On a question: find top-k similar chunks → pass to LLM → answer | `retrieve.py` + `rag.py` |

**At query time:** user question → embed question → similarity search → top-k chunks → prompt LLM with context → grounded answer (+ citations).

---

## When to use RAG

| Approach | Good for | Weak for |
|----------|----------|----------|
| **Prompt only** | General knowledge, creative tasks, no private data | Facts that change often, proprietary docs |
| **RAG** | Q&A over your docs, up-to-date knowledge, citations, "I don't know" when missing | Tasks needing new skills the model lacks |
| **Fine-tuning** | Consistent tone/format, domain jargon baked in | Fast-changing knowledge (retrain cost), factual recall from large corpora |

**Rule of thumb:** if the answer lives in *your* documents and changes over time → **RAG**. If you need a specific voice or output format on stable patterns → consider fine-tuning (often *after* RAG works).

---

## Key concepts

- **Grounding** — answer should stick to retrieved context, not invent facts
- **Top-k** — how many chunks to retrieve (e.g. k=5); tradeoff: recall vs noise vs token cost
- **Hallucination** — model adds plausible but wrong details; RAG + refusal rules reduce this
- **Out-of-corpus refusal** — when nothing relevant is retrieved, say "I don't know" instead of guessing

---

## Related files

- `evals-basics.md` — how to test whether RAG is working
- `llm-tool-orchestration.md` — RAG as one tool in an agent

---

*Stub — expand as you build Steps 1–2.*
