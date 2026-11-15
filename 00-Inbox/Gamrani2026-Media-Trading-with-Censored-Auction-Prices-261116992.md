---
type: literature
status: inbox
title: "Media Trading with Censored Auction Prices: A Stochastic Control and Reinforcement Learning Approach"
authors: ["Yun-Ithry Gamrani", "Huyên Pham"]
year: 2026
venue: "arXiv q-fin.MF (2611.16992)"
url: https://arxiv.org/abs/2611.16992
pdf_url: https://arxiv.org/pdf/2611.16992
pdf: 00-Inbox/papers/Gamrani2026-Media-Trading-with-Censored-Auction-Prices-261116992.pdf
swept: 2026-11-15
posted: 2026-11-12
origin: daily sweep script
relevance: medium
tags: [auctions]
---

# Media Trading with Censored Auction Prices: A Stochastic Control and Reinforcement Learning Approach

## Abstract (verbatim from arXiv)
In real-time bidding, marketing agencies must balance campaign performance, transaction margins and the use of a finite advertising budget. A key difficulty is that market-clearing prices are typically observed only when bids are successful, so the information available for subsequent decisions depends on the bidding policy. We formulate this problem using a continuous-time stochastic control model with a latent price process. To construct a price signal, we consider parallel exploratory subcampaigns in which bids are randomized subject to an upper bound. Under a stylized cross-sectional sampling model, the resulting price estimator is consistent and satisfies a mean-square error bound of order $N^{-1}$, where $N$ is the number of exploratory observations. We then describe a model-based approach combining forward-equation calibration with Hamilton-Jacobi-Bellman policy iteration and a physics-informed neural network, alongside an entropy-regularized actor-critic approach based on observable information in a model-free setting. Synthetic experiments illustrate the estimator and the computational procedures. The framework clarifies the decision and information trade-offs faced by the agency, while distinguishing full-information benchmarks and estimated-price policies from the genuinely partially observed control problem.

## Why staged
Auto-staged by the daily sweep (keyword filter, unreviewed). Possible related notes: [[Opening and Closing Auctions]].
