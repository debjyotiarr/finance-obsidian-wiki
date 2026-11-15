---
type: literature
status: inbox
title: "End-to-End Policy Learning of A Statistical Arbitrage Autoencoder Architecture"
authors: ["Fabian Krause", "Jan-Peter Calliess"]
year: 2024
venue: "arXiv 2402.08233"
url: http://arxiv.org/abs/2402.08233
pdf_url:
pdf: 00-Inbox/papers/Krause2024-End-to-End-Policy-Learning-of-f6f77f.pdf
swept: 2026-11-12
origin: baobach/hft_papers catalogue
relevance: medium
tags: [arxiv, stat-arb]
---

# End-to-End Policy Learning of A Statistical Arbitrage Autoencoder Architecture

## Abstract (verbatim from arXiv)
In Statistical Arbitrage (StatArb), classical mean reversion trading strategies typically hinge on asset-pricing or PCA based models to identify the mean of a synthetic asset. Once such a (linear) model is identified, a separate mean reversion strategy is then devised to generate a trading signal. With a view of generalising such an approach and turning it truly data-driven, we study the utility of Autoencoder architectures in StatArb. As a first approach, we employ a standard Autoencoder trained on US stock returns to derive trading strategies based on the Ornstein-Uhlenbeck (OU) process. To further enhance this model, we take a policy-learning approach and embed the Autoencoder network into a neural network representation of a space of portfolio trading policies. This integration outputs portfolio allocations directly and is end-to-end trainable by backpropagation of the risk-adjusted returns of the neural policy. Our findings demonstrate that this innovative end-to-end policy learning approach not only simplifies the strategy development process, but also yields superior gross returns over its competitors illustrating the potential of end-to-end training over classical two-stage approaches.

## Why staged
Auto-triaged by keyword from the baobach/hft_papers catalogue (unreviewed; quality unknown). Possible atoms: [[Pairs Trading and Statistical Arbitrage]].
