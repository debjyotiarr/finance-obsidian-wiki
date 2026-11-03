---
type: atom
status: seed
domain: microstructure
assets: [equities, futures]
tags: [market-structure, orderbook, large-tick]
created: 2026-11-03
---

# Tick Size Constraints

**Idea.** The ratio of tick size to price divides instruments into two regimes. *Large-tick* assets (spread pinned at one tick, deep queues — e.g., ES futures, low-priced liquid stocks) and *small-tick* assets (multi-tick spreads, thin levels — e.g., high-priced stocks). Almost every microstructure signal behaves differently across this divide.

**Consequences.**
- Large tick: competition is via queue priority → [[Queue Position Value]] dominates; book imbalance ([[Microprice]]) is highly informative; price moves are rare and discrete.
- Small tick: competition is via price; the inside quote flickers; depth aggregation across levels matters; [[Order Flow Imbalance]] needs multi-level treatment.

**Practical notes.**
- Classify your universe by average spread in ticks before building any book signal.
- Regulatory tick changes (e.g., US Tick Size Pilot, half-penny ticks under Reg NMS amendments) are natural experiments and regime breaks.

**Related.** [[Queue Position Value]], [[Microprice]], [[Bid-Ask Spread Decomposition]], [[Maker-Taker Fee Economics]]

**Key references.** Eisler, Bouchaud et al. on large-tick dynamics; Dayri & Rosenbaum (2015), *Large Tick Assets: Implicit Spread and Optimal Tick Size*.
