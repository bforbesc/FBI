# AI Signal Digest

A personal, on-demand AI/ML newsletter digest — built for a data scientist / ML engineer who wants to stay current without the noise.

## How it works

Emails tagged with the Gmail label `_AI_SIGNAL` are fetched, read in full, and synthesized into a clean, dark-themed HTML digest covering:

- **TL;DR** — the 2-3 things that actually matter
- **Top Stories** — key developments with sources and links
- **Research Highlights** — notable papers, one sentence each
- **Industry & Engineering** — grouped by theme, no fluff
- **Data Points** — numbers worth remembering
- **Worth a Deeper Read** — 2-3 curated picks

Digests are saved to the `digests/` folder and are skimmable in under 5 minutes.

## Usage

This is a **Claude Cowork skill**. Add `SKILL.md` to your Claude Cowork workspace, then tell Claude what you want:

| What you say | What it does |
|---|---|
| "Run my digest" | Last 7 days |
| "Run my digest for last week" | Previous Mon–Sun |
| "Create a digest for last month" | Full previous month |
| "Digest for April 10th" | Single day |
| "Digest from April 1 to April 7" | Custom range |
| "Show me my digests" | Lists files in `digests/` |

## File structure

```
ai-signal/
├── README.md           ← this file
├── SKILL.md            ← Claude Cowork skill definition and instructions
└── digests/
    ├── digest-YYYY-MM-DD.html              # single day
    ├── digest-YYYY-MM-DD--YYYY-MM-DD.html  # date range / week
    └── digest-YYYY-MM.html                 # full month
```

## Requirements

- **Gmail MCP** connected in Claude Cowork (`mcp__claude_ai_Gmail__search_threads`, `mcp__claude_ai_Gmail__get_thread`)
- Emails labeled `_AI_SIGNAL` in your Gmail account
