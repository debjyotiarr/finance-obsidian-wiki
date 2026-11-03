---
type: atom
status: seed
domain: microstructure
assets: [equities, futures]
tags: [market-making, orderbook, large-tick]
created: 2026-11-03
---

# Queue Position Value

**Idea.** In large-tick instruments where the spread is almost always one tick, the economic value of a resting limit order depends heavily on its position in the FIFO queue. Front-of-queue orders capture the spread with low adverse selection; back-of-queue orders are filled mostly when the level is about to break.

**Why it works.** Fills that occur while the queue is still deep are benign (the price holds); fills that occur as the queue empties are toxic. Queue position is therefore a direct proxy for expected [[Adverse Selection]] conditional on fill.

**Practical notes.**
- Value of queue position can be estimated by simulating fill outcomes conditional on remaining queue ahead (Moallemi & Yuan).
- Drives behavior: traders join new levels early, use order-splitting to preserve priority, and treat cancel/replace decisions as an option-value problem.
- Matters most in ES-type futures and sub-dollar-spread equities; irrelevant in small-tick names.

**Related.** [[Tick Size Constraints]], [[Market Maker Inventory Control]], [[Limit Order Book Shape as Signal]]

**Key references.** Moallemi & Yuan (2016), *A Model for Queue Position Valuation*.
