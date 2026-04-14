# AI Signal Digest

An on-demand AI/ML newsletter digest. Run it by saying "run my digest", "latest digest", "today's digest", or similar.

## What it does

Fetches emails labeled `_AI_SIGNAL` from Gmail and synthesizes them into a clean digest covering:

- **TL;DR** — the 2-3 things that actually matter
- **Top Stories** — key developments with sources and links
- **Research Highlights** — notable papers, one sentence each
- **Industry & Engineering** — grouped by theme, no fluff
- **Data Points** — numbers worth remembering
- **Worth a Deeper Read** — 2-3 curated picks

Digests are saved to the `digests/` folder and are skimmable in under 5 minutes.

## Usage

Invoke via `SKILL.md` in Claude Cowork, or directly in Claude Code from this directory.

| What you say | What it does |
|---|---|
| "Run my digest" | Last 7 days |
| "Run my digest for last week" | Previous Mon–Sun |
| "Create a digest for last month" | Full previous month |
| "Digest for April 10th" | Single day |
| "Digest from April 1 to April 7" | Custom range |
| "Show me my digests" | Lists files in `digests/` |

## Requirements

- **Gmail MCP** connected (`mcp__claude_ai_Gmail__search_threads`, `mcp__claude_ai_Gmail__get_thread`)
- Emails labeled `_AI_SIGNAL` in Gmail

## File structure

```
ai-signal/
├── CLAUDE.md           ← this file (Claude Code + Cowork context)
├── SKILL.md            ← skill definition and instructions
└── digests/
    ├── digest-YYYY-MM-DD.html
    ├── digest-YYYY-MM-DD--YYYY-MM-DD.html
    └── digest-YYYY-MM.html
```
