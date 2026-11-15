---
type: literature
status: inbox
title: "C++ Design Patterns for Low-latency Applications Including High-frequency Trading"
authors: ["Paul Bilokon", "Burak Gunduz"]
year: 2023
venue: "arXiv 2309.04259"
url: http://arxiv.org/abs/2309.04259
pdf_url:
pdf: 00-Inbox/papers/Bilokon2023-C-Design-Patterns-for-Low-latency-d5bde1.pdf
swept: 2026-11-12
origin: baobach/hft_papers catalogue
relevance: high
tags: [arxiv, hft]
---

# C++ Design Patterns for Low-latency Applications Including High-frequency Trading

## Abstract (verbatim from arXiv)
This work aims to bridge the existing knowledge gap in the optimisation of latency-critical code, specifically focusing on high-frequency trading (HFT) systems. The research culminates in three main contributions: the creation of a Low-Latency Programming Repository, the optimisation of a market-neutral statistical arbitrage pairs trading strategy, and the implementation of the Disruptor pattern in C++. The repository serves as a practical guide and is enriched with rigorous statistical benchmarking, while the trading strategy optimisation led to substantial improvements in speed and profitability. The Disruptor pattern showcased significant performance enhancement over traditional queuing methods. Evaluation metrics include speed, cache utilisation, and statistical significance, among others. Techniques like Cache Warming and Constexpr showed the most significant gains in latency reduction. Future directions involve expanding the repository, testing the optimised trading algorithm in a live trading environment, and integrating the Disruptor pattern with the trading algorithm for comprehensive system benchmarking. The work is oriented towards academics and industry practitioners seeking to improve performance in latency-sensitive applications.

## Why staged
Auto-triaged by keyword from the baobach/hft_papers catalogue (unreviewed; quality unknown). Possible atoms: [[Latency Arbitrage]].
