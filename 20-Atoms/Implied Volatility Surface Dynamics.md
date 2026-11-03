---
type: atom
status: seed
domain: options
assets: [options]
tags: [options, volatility, relative-value]
created: 2026-11-03
---

# Implied Volatility Surface Dynamics

**Idea.** The implied-vol surface (strike × maturity) moves in a few dominant modes — level, term-structure slope, skew — and its dynamics are partly predictable: vol mean-reverts, skew steepens in selloffs, and surface dislocations (single points rich/cheap vs a smooth fit) revert. Vol relative value trades the surface against its own typical shape.

**Practical notes.**
- Fit a parametric surface (SVI/SSVI or a spline) per snapshot; residuals of individual options vs the fit are the natural mean-reversion signal at HFT-to-daily horizons.
- Sticky-strike vs sticky-delta behavior differs by market and regime; getting this wrong breaks delta-hedged PnL attribution.
- Skew and term structure also carry *directional* information for the underlying — steepening put skew often precedes weakness (ties to [[Options Order Flow as Equity Signal]]).
- Market making on options chains is inventory control in surface coordinates — see [[Market Maker Inventory Control]].

**Related.** [[Variance Risk Premium]], [[Options Order Flow as Equity Signal]], [[Gamma Exposure and Dealer Hedging]]

**Key references.** Gatheral & Jacquier (2014), *Arbitrage-Free SVI Volatility Surfaces*; Cont & da Fonseca (2002), *Dynamics of Implied Volatility Surfaces*.
