---
type: literature
status: inbox
title: "Delta-Vega Hedging with Deep Reinforcement Learning: From Simulation to Reality"
authors: ["Michele Colombi", "Marco Di Francesco", "Pietro Rossi"]
year: 2026
venue: "arXiv q-fin.CP (2611.32790)"
url: https://arxiv.org/abs/2611.32790
pdf_url: https://arxiv.org/pdf/2611.32790
pdf: 00-Inbox/papers/Colombi2026-Delta-Vega-Hedging-with-Deep-Reinforcement-261132790.pdf
swept: 2026-11-25
posted: 2026-11-24
origin: daily sweep script
relevance: medium
tags: [execution]
---

# Delta-Vega Hedging with Deep Reinforcement Learning: From Simulation to Reality

## Abstract (verbatim from arXiv)
Hedging an option portfolio with the underlying asset alone leaves the position exposed to changes in volatility, which can be managed by trading another derivative, at higher transaction costs. We propose a deep reinforcement learning approach to hedge both price and volatility risk under discrete-time trading and transaction costs, by trading the underlying asset and a second, longer-dated option. We train the agent with Proximal Policy Optimization (PPO) on synthetic data from a stochastic volatility model, and restrict its state to quantities observable in the market, so that the policy learned in simulation applies directly to market data. In simulation, we validate the policy against semi-analytical Delta and Delta-Vega hedging benchmarks. PPO matches Delta-Vega's objective at baseline transaction costs and increasingly outperforms it as costs rise, with both two-instrument strategies consistently outperforming the single-instrument Delta hedge. On historical S&P 500 index option data, we benchmark our approach against practitioner Black-Scholes Delta and Delta-Vega hedging strategies. The two-instrument strategies roughly halve the profit-and-loss dispersion of the Delta hedge, and PPO attains a lower profit-and-loss volatility than Delta-Vega at comparable transaction costs. PPO holds more of the hedging option than Delta-Vega, in line with the stochastic-volatility model hedge, and its advantage is concentrated in high-volatility episodes.

## Why staged
Auto-staged by the daily sweep (keyword filter, unreviewed). Possible related notes: [[Implementation Shortfall]].
