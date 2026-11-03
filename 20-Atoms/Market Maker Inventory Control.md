---
type: atom
status: seed
domain: microstructure
assets: [equities, futures, options]
tags: [market-making, risk, optimal-control]
created: 2026-11-03
---

# Market Maker Inventory Control

**Idea.** A market maker's quotes should depend on current inventory: skew quotes to shed unwanted position. Avellaneda & Stoikov (2008) formalized this as a stochastic control problem — the optimal bid/ask are centered on a *reservation price* shifted away from the mid in proportion to inventory, risk aversion, and remaining time.

**Core result.** Reservation price r = s − q·γ·σ²·(T−t), where q is inventory. Spread widens with volatility and risk aversion, narrows with order-arrival intensity.

**Practical notes.**
- Real desks implement this as inventory-dependent quote skew plus hard position limits, not the closed-form solution.
- Interacts with [[Adverse Selection]]: skewing toward the toxic side to flatten inventory can be expensive; good implementations condition the skew on flow toxicity.
- Hedging in a correlated instrument (e.g., ES vs SPY — see [[Futures-ETF Lead-Lag]]) is often cheaper than skewing.

**Related.** [[Bid-Ask Spread Decomposition]], [[Queue Position Value]], [[Gamma Exposure and Dealer Hedging]]

**Key references.** Avellaneda & Stoikov (2008); Guéant, Lehalle & Fernandez-Tapia (2013); Ho & Stoll (1981).
