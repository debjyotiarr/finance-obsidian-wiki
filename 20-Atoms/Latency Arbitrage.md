---
type: atom
status: seed
domain: microstructure
assets: [equities, futures]
tags: [market-structure, hft, arbitrage]
created: 2026-11-03
---

# Latency Arbitrage

**Idea.** When the same or near-identical instrument trades on multiple venues, the fastest participant can trade on one venue against quotes that are stale relative to information already public on another. Budish, Cramton & Shim (2015) documented persistent ES–SPY arbitrage opportunities lasting milliseconds and argued continuous-time trading creates a wasteful speed race.

**Mechanics.** Futures typically lead (see [[Futures-ETF Lead-Lag]]); on a futures tick, racers snipe stale equity/ETF quotes before makers can cancel. The maker's loss is the sniper's gain — a pure transfer priced into spreads as [[Adverse Selection]].

**Practical notes.**
- Even non-HFT strategies pay for this via wider spreads; execution should avoid resting quotes in snipeable states around correlated-instrument moves.
- Structural responses: speed bumps (IEX), frequent batch auctions (proposal), asymmetric delays.
- Measuring "races": Aquilina, Budish, O'Neill (2021) using exchange message data — races are ~20% of volume in FTSE 100 names.

**Related.** [[Futures-ETF Lead-Lag]], [[Adverse Selection]], [[Cross-Venue Fragmentation]], [[Microprice]]

**Key references.** Budish, Cramton, Shim (2015); Aquilina, Budish, O'Neill (2021), *Quantifying the High-Frequency Trading Arms Race*.
