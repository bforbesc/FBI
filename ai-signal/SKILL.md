---
name: ai-signal
description: >
  On-demand AI/ML newsletter digest for data scientists and ML engineers. Use this skill
  whenever the user says "run my digest", "latest digest", "today's digest", "digest for last week",
  "show me my digests", or asks to create or view a digest for a specific date or range.
  Also trigger on phrases like "what happened in AI this week", "catch me up on ML news",
  "what did I miss in AI", or any request to summarize recent AI/ML news from Gmail.
compatibility: "Requires Gmail MCP tools: mcp__claude_ai_Gmail__search_threads, mcp__claude_ai_Gmail__get_thread"
---

# AI Signal Digest

## What this is
On-demand AI/ML digest for a data scientist / ML engineer. Run it by saying "run my digest" or similar.

## Step 1 — Determine date window
Parse the user's request to determine the date range before querying Gmail.

**Default (no date specified):** last 7 days ending today.

**Supported phrases and how to resolve them:**
- "run my digest" / "latest" → last 7 days
- "today" → today only
- "yesterday" → yesterday only
- "this week" → Monday–today of the current ISO week
- "last week" → Monday–Sunday of the previous ISO week
- "this month" → 1st of current month to today
- "last month" → full previous calendar month
- "April" / "April 2025" → full named month
- "YYYY-MM-DD" → that single day
- "from X to Y" → explicit range

**Gmail query template:**
```
label:_AI_SIGNAL after:YYYY/MM/DD before:YYYY/MM/DD
```
Always compute concrete `after` / `before` dates before querying.

## Step 2 — Fetch
Run the Gmail query from Step 1. Read the **full content** of every matching thread (all messages in each thread). This is the only data source — do not use web search or external knowledge.

## Step 3 — Digest structure
**File naming:**
- Single day: `digests/digest-YYYY-MM-DD.html`
- Week range: `digests/digest-YYYY-MM-DD--YYYY-MM-DD.html`
- Full month: `digests/digest-YYYY-MM.html`

Sections:
1. **TL;DR** — 2-3 sentences, most important things in the period
2. **Top Stories** — 3-5 items, 2-3 sentence summary each, with source + link
3. **Research Highlights** — papers only: title (linked) · first author et al. · one sentence. No abstracts.
4. **Industry & Engineering** — short cards grouped by theme, 2-3 lines each
5. **Data Points** — stat chip grid: number + label + source only
6. **Worth a Deeper Read** — 2-3 picks, one sentence on why

## Step 4 — Browse existing digests
If the user asks to "show", "open", or "find" a past digest, check `digests/` for a matching file by date before re-running a fetch. List available digests if the user asks what's been generated.

## Format rules
- Dark background, clean inline CSS, mobile-friendly
- Skimmable in under 5 minutes
- Specifics only: model names, version numbers, metric scores
- No abstracts, no fluff, no repeated facts across sections
- Include the date range covered in the digest header
