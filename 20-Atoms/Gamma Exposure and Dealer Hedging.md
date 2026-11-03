---
type: atom
status: seed
domain: options
assets: [options, equities, futures]
tags: [options, flow, volatility, market-structure]
created: 2026-11-03
---

# Gamma Exposure and Dealer Hedging

**Idea.** Option dealers delta-hedge their books. When dealers are net *long* gamma they trade against the market (sell rallies, buy dips), damping volatility; net *short* gamma forces them to chase moves, amplifying them. Aggregate dealer gamma exposure (GEX) thus predicts realized volatility, intraday mean-reversion vs trend behavior, and pinning near large strikes at expiry.

**Practical notes.**
- Estimating GEX requires assumptions about which side dealers hold; naive "all calls dealer-short" versions are crude. Open-interest-weighted gamma by strike plus flow data (e.g., open/close flags) does better.
- Effects are strongest near expirations (charm/vanna flows), around large round strikes (pinning), and in the 0DTE era where intraday gamma turns over daily.
- Conditioning [[Intraday Momentum]] on the gamma regime is a known enhancer: momentum works in short-gamma regimes, reversion in long-gamma.

**Related.** [[Options Order Flow as Equity Signal]], [[Implied Volatility Surface Dynamics]], [[Intraday Momentum]], [[Market Maker Inventory Control]]

**Key references.** Baltussen, Da, Lammers, Martens (2021), *Hedging Demand and Market Intraday Momentum*; Ni, Pearson, Poteshman (2005) on expiration pinning.
