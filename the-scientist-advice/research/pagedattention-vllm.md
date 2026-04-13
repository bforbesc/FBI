# Efficient Memory Management for Large Language Model Serving with PagedAttention

**Authors:** Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Yu, et al.  
**Year:** 2023  
**Venue:** SOSP 2023  
**Link:** https://arxiv.org/abs/2309.06180  
**Saved:** 2026-04-08

## Summary

Foundational paper introducing PagedAttention and the vLLM serving system. Identifies KV cache memory fragmentation as the core bottleneck in LLM serving — standard approaches waste up to 25% of GPU memory. PagedAttention borrows the paged virtual memory concept from OS design, allocating KV cache in fixed-size "pages" that can be shared and reclaimed efficiently. Combined with continuous batching, vLLM achieves 2-4x throughput improvement over HuggingFace Transformers and Orca with near-zero memory waste.

## Key findings

- Standard LLM serving wastes up to 25% of GPU memory on KV cache fragmentation
- PagedAttention solves this with OS-style virtual memory management for KV cache
- 2-4x throughput improvement over prior systems
- Continuous batching keeps GPU utilization high across variable-length requests

## When to use this

The baseline reference for any LLM serving discussion. vLLM is now the industry-standard serving system and this is the paper behind it.

## Context

Found while researching: LLM inference optimization for production low-latency serving
