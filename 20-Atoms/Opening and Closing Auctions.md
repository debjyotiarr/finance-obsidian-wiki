---
type: atom
status: seed
domain: microstructure
assets: [equities]
tags: [auctions, market-structure, flow]
created: 2026-11-03
---

# Opening and Closing Auctions

**Idea.** The open and close are single-price call auctions, not continuous markets, and the close now concentrates ~10%+ of US equity volume (index funds benchmark to it). Auction mechanics — imbalance publication, indicative prices, cutoff times — create a distinct, information-rich microstructure.

**Practical notes.**
- NYSE/Nasdaq publish MOC/LOC imbalance data from ~15:50 ET; the imbalance and its revisions predict both auction price pressure and post-auction reversion.
- Predictable close flows (index rebalances, ETF creation/redemption — see [[ETF Arbitrage and Flows]], option expiry baskets) are front-run and provided-to; which side you're on is a capacity question.
- The opening auction digests overnight information (ties to [[Overnight vs Intraday Returns]]); opening-price dislocations in individual names revert intraday.
- Auction-adjacent continuous trading (last 10 min) shows amplified [[Intraday Momentum]] effects.

**Related.** [[Intraday Momentum]], [[ETF Arbitrage and Flows]], [[Overnight vs Intraday Returns]]

**Key references.** Bogousslavsky & Muravyev (2023), *Who Trades at the Close?*; Hu & Murphy on closing auction manipulation and dynamics.
