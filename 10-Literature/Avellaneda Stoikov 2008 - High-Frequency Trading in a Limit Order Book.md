---
type: literature
status: extracted
authors: [Marco Avellaneda, Sasha Stoikov]
year: 2008
venue: Quantitative Finance
url: https://www.math.nyu.edu/~avellane/HighFrequencyTrading.pdf
pdf:
tags: [market-making, optimal-control]
created: 2026-11-03
---

# Avellaneda & Stoikov (2008) — High-Frequency Trading in a Limit Order Book

## One-line summary
Optimal market-making quotes are centered on an inventory-adjusted reservation price, with spread set by volatility, risk aversion, and order-arrival intensity.

## Key contributions
- Frames market making as HJB stochastic control: maximize terminal utility over quote distances.
- Reservation price r = s − q·γ·σ²·(T−t): skew quotes linearly in inventory.
- Optimal half-spread adds a term from the exponential fill-intensity curve κ.

## Data and method
Theoretical; mid price as arithmetic Brownian motion, Poisson fills with intensity decaying exponentially in quote distance.

## Atoms extracted
- [[Market Maker Inventory Control]] — the canonical model.
- [[Bid-Ask Spread Decomposition]] — inventory component made precise.

## Critique / open questions
No adverse selection (fills are exogenous) — the real killer cost is absent; see [[Adverse Selection]]. No queue (fills are distance-only), so inapplicable as-is to large-tick books — see [[Queue Position Value]]. Guéant–Lehalle–Fernandez-Tapia (2013) give tractable asymptotics; modern treatments add flow-toxicity conditioning.
