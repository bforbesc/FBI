# ML Research Log

A running record of papers found and saved during research sessions.

---

## How to use this log

Each entry links to a paper summary in `papers/`. Entries are added chronologically as you research.
Ask me to "save that paper" at any point and I'll add it here and create an individual summary file.

---

## 2026-04-08

**Question:** Optimal chunking strategies for RAG pipelines (per page, paragraph, token window?)

- [Is Semantic Chunking Worth the Computational Cost?](research/is-semantic-chunking-worth-it.md) — NAACL 2025. Fixed-size chunking matches or beats semantic chunking in most real-world cases.
- [Late Chunking: Contextual Chunk Embeddings](research/late-chunking.md) — arXiv 2024. Embed full doc first, chunk afterward — preserves context, better retrieval quality.

**Question:** Best embedding model for technical documentation in a vector DB

- *(no papers saved — see session notes: Voyage-3-large recommended, MTEB benchmark is the reference)*

**Question:** LLM inference optimization for low-latency production serving

- [PagedAttention / vLLM](research/pagedattention-vllm.md) — SOSP 2023. Foundational paper behind vLLM. 2-4x throughput via OS-style KV cache memory management.
