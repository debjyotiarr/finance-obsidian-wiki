---
type: atom
status: seed
domain: mid-frequency
assets: [equities, futures]
tags: [momentum, intraday, alpha]
created: 2026-11-03
---

# Intraday Momentum

**Idea.** The first half-hour return of the trading day predicts the last half-hour return in the same direction (Gao, Han, Li, Zhou 2018, on SPY). Related patterns: overnight gaps continue early, and late-day flows (ETF rebalancing, [[Gamma Exposure and Dealer Hedging|dealer hedging]], MOC imbalances) create predictable end-of-day drift.

**Candidate mechanisms.** Slow-moving capital reacting to morning information; intraday leverage targeting and gamma hedging amplifying moves into the close; investor attention clustering at open/close.

**Practical notes.**
- Strongest on high-volatility and high-volume days, and around macro announcement days.
- Interacts with the intraday volume U-shape — size the close leg where liquidity actually is.
- MOC/LOC imbalance feeds (published ~15:50 ET for NYSE/Nasdaq) are a directly tradable cousin of this effect.
- Decay check: published 2018; monitor live performance — see [[Signal Decay and Alpha Horizon]].

**Related.** [[Overnight vs Intraday Returns]], [[Gamma Exposure and Dealer Hedging]], [[Short-Term Reversal]]

**Key references.** Gao, Han, Li, Zhou (2018), *Market Intraday Momentum*; Bogousslavsky (2021) on intraday return patterns.
