---
type: literature
status: inbox
title: "Multi-Level Market Making with Reinforcement Learning"
authors: [Cheridito, Patrick, Weiss, Moritz]
year: 2026
venue: arXiv q-fin.TR (2608.18195)
url: https://arxiv.org/abs/2608.18195
pdf_url: https://arxiv.org/pdf/2608.18195
pdf: 00-Inbox/papers/Cheridito-Weiss2026-MultiLevel-MM-RL.pdf
swept: 2026-11-03
tags: [market-making, machine-learning, orderbook]
---

# Multi-Level Market Making with Reinforcement Learning

## Abstract (verbatim from arXiv)
We introduce a reinforcement learning framework for market making in a limit order book. Our algorithm aims to maximize trading revenue by dynamically submitting market and limit orders of varying sizes across multiple price levels while controlling inventory size. We use multivariate logistic-normal distributions to model order allocations and employ a deep-set encoder to aggregate features from variable-length order sets into a fixed-dimensional latent representation. Additionally, we incorporate potential-based reward shaping to accelerate learning without altering the optimal policy. We illustrate the performance of the method in three simulated market environments consisting of noise traders who submit random trades, tactical traders who respond to instantaneous volume imbalance, and strategic traders who trade in the direction of an exponentially weighted volume imbalance signal.

## Why staged
Multi-level quoting with explicit queue-position state connects [[Market Maker Inventory Control]], [[Queue Position Value]], and [[Limit Order Book Shape as Signal]]. The deep-set treatment of variable order sets is a reusable modeling idea.
