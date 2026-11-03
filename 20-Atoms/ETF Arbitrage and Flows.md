---
type: atom
status: seed
domain: microstructure
assets: [equities, futures]
tags: [etf, arbitrage, flow, cross-asset]
created: 2026-11-03
---

# ETF Arbitrage and Flows

**Idea.** Authorized participants arbitrage ETF price against NAV via creation/redemption, binding the ETF to its basket. This machinery transmits flows both ways: ETF demand propagates to constituents (liquidity mismatch in bond ETFs; inclusion effects in equities), and basket moves propagate to the ETF. Premium/discount and creation-flow data are signals.

**Practical notes.**
- ETF premium vs iNAV, after fair-valuing stale constituents, mean-reverts intraday — the bread-and-butter of ETF market making; stale-constituent handling is where the skill is.
- Constituent-level: a stock's ownership by ETFs predicts its exposure to non-fundamental flow (Ben-David, Franzoni, Moussawi find higher volatility); rebalance dates create forecastable demand.
- Leveraged ETFs must rebalance daily *in the direction of the move*, near the close — a predictable, sizeable flow that interacts with [[Opening and Closing Auctions]] and [[Gamma Exposure and Dealer Hedging]].
- ES–SPY–basket triangle is the canonical speed game — see [[Futures-ETF Lead-Lag]].

**Related.** [[Futures-ETF Lead-Lag]], [[Opening and Closing Auctions]], [[Pairs Trading and Statistical Arbitrage]]

**Key references.** Ben-David, Franzoni, Moussawi (2018), *Do ETFs Increase Volatility?*; Cheng & Madhavan (2009) on leveraged ETF rebalancing.
