# Portfolio Project Coverage — Current Progress vs Plan

Comparison of **current progress** against the portfolio spec in `ai-engineer-job-plan.md`.

---

## Current status

**Portfolio: not started.**

No repo, no ingestion pipeline, no vector index, no RAG query path yet. PlaySide LLM experience is the primary qualification for applications now; this project is the bridge to industry-standard keywords (RAG, agents, evals, Docker).

**What exists today (planning only):**

- Job plan and portfolio spec (`ai-engineer-job-plan.md`)
- Corpus prep in this folder: playbook + handbook stubs under `docs/` (ready to copy into the repo when you scaffold it)

---

## Coverage at a glance

| Plan milestone | Status |
|----------------|--------|
| **Week 1: Repo + ingest pipeline** | Not started |
| **Week 2: RAG MVP** | Not started |
| **Week 3: Agent + evals** | Not started |
| **Week 4: Full portfolio (Docker, README)** | Not started |

| Area | Progress |
|------|----------|
| **P0 — RAG pipeline** | 0% |
| **P1 — Agent + evals + CI** | 0% |
| **P2 — Docker + observability + README** | 0% |
| **Overall portfolio spec** | **0%** |

---

## What the spec requires (nothing built yet)

Mapped to `ai-engineer-job-plan.md`:

| Spec item | Priority | Status |
|-----------|----------|--------|
| Document ingestion (Markdown) | P0 | ☐ Not started |
| Chunking + embeddings | P0 | ☐ Not started |
| Vector store (Chroma) | P0 | ☐ Not started |
| Ingest → embed → store pipeline | P0 | ☐ Not started |
| RAG query path (retrieve → generate) | P0 | ☐ Not started |
| Context-only / out-of-corpus refusal | P0 | ☐ Not started |
| HTTP API (`POST /ask`) | P0 | ☐ Not started |
| Source citations in answers | P0 | ☐ Not started |
| Compare 2 chunk strategies (README) | P0 | ☐ Not started |
| Tool-calling agent (2+ tools) | P1 | ☐ Not started |
| Eval harness (20–50 golden Q&A) | P1 | ☐ Not started |
| CI runs evals on push | P1 | ☐ Not started |
| Docker (`docker compose up`) | P2 | ☐ Not started |
| Observability (latency, tokens, scores) | P2 | ☐ Not started |
| Cost notes in README | P2 | ☐ Not started |
| Strong README (diagram, evals, tradeoffs) | P2 | ☐ Not started |

---

## Visual: where you are on the plan

```
[░░░░░░░░░░░░░░░░░░░░]  P0 RAG pipeline     0%
[░░░░░░░░░░░░░░░░░░░░]  P1 Agent + evals    0%
[░░░░░░░░░░░░░░░░░░░░]  P2 Docker + ops     0%
[░░░░░░░░░░░░░░░░░░░░]  README / story      0%
─────────────────────────────────────────
Overall portfolio spec:              0%
```

---

## How to phrase it on resume / LinkedIn

### Accurate today (before the repo exists)

Lead with **PlaySide production LLM work** (tool orchestration, iteration, shared runtime). Do **not** claim a RAG portfolio project until local RAG Q&A works end-to-end (Week 2 milestone).

Example (no portfolio yet):

> Software engineer with production LLM agent and tool-orchestration experience; building a RAG + evals portfolio project aligned with AI Engineer roles.

### After Week 2 (RAG MVP — local Q&A working)

> Built a local RAG prototype over personal job-search and AI study markdown: ingestion, OpenAI embeddings, Chroma retrieval, and context-grounded Q&A with out-of-corpus refusal.

### After eval harness (Week 2–3)

> Built **ai-job-copilot**: RAG assistant over job-search playbook + AI handbook with FastAPI API, source citations, and automated eval harness (retrieval + answer checks).

### Target wording (full portfolio — Week 4)

> Production-style doc assistant: FastAPI RAG API, tool-calling agent, automated eval suite in CI, Dockerized deployment, with observability and documented design tradeoffs.

---

## Suggested next steps (build order)

| Phase | Task | Est. effort |
|-------|------|-------------|
| **Setup** | Create `ai-job-copilot` repo, venv, `.env`, copy corpus into `docs/` | ~2–3 hrs |
| **Week 1** | Ingestion: load → chunk → embed → Chroma | ~4–6 hrs |
| **Week 2** | RAG query path + refusal rules; then FastAPI `POST /ask` + citations | ~5–9 hrs |
| **Week 2–3** | Golden eval set + eval runner script | ~3–5 hrs |
| **Week 3** | CI runs evals on push; tool-calling agent (2+ tools) | ~5–8 hrs |
| **Week 4** | Docker + basic logging; README polish and architecture diagram | ~6–8 hrs |

**Apply to jobs from Week 1** — do not wait for the portfolio. Add the repo link once the HTTP API and README are presentable (late Week 2+).

**First concrete action:** Create the repo, install dependencies, and copy `docs/playbook/` and `docs/handbook/` from this learning-plan folder into the project.

---

## Checklist (track progress)

### Setup — repo & corpus
- [ ] Python venv + dependencies installed
- [ ] Git repo created and pushed
- [ ] `.env` with OpenAI key
- [ ] `docs/playbook/` populated (job plan, portfolio coverage, company-notes template)
- [ ] `docs/handbook/` populated (RAG, evals, tool orchestration, system design stubs)
- [ ] `src/config.py` scaffold

### P0 — RAG MVP
- [ ] Document ingestion (Markdown)
- [ ] Chunking + embeddings
- [ ] Vector store (Chroma)
- [ ] Ingest → embed → store pipeline
- [ ] RAG query path (retrieve → generate)
- [ ] Out-of-corpus refusal rules
- [ ] HTTP API (`POST /ask`)
- [ ] Source citations in answers
- [ ] Compare 2 chunk strategies (documented in README)

### P1 — Agent + evals
- [ ] Tool-calling agent (2+ tools)
- [ ] Eval harness (20–50 golden Q&A pairs)
- [ ] CI runs evals on push

### P2 — Production polish
- [ ] Docker (`docker compose up`)
- [ ] Observability (latency, tokens, retrieval scores)
- [ ] Cost notes in README
- [ ] README: architecture diagram, design decisions, eval results, next steps

---

*Reference note — saved for AI Engineer job search planning. See also: `ai-engineer-job-plan.md`.*
