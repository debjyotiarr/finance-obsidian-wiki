---
type: atom
status: seed
domain: execution
assets: [equities, futures, options]
tags: [execution, measurement, tca]
created: 2026-11-03
---

# Implementation Shortfall

**Idea.** The true cost of trading is the difference between the paper portfolio (filled instantly at the decision price) and the real portfolio — Perold's *implementation shortfall*. It decomposes into delay cost, impact cost, spread cost, and opportunity cost of unfilled quantity.

**Why it matters.** Signals live or die by net-of-cost performance. A mid-frequency alpha of 10 bps with 8 bps shortfall is a different business from the same alpha with 2 bps. Transaction cost analysis (TCA) against arrival price is the standard report card.

**Practical notes.**
- Benchmarks: arrival price (the honest one), VWAP (gameable), close (for close-targeting strategies).
- Pre-trade cost models (based on [[Square-Root Law of Market Impact]]) should be calibrated against your own fills, not vendor averages.
- Shortfall feeds back into strategy design: capacity, turnover ceilings, and whether a signal is tradable at all — see [[Signal Decay and Alpha Horizon]].

**Related.** [[Optimal Execution (Almgren-Chriss)]], [[Square-Root Law of Market Impact]], [[Signal Decay and Alpha Horizon]]

**Key references.** Perold (1988), *The Implementation Shortfall*; Kissell (2013), *The Science of Algorithmic Trading*.
