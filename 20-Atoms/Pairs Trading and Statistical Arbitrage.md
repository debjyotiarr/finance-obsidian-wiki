---
type: atom
status: seed
domain: mid-frequency
assets: [equities, futures]
tags: [stat-arb, mean-reversion, relative-value]
created: 2026-11-03
---

# Pairs Trading and Statistical Arbitrage

**Idea.** Securities with a common fundamental exposure should move together; when their spread diverges beyond its typical range, short the rich leg and buy the cheap one, betting on reconvergence. Gatev, Goetzmann & Rouwenhorst (2006) documented the classic distance-method version; modern stat arb generalizes to factor-residual mean reversion across hundreds of names.

**Practical notes.**
- Cointegration tests beat correlation for pair selection, but *economic* linkage (dual listings, share classes, ETF vs basket, futures vs cash — see [[Futures-ETF Lead-Lag]]) beats statistics.
- Spread half-life sets the strategy's natural horizon and capital turnover; model it with an OU process.
- The classic version has decayed badly since the 2000s (crowding); residual reversal at shorter horizons and intraday stat arb remain active — see [[Signal Decay and Alpha Horizon]].
- Risk: divergences are sometimes informed (one leg is about to be repriced permanently). Stop-losses and event filters are load-bearing.

**Related.** [[Short-Term Reversal]], [[Futures-ETF Lead-Lag]], [[Backtest Overfitting and Deflated Sharpe]]

**Key references.** Gatev, Goetzmann, Rouwenhorst (2006); Avellaneda & Lee (2010), *Statistical Arbitrage in the US Equities Market*.
