# The Scientist's Advice

A research-backed assistant for data engineers, ML engineers, and data scientists. Every answer is grounded in real published papers — not conventional wisdom or vibes.

## What it does

- Searches academic sources (arXiv, Semantic Scholar, Papers With Code, Hugging Face Papers) before answering
- Prioritizes recent, well-cited papers from reputable venues
- Translates findings into plain language and actionable recommendations
- Saves interesting papers to the workspace with plain-language summaries

## Usage

Invoke via `SKILL.md` in Claude Cowork, or directly in Claude Code from this directory.

Ask anything in these areas and it will search for research first:

- RAG, embeddings, chunking, retrieval
- LLM fine-tuning, prompt engineering, agents
- Model serving, vector DBs, MLOps, feature stores
- Data engineering: Spark, dbt, Kafka, data quality
- Statistical methods, A/B testing, causal inference

Say **"research this"**, **"what does the research say about X"**, or **"find papers on X"** to trigger explicitly.

## Saving papers

Say **"save that paper"** and the assistant will:
1. Create a plain-language summary in `research/[paper-name].md`
2. Append an entry to `research-log.md`

## Customizing

Edit `config.md` to change scope, sources, and tone. No need to touch `SKILL.md`.

## File structure

```
the-scientist-advice/
├── CLAUDE.md         ← this file (Claude Code + Cowork context)
├── SKILL.md          ← skill definition and instructions
├── config.md         ← customize scope, sources, and tone
├── research-log.md   ← chronological log of all saved papers
└── research/         ← paper summaries, one file per paper
```
