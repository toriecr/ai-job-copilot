# Evals Basics

**Evals** = **evaluations**: repeatable checks that your LLM/RAG system behaves correctly — not just "it looked fine when I tried one question."

Regular tests assert `add(2, 2) == 4`. LLM outputs are fuzzy, so evals check **patterns of good behavior** instead.

---

## What evals check

| Check type | Question it answers | Example |
|------------|---------------------|---------|
| **Retrieval** | Did the right doc/chunk get retrieved? | Question about portfolio gaps → `portfolio-coverage.md` in top-k |
| **Answer quality** | Does the answer include expected facts? | Answer mentions "eval harness" and "CI" |
| **Grounding** | Did it stay within retrieved context? | No invented company names or dates |
| **Refusal** | For out-of-corpus questions, did it decline? | "Capital of France?" → "not in my documents" |
| **Regression** | After a change, did scores get worse? | Re-run evals after tweaking chunk size or prompt |

---

## Retrieval vs answer checks

**Retrieval eval** — did search find the right source?

```json
{
  "question": "What P1 items are missing from my portfolio?",
  "expected_sources": ["portfolio-coverage.md"]
}
```

Pass if any retrieved chunk's metadata matches an expected source file.

**Answer eval** — did the final text contain what you expect?

```json
{
  "question": "What P1 items are missing from my portfolio?",
  "expected_answer_contains": ["tool-calling agent", "eval harness", "CI"]
}
```

Pass if the answer (case-insensitive) includes those phrases.

You usually want **both**: good retrieval but bad prompting still fails; good prompt with wrong retrieval means lucky guessing.

---

## Golden dataset + harness

1. Create `data/golden_eval.json` — 20–50 questions you care about
2. `eval_runner.py` runs each question through the pipeline
3. Score: e.g. **18/20 passed**
4. Run in CI on every push → catch regressions early

Evals are **not** training a model or academic leaderboards. For a portfolio, **20–50 good questions** is enough.

---

## Why recruiters care

Anyone can demo one good ChatGPT answer. Evals show you think like an engineer: define expected behavior, measure it, catch regressions when you tweak prompts or chunking.

---

## Related files

- `rag-pipeline.md` — what you're evaluating

---

*Stub — flesh out golden questions as you finish Step 2.*
