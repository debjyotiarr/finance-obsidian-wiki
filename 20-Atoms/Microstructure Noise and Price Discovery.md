---
type: atom
status: seed
domain: microstructure
assets: [equities, futures]
tags: [measurement, modeling, price-discovery]
created: 2026-11-03
---

# Microstructure Noise and Price Discovery

**Idea.** Observed trade prices = efficient price + noise (bid-ask bounce, discreteness, temporary impact). At high frequencies the noise dominates: naive realized variance explodes as sampling frequency rises (the volatility signature plot). Separating the efficient-price component from noise is the core estimation problem beneath most microstructure signals.

**Tools.**
- Roll (1984) spread estimator: spread from negative first-order autocovariance of price changes.
- Hasbrouck's VECM/information-share machinery: which market/venue impounds information first — the formal backbone of [[Futures-ETF Lead-Lag]] and [[Cross-Venue Fragmentation]] analysis.
- Realized kernels, pre-averaging, and two-scale estimators recover efficient-price variance from tick data — feeds [[Realized Volatility Forecasting]].

**Practical notes.**
- Any signal built on raw trade prices at tick frequency partially trades bid-ask bounce against itself; build on mid or [[Microprice]] instead.
- The noise *is* someone's income: its structure (spread, impact decay) is the market maker's revenue model seen from the other side.

**Related.** [[Microprice]], [[Realized Volatility Forecasting]], [[Bid-Ask Spread Decomposition]]

**Key references.** Hasbrouck (1995); Zhang, Mykland, Aït-Sahalia (2005); Roll (1984).
