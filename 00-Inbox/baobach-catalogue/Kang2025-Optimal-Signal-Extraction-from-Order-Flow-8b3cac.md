---
type: literature
status: inbox
title: "Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure"
authors: ["Sungwoo Kang"]
year: 2025
venue: "arXiv 2512.18648"
url: http://arxiv.org/abs/2512.18648
pdf_url:
pdf: 00-Inbox/papers/Kang2025-Optimal-Signal-Extraction-from-Order-Flow-8b3cac.pdf
swept: 2026-11-12
origin: baobach/hft_papers catalogue
relevance: high
tags: [arxiv, microstructure, orderflow]
---

# Optimal Signal Extraction from Order Flow: A Matched Filter Perspective on Normalization and Market Microstructure

## Abstract (verbatim from arXiv)
We establish a general matched filter principle for order flow normalization: optimal normalization must match the scaling behaviour of the signal-generating process. For capacity-constrained institutional investors, market capitalization normalization ($S^{MC}$) is the matched filter; for volume-targeting traders (e.g., VWAP/TWAP algorithms), trading value normalization ($S^{TV}$) is optimal. Monte Carlo simulations confirm this principle works bidirectionally, with matched filters achieving up to $1.99\times$ higher signal correlation. Empirical validation using 2.7 million stock-day observations from the Korean market (2020--2024) reveals symmetric normalization dominance across investor types: domestic institutional flows predict next-day returns significantly under $S^{MC}$ ($t = 9.65$), while foreign flows exhibit stronger predictability under $S^{TV}$ ($t = 16.35$) -- with no sign reversal at longer horizons, indicating durable private information rather than temporary price impact. These findings motivate the ``Informed Executor'' hypothesis: sophisticated foreign investors possess genuine private information but employ volume-targeting algorithms for stealth execution -- volume-scaling reflects execution methodology, not absence of information. Information-theoretic validation using KL divergence independently corroborates these results. The matched filter principle generalises to any market where signal scaling varies across trader types, with implications for trading algorithms, factor construction, and market microstructure methodology.

## Why staged
Auto-triaged by keyword from the baobach/hft_papers catalogue (unreviewed; quality unknown). Possible atoms: [[Order Flow Imbalance]], [[Microstructure Noise and Price Discovery]].
