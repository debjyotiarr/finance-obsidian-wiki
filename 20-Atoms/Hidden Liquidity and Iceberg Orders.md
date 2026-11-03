---
type: atom
status: seed
domain: microstructure
assets: [equities, futures]
tags: [orderbook, liquidity, detection]
created: 2026-11-03
---

# Hidden Liquidity and Iceberg Orders

**Idea.** A substantial fraction of liquidity is not displayed: iceberg orders (displayed tip, hidden reserve), fully hidden orders, and dark pools. Detecting hidden size changes the effective book, fill probabilities, and the meaning of displayed imbalance.

**Detection approaches.**
- Executions exceeding displayed size at a level, or immediate refills after a fill at the same price, reveal icebergs.
- Some feeds let you reverse-engineer reserve size from order-ID / priority patterns.
- Statistical models of refill behavior give a probability of further hidden size.

**Practical notes.**
- Hidden liquidity biases [[Order Flow Imbalance]] and [[Microprice]] in small-tick names — displayed imbalance overstates true imbalance.
- The presence of a detected iceberg is itself a signal: a large patient trader is anchored at that price.
- Dark pool prints (reported to the tape with delay) carry exploitable information about institutional flow.

**Related.** [[Limit Order Book Shape as Signal]], [[Adverse Selection]], [[Cross-Venue Fragmentation]]

**Key references.** Hautsch & Huang (2012) on hidden liquidity detection; Buti, Rindi, Werner on dark pools.
