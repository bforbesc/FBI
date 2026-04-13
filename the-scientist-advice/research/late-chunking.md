# Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models

**Authors:** Günther, M., Mohr, I., Williams, D. J., Wang, B., & Xiao, H.  
**Year:** 2024  
**Venue:** arXiv:2409.04701  
**Link:** https://arxiv.org/abs/2409.04701  
**Saved:** 2026-04-08

## Summary

Introduces a novel, training-free chunking method that preserves cross-chunk context. Traditional approaches chunk first, then embed each chunk independently — losing surrounding context. Late chunking inverts this: embed the full document using a long-context embedding model, then chunk the resulting embeddings. Produces better chunk representations with measurably better retrieval quality. Works with any long-context embedding model (e.g., Jina-2), no additional training needed.

## Key findings

- Preserves contextual information lost in traditional chunk-then-embed pipelines
- Training-free — works with any existing long-context embedding model
- Better retrieval quality at the cost of longer embedding times (scales with document length)

## When to use this

When retrieval quality matters more than embedding speed, and documents are long enough that cross-chunk context is important. Not recommended when embedding throughput is the bottleneck.

## Context

Found while researching: optimal chunking strategies for RAG pipelines
