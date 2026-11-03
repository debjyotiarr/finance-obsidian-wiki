---
type: atom
status: seed
domain: options
assets: [options, futures, equities]
tags: [volatility, risk-premium, alpha]
created: 2026-11-03
---

# Variance Risk Premium

**Idea.** Implied variance systematically exceeds subsequently realized variance: sellers of index options/variance earn a persistent premium as compensation for crash risk. The VRP (implied minus expected realized variance) is also a *predictor* — a high VRP forecasts positive equity returns over weeks to months (Bollerslev, Tauchen, Zhou 2009).

**Practical notes.**
- Harvesting: short delta-hedged straddles, variance swaps, VIX futures carry (the VIX term structure's contango is the same premium in futures form — see [[Futures Term Structure and Carry]]).
- The premium is payment for negatively skewed returns: years of carry can vanish in one event (Feb 2018 "Volmageddon"). Position sizing and convexity hedges are the whole game.
- Cross-sectionally, single-name VRP vs index VRP spreads capture the correlation risk premium.
- Realized-variance forecasting quality (HAR models, intraday data) directly improves VRP measurement.

**Related.** [[Implied Volatility Surface Dynamics]], [[Futures Term Structure and Carry]], [[Gamma Exposure and Dealer Hedging]]

**Key references.** Carr & Wu (2009), *Variance Risk Premiums*; Bollerslev, Tauchen, Zhou (2009).
