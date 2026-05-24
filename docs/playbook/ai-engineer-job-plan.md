# AI Engineer Job Plan — ASAP Track

**Goal:** Land an AI Engineer / LLM Engineer / SWE (AI team) role as quickly as possible.  
**Profile:** Production LLM tool orchestration at PlaySide + full-stack (TypeScript, Python, React, Node, Flask).  
**Time budget:** ~10–15 hrs/week if employed; ~25–30 hrs/week if full-time search.

**Core strategy:** Apply from Week 1. Use PlaySide AI work as your primary qualification. Build one portfolio project to translate that into industry-standard keywords (RAG, agents, evals, vector DB, Docker).

---

## Success metrics

| Milestone | Target date | Done |
|-----------|-------------|------|
| Resume + LinkedIn updated (AI-forward) | End of Week 1 | ☐ |
| First 10 applications sent | End of Week 1 | ☐ |
| Portfolio repo started | End of Week 1 | ☐ |
| Portfolio MVP (RAG Q&A working) | End of Week 2 | ☐ |
| Portfolio complete (agent + eval + Docker) | End of Week 4 | ☐ |
| 30+ total applications | End of Week 4 | ☐ |
| First phone screens | Weeks 2–4 | ☐ |
| First technical / system-design interviews | Weeks 4–8 | ☐ |
| Offer signed | ASAP | ☐ |

---

## Target roles (apply to all of these)

**Primary (50% of applications)**
- AI Engineer
- Applied AI Engineer
- LLM Engineer
- GenAI Engineer

**Secondary (30%)**
- Software Engineer — AI / ML Platform / Developer Experience
- Full-Stack Engineer (AI product team)

**Fallback (20%)**
- Senior Software Engineer (TypeScript / Python / full-stack) — keeps options open while pivoting

**Locations:** Melbourne on-site/hybrid + remote (AU-friendly time zones + fully remote global).

---

## Positioning (use everywhere)

**One-liner:**
> Software engineer shipping production LLM tool orchestration in a shared game-engine runtime — now building and scaling LLM-powered products end-to-end.

**Keywords to mirror in resume + LinkedIn + applications:**
`LLM`, `agent`, `tool use`, `RAG`, `embeddings`, `vector search`, `prompt engineering`, `evaluation`, `TypeScript`, `Python`, `FastAPI` / `Node.js`, `Docker`, `CI/CD`, `production`

---

## Portfolio project spec

Build **one** repo — **`ai-job-copilot`** — that bridges PlaySide experience → what recruiters grep for.

### Elevator pitch

Personal RAG assistant over your **job-search playbook** and **AI engineering study handbook** — with FastAPI, source citations, eval harness, tool-calling agent, and Docker.

**One-sentence description (README / applications):**

> A personal RAG assistant over my job-search playbook and AI engineering study notes, with evals to verify answers stay grounded in that material.

### Corpus (what gets indexed)

Two folders under `docs/` — one app searches both:

| Folder | Purpose | Examples |
|--------|---------|----------|
| **`docs/playbook/`** | Operational job-search notes | Job plan, portfolio checklist, company research, interview debriefs |
| **`docs/handbook/`** | AI concepts you're learning | RAG, evals, tool orchestration, system design notes |

The corpus grows as you job-search and study. Eval questions mix practical (*"What's missing from my portfolio?"*) and conceptual (*"What are the RAG pipeline steps?"*).

**Optional later:** add `docs/project/` or index the repo README for a codebase-assistant angle (`get_file_snippet` tool). Not required for MVP.

### Must-have features (MVP → complete)

| Priority | Feature | Notes |
|----------|---------|-------|
| P0 | Document ingestion | Markdown; recursive load from `docs/playbook/` and `docs/handbook/` |
| P0 | Chunking + embeddings | Compare 2 strategies in README (fixed-size vs paragraph) |
| P0 | Vector store | Chroma (local) — document why in README |
| P0 | RAG Q&A endpoint | `POST /ask` — retrieve → synthesize with citations |
| P1 | Tool-calling agent | At least 2 tools: e.g. `search_playbook`, `search_handbook` |
| P1 | Eval harness | 20–50 golden Q&A pairs; script reports retrieval hit rate + answer match |
| P1 | CI | GitHub/GitLab CI runs evals on push (even if threshold is loose at first) |
| P2 | Docker | `docker compose up` runs API + vector DB |
| P2 | Observability | Log latency, token usage, retrieval scores per request |
| P2 | Cost notes | README section: $/1k queries estimate |

### Tech stack (recommended)
- **Language:** Python (FastAPI) — matches most AI Engineer JDs; optional thin Node client for demo
- **LLM:** OpenAI or Anthropic API (free tier / low cost for portfolio)
- **Embeddings:** OpenAI `text-embedding-3-small` or open model via Hugging Face
- **Vector DB:** Chroma (fastest to ship) or pgvector (shows DB skill)
- **Agent:** Raw API tool-calling first; optional LangChain/LlamaIndex mention in README if you use it
- **Eval:** pytest or standalone script; store golden set as JSON

### README sections (recruiters read this, not every file)
1. Problem + approach (3 sentences)
2. Architecture diagram (ASCII or Mermaid)
3. Quick start (`docker compose up`)
4. Design decisions (chunk size, embedding model, why RAG vs fine-tuning)
5. Eval methodology + sample results
6. Tradeoffs & next steps (caching, reranking, human feedback loop)

### What NOT to over-build
- Fancy frontend (CLI or Swagger UI is enough)
- Multiple embedding providers
- Custom model training
- Kubernetes (Docker is enough for portfolio)

### Suggested repo structure
```
ai-job-copilot/
├── README.md
├── .gitignore
├── .env.example
├── requirements.txt
├── docker-compose.yml          # Week 4
├── Dockerfile                  # Week 4
├── .github/workflows/eval.yml  # Week 3
├── docs/
│   ├── playbook/
│   │   ├── ai-engineer-job-plan.md
│   │   ├── portfolio-coverage.md
│   │   ├── company-notes/
│   │   └── interview-debriefs/
│   └── handbook/
│       ├── rag-pipeline.md
│       ├── evals-basics.md
│       ├── llm-tool-orchestration.md
│       └── system-design-template.md
├── data/
│   ├── chroma/                 # gitignored — local vector index
│   └── golden_eval.json        # Week 2+
└── src/
    ├── config.py
    ├── load_docs.py
    ├── chunk.py
    ├── embed.py
    ├── store.py
    ├── retrieve.py
    ├── rag.py
    ├── ingest.py
    ├── api.py
    ├── agent.py
    └── eval_runner.py
```

### Sample golden eval entries
```json
{
  "question": "What P1 items are missing from my portfolio?",
  "expected_sources": ["portfolio-coverage.md"],
  "expected_answer_contains": ["tool-calling agent", "eval harness", "CI"]
}
```
```json
{
  "question": "What are the steps in a RAG pipeline?",
  "expected_sources": ["rag-pipeline.md"],
  "expected_answer_contains": ["chunk", "embed", "retrieve"]
}
```

---

## Week-by-week checklist

### Week 1 — Launch (apply + position + start project)

**Job search**
- [ ] Rewrite resume: lead with AI/LLM section (see [Resume tweaks](#resume-tweaks) below)
- [ ] Update LinkedIn headline: e.g. `Software Engineer | Production LLM agents & tool orchestration | TypeScript · Python`
- [ ] Add 3–5 AI bullets to LinkedIn experience (mirror resume)
- [ ] Set LinkedIn "Open to work" (recruiter-visible if preferred)
- [ ] Save 10 LinkedIn job alerts: "AI Engineer", "LLM Engineer", "Applied AI", "GenAI" + Melbourne/Remote
- [ ] Apply to **5–10 roles** (do not wait for portfolio)
- [ ] Message 3 people: ex-colleague, recruiter, or USC/alumni for referrals or sanity check

**Learning**
- [ ] Complete one short RAG course (see [Resources](#resources))
- [ ] Skim 5 real JDs; list top 10 repeated keywords in a note
- [ ] Create `ai-job-copilot` repo; scaffold `docs/playbook/`, `docs/handbook/`, and `src/`
- [ ] Implement ingest + chunk + embed + store (P0)

**Deliverable:** Resume live, 5+ applications, repo with embeddings pipeline working.

---

### Week 2 — RAG MVP + volume applications

**Job search**
- [ ] Apply to **8–10 roles** (customize first paragraph per JD)
- [ ] Respond to all recruiter InMails within 24h
- [ ] Track applications in spreadsheet: company, role, date, status, keywords

**Learning / project**
- [ ] Finish `POST /ask` RAG endpoint with source citations
- [ ] Write 20 golden eval questions from playbook + handbook corpus
- [ ] Run eval v1 manually; record baseline scores in README
- [ ] Compare 2 chunk sizes; document winner in README

**Interview prep**
- [ ] Prepare 2-min "tell me about yourself" (AI-forward)
- [ ] Prepare STAR story: production LLM skill iteration at PlaySide
- [ ] Prepare STAR story: technical tradeoff (correctness vs velocity in shared runtime)

**Deliverable:** Working RAG demo + eval baseline + 15+ cumulative applications.

---

### Week 3 — Agent layer + system design prep

**Job search**
- [ ] Apply to **8–10 roles**
- [ ] Follow up on Week 1 applications (LinkedIn or email)
- [ ] Post on LinkedIn: short note on what you're building (optional but helps visibility)

**Learning / project**
- [ ] Add tool-calling agent (2+ tools) on top of RAG
- [ ] Add structured logging: latency, tokens, retrieval score
- [ ] Start eval in CI (GitHub Actions or GitLab CI)
- [ ] Draft architecture diagram for README

**Interview prep**
- [ ] Study one LLM system design walkthrough (see Resources)
- [ ] Practice out loud: "Design a customer support bot over internal docs" (10 min)
- [ ] Refresh: when RAG vs fine-tuning vs prompt-only

**Deliverable:** Agent works end-to-end; 25+ cumulative applications.

---

### Week 4 — Ship portfolio + polish story

**Job search**
- [ ] Apply to **8–10 roles** — **link portfolio repo in every AI application**
- [ ] Target 2–3 consultancies/SIs (often faster hiring for AI project work)
- [ ] Ask 1 contact for referral to a specific company on your list

**Learning / project**
- [ ] Dockerize (`docker compose up` works from clean clone)
- [ ] Expand golden set to 30–50 questions
- [ ] Complete README (all sections from spec)
- [ ] Add pin to GitHub profile; link from LinkedIn Featured

**Interview prep**
- [ ] Mock: walk through portfolio architecture in 5 min
- [ ] Mock: "What would you improve with another 2 weeks?"
- [ ] Keep coding practice: 3 LeetCode medium (SWE rounds still happen)

**Deliverable:** Portfolio **done**; 35+ cumulative applications; ready for technical rounds.

---

### Week 5 — Fine-tuning touch + interview mode

**Job search**
- [ ] Apply to **5–8 roles** (quality > quantity if interviews are active)
- [ ] Prioritize follow-ups and scheduling over new apps if pipeline is hot
- [ ] Consider contract/freelance AI listings (shorten time-to-income)

**Learning**
- [ ] Run one LoRA fine-tune on a tiny dataset (Hugging Face + `peft`) — notebook OK
- [ ] Write 5 sentences in README or LinkedIn: when you'd choose fine-tune vs RAG
- [ ] Fill gaps from any interview feedback received

**Interview prep**
- [ ] ML concepts drill: transformers, attention, context window, embeddings (1 hr)
- [ ] System design: add caching, rate limits, fallback model, PII handling to your bot design
- [ ] Prepare question for interviewers: "How do you evaluate LLM features in production?"

**Deliverable:** Can explain fine-tuning vs RAG; actively interviewing or in deep follow-up.

---

### Week 6 — Double down on weak spots

**Job search**
- [ ] Apply to **5–8 roles** if pipeline < 3 active processes
- [ ] Revisit rejected applications: pattern in role level or keywords?
- [ ] Expand to remote US/EU companies open to AU hours

**Learning**
- [ ] Complete "Evaluating AI Agents" or equivalent short course
- [ ] Optional: add reranking or hybrid search to portfolio (BM25 + vector) — strong differentiator
- [ ] Optional: DeepLearning.AI "AI Agentic Design Patterns" certificate → LinkedIn

**Interview prep**
- [ ] Take-home template: reuse portfolio modules to timebox future homework
- [ ] Document PlaySide AI work metrics if you can (even directional: "reduced retry rate")

**Deliverable:** 45+ lifetime applications; 2+ interview processes in flight (target).

---

### Week 7 — Close loops

**Job search**
- [ ] Focus on advancing final-round candidates
- [ ] Negotiation prep: comp research (Levels.fyi, Glassdoor AU, Seek salary)
- [ ] If no interviews yet: resume review with 1 senior engineer or recruiter; adjust keywords

**Learning**
- [ ] Only study what upcoming interviews require (company-specific)
- [ ] Light coding maintenance (1–2 problems/week)

**Interview prep**
- [ ] Behavioral: conflict, production incident, mentoring, stakeholder pushback
- [ ] Prepare questions about team maturity: eval culture, on-call, model choice ownership

**Deliverable:** At least one late-stage process or clear diagnosis of blocker.

---

### Week 8 — Sustain pipeline until offer

**Job search**
- [ ] Do not stop applying until **signed offer**
- [ ] Weekly: 3–5 applications + all follow-ups
- [ ] Consider broadening to "Platform Engineer" or "Developer Tools" if AI title bar is too high

**Reflect**
- [ ] What interview topics repeated? Add to study doc.
- [ ] Update portfolio README with anything you explained in interviews
- [ ] Refresh LinkedIn with "Built X" post linking repo

**Deliverable:** Offer signed OR repeatable weekly machine that keeps pipeline full.

---

## Resume tweaks

Move AI work to the top of PlaySide (or add a **Selected AI engineering** block before experience):

**Suggested bullets (customize with your numbers):**
- Design and maintain modular LLM "skill" files that orchestrate game-engine tools for agent-style workflows in production (level/content generation, configuration), enabling repeatable tool use without ad-hoc prompting.
- Iterate skill specs from production failure modes — tightening tool selection, ordering, and constraints (production prompt/instruction tuning).
- Shape TypeScript architecture so codebases remain interpretable and safely modifiable by an embedded AI assistant (module boundaries, consistent patterns, regression risk reduction).
- Ship in a high-change multi-team environment (shared runtime, proprietary engine, major tech partner).

**Skills line to add:**
`LLM agents · tool use · prompt engineering · RAG · embeddings · evaluation · TypeScript · Python · FastAPI · Node.js · Docker · CI/CD`

---

## Application tracker (copy to spreadsheet)

| Company | Role | Date applied | Source | Keywords from JD | Status | Next action | Notes |
|---------|------|--------------|--------|------------------|--------|-------------|-------|
| | | | | | Applied | | |
| | | | | | Phone screen | | |
| | | | | | Technical | | |
| | | | | | Final | | |
| | | | | | Rejected | | |
| | | | | | Offer | | |

---

## Interview cheat sheet

### Tell me about yourself (~2 min)
1. Current: SWE II at PlaySide — production LLM agent/tool orchestration for game engine  
2. Before: full-stack at Luma (React, Flask, MariaDB) — delivery end-to-end  
3. Now: extending into standard LLM product stack (RAG, evals, deployment) via **ai-job-copilot**  
4. Looking for: AI Engineer role building production LLM systems

### Likely technical topics
- RAG pipeline: ingest → chunk → embed → retrieve → generate  
- Chunk size tradeoffs; metadata filtering; hybrid search  
- Agent design: tool schemas, error handling, max steps  
- Evals: golden sets, retrieval metrics, regression in CI  
- Production: latency, cost, caching, fallbacks, observability, PII  
- RAG vs fine-tuning vs prompt engineering — decision framework  

### STAR stories to prepare (minimum 4)
1. Production LLM skill iteration — missed behavior → fixed spec → outcome  
2. Architecture for AI-modifiable codebase — decision and result  
3. Full-stack delivery — Luma Gantt or Flask/React feature end-to-end  
4. Leadership — pod lead, MR review, or EM support under organizational friction  

### Questions to ask them
- How do you evaluate LLM features before and after launch?  
- Who owns prompts, retrieval, and model selection?  
- What does on-call look like for AI features?  
- Biggest failure mode in your current LLM stack?

---

## Resources

### Short courses (high ROI, fast)
| Resource | Focus | Link |
|----------|-------|------|
| DeepLearning.AI — Retrieval Augmented Generation (RAG) | RAG fundamentals | https://www.deeplearning.ai/short-courses/ |
| DeepLearning.AI — Building and Evaluating Advanced RAG | Advanced RAG + eval | https://www.deeplearning.ai/short-courses/ |
| DeepLearning.AI — AI Agents in LangGraph | Agent patterns | https://www.deeplearning.ai/short-courses/ |
| DeepLearning.AI — Evaluating AI Agents | Agent evals | https://www.deeplearning.ai/short-courses/ |
| DeepLearning.AI — Fine-Tuning LLMs | LoRA / fine-tuning | https://www.deeplearning.ai/short-courses/ |
| Fast.ai — Practical Deep Learning | PyTorch + ML intuition (optional deeper) | https://course.fast.ai/ |

Browse all short courses: https://www.deeplearning.ai/courses/

### Docs & references
| Resource | Focus | Link |
|----------|-------|------|
| OpenAI — Function calling / tools | Agent tool use | https://platform.openai.com/docs/guides/function-calling |
| Anthropic — Tool use | Agent tool use | https://docs.anthropic.com/en/docs/build-with-claude/tool-use |
| Simon Willison's blog | LLM engineering practice | https://simonwillison.net/ |
| LlamaIndex docs | RAG patterns | https://docs.llamaindex.ai/ |
| Chroma docs | Vector DB quick start | https://docs.trychroma.com/ |
| Hugging Face — PEFT / LoRA | Fine-tuning | https://huggingface.co/docs/peft |
| Jay Alammar — The Illustrated Transformer | Transformer intuition | https://jalammar.github.io/illustrated-transformer/ |

### System design
| Resource | Focus | Link |
|----------|-------|------|
| Eugene Yan — Patterns for LLM apps | Production patterns | https://eugeneyan.com/writing/llm-patterns/ |
| Latent Space (podcast/newsletter) | Industry landscape | https://www.latent.space/ |

### Job boards
| Board | Link |
|-------|------|
| LinkedIn Jobs | https://www.linkedin.com/jobs/ |
| Seek (AU) | https://www.seek.com.au/ |
| Wellfound (startups) | https://wellfound.com/ |
| Otta | https://otta.com/ |
| HN Who's Hiring (monthly) | https://news.ycombinator.com/ |

### Coding interview (still required at many companies)
| Resource | Link |
|----------|------|
| LeetCode (medium focus) | https://leetcode.com/ |
| NeetCode roadmap | https://neetcode.io/roadmap |

---

## Weekly rhythm (template)

**Mon (1 hr):** Job alerts review; apply to 2 roles  
**Tue (2 hrs):** Project / learning block  
**Wed (1 hr):** Apply to 2 roles; recruiter follow-ups  
**Thu (2 hrs):** Project / learning block  
**Fri (1 hr):** Interview prep or eval run; update tracker  
**Sat (optional 2 hrs):** Deep project or take-home  
**Sun:** Off (avoid burnout — sustained search beats sprint-and-crash)

---

## If things aren't working by Week 6

**Resume not getting callbacks**
- A/B test headline and first 3 bullets  
- Lead with "LLM" / "agent" in title line  
- Get 1 recruiter feedback on resume  

**Callbacks but failing technical**
- Map each failure to a topic; study only that for 1 week  
- Do mock interviews (Pramp, friend, or record yourself)  

**Callbacks but "not enough ML"**
- Emphasize Applied AI / LLM Engineer roles, not Research ML  
- Add fine-tuning notebook + eval metrics to portfolio  
- Target product companies over pure research labs  

**No time to build**
- Apply heavily as "SWE with production LLM experience" now  
- Ship minimal portfolio: RAG endpoint + 10 eval questions + README (Weekend 1)  

---

## Notes / learnings (fill in as you go)

**JD keywords I see most often:**
1.  
2.  
3.  

**Interview topics that came up:**
1.  
2.  

**What worked in applications:**
-  

**What to improve:**
-  

---

*Last updated: May 2026 — revisit weekly and check off milestones.*
