---
type: atom
status: seed
domain: microstructure
assets: [equities]
tags: [market-structure, routing, lead-lag]
created: 2026-11-03
---

# Cross-Venue Fragmentation

**Idea.** US equities trade across ~16 lit exchanges plus dozens of ATSs/dark pools. The consolidated book is a fiction assembled from feeds with different latencies; price formation concentrates on a few venues and propagates to the rest. Who updates first, and where real size sits, is itself a signal and an execution problem.

**Practical notes.**
- Lead-lag across venues: primary-listing venues and the largest ECNs tend to lead; quotes elsewhere are echoes. Trading the echo against the leader is a latency game — see [[Latency Arbitrage]].
- SIP vs direct feeds: strategies on the slow consolidated feed see a delayed market; direct-feed users can anticipate NBBO changes.
- Smart order routing must model per-venue fill probability, fees ([[Maker-Taker Fee Economics]]), and information leakage.
- Odd-lot and off-exchange (TRF) volume shares are rising; the lit book under-represents true activity.

**Related.** [[Latency Arbitrage]], [[Maker-Taker Fee Economics]], [[Hidden Liquidity and Iceberg Orders]], [[Futures-ETF Lead-Lag]]

**Key references.** O'Hara & Ye (2011), *Is Market Fragmentation Harming Market Quality?*; Hasbrouck (1995) information shares.
