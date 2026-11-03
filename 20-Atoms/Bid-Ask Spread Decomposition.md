---
type: atom
status: seed
domain: microstructure
assets: [equities, futures]
tags: [market-making, liquidity, measurement]
created: 2026-11-03
---

# Bid-Ask Spread Decomposition

**Idea.** The quoted spread compensates liquidity providers for three distinct costs: order-processing costs, inventory risk, and adverse selection. Decomposing which component dominates in a given instrument tells you what strategy is viable there.

**Practical notes.**
- Effective spread = 2·|trade price − mid|; realized spread subtracts the post-trade mid move, isolating what the maker actually keeps.
- In [[Tick Size Constraints|large-tick names]] the spread is pinned at one tick and competition happens via queue position instead of price — see [[Queue Position Value]].
- High adverse-selection share → the instrument rewards informed/latency-sensitive takers; high inventory share → rewards warehousing risk.

**Related.** [[Adverse Selection]], [[Market Maker Inventory Control]], [[Maker-Taker Fee Economics]]

**Key references.** Huang & Stoll (1997), *The Components of the Bid-Ask Spread*; Stoll (1989).
