---
type: atom
status: seed
domain: microstructure
assets: [equities, futures]
tags: [orderflow, risk, information]
created: 2026-11-03
---

# Order Flow Toxicity (VPIN)

**Idea.** VPIN (Volume-Synchronized Probability of Informed Trading) measures how one-sided recent volume is, sampled in volume buckets rather than clock time. High VPIN = flow is likely informed = liquidity provision is dangerous. Easley, López de Prado & O'Hara proposed it as a real-time toxicity gauge and noted it spiked before the 2010 Flash Crash.

**Mechanics.** Classify volume into buy/sell (bulk classification by price change within volume buckets); VPIN = average |buy − sell| / total over a rolling window of buckets. Volume sampling makes it comparable across activity regimes — see [[Volume Clock]].

**Practical notes.**
- Use as a *risk overlay*: widen quotes or pull liquidity when toxicity spikes, rather than as a directional signal.
- Contested empirically (Andersen & Bondarenko argue it mostly proxies volatility) — treat the volatility-adjusted residual as the informative part.
- Natural companion to markout-based [[Adverse Selection]] measurement.

**Related.** [[Adverse Selection]], [[Volume Clock]], [[Trade Sign Autocorrelation]], [[Market Maker Inventory Control]]

**Key references.** Easley, López de Prado, O'Hara (2012), *Flow Toxicity and Liquidity in a High-Frequency World*.
