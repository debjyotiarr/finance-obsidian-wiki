---
type: literature
status: inbox
title: "Multi-Level Market Making with Reinforcement Learning"
authors: [Cheridito, Patrick, Weiss, Moritz]
year: 2026
venue: arXiv q-fin.TR (2608.18195)
url: https://arxiv.org/abs/2608.18195
pdf_url: https://arxiv.org/pdf/2608.18195
pdf:
swept: 2026-11-03
tags: [market-making, machine-learning, orderbook]
---

# Multi-Level Market Making with Reinforcement Learning

## Abstract (summarized — arxiv.org unreachable from this environment; verify at url)
RL framework for LOB market making with market and limit orders of varying sizes across several price levels. State includes the full book, queue positions, and past order flow. Order allocations modeled with multivariate logistic-normal distributions; a deep-set encoder turns variable-length order sets into fixed-size representations; potential-based reward shaping speeds learning without changing the optimal policy. Reported to outperform benchmarks in three simulated environments. ETH Zurich; submitted 2026-08-18.

## Why staged
Multi-level quoting with explicit queue-position state connects [[Market Maker Inventory Control]], [[Queue Position Value]], and [[Limit Order Book Shape as Signal]]. The deep-set treatment of variable order sets is a reusable modeling idea.
