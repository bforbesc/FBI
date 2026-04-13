# Is Semantic Chunking Worth the Computational Cost?

**Authors:** Qu, R., Tu, R., & Bao, F. S.  
**Year:** 2024  
**Venue:** NAACL 2025  
**Link:** https://arxiv.org/abs/2410.13070  
**Saved:** 2026-04-08

## Summary

Challenges the assumption that semantic chunking is better than fixed-size chunking for RAG. Evaluated semantic chunking across three retrieval tasks (document retrieval, evidence retrieval, answer generation) and found that the computational costs are rarely justified by performance gains. On naturally-structured documents, fixed-size chunking performed as well or better. Clustering-based semantic methods sometimes failed by misgrouping sentences, and breakpoint-based approaches created single-sentence chunks lacking context.

## Key findings

- Fixed-size token chunking matches or beats semantic chunking on typical documents
- Semantic chunking only helps in artificial scenarios with stitched documents from diverse topics
- Computational overhead of semantic chunking is rarely worth it in practice

## When to use this

Cite when someone is considering semantic chunking vs. fixed-size chunking. The answer from this paper is: start with fixed-size, only add semantic chunking if you have specific evidence it helps your data.

## Context

Found while researching: optimal chunking strategies for RAG pipelines
