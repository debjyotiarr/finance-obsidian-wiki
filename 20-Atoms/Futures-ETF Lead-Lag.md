---
type: atom
status: seed
domain: microstructure
assets: [futures, equities]
tags: [lead-lag, arbitrage, price-discovery]
created: 2026-11-03
---

# Futures-ETF Lead-Lag

**Idea.** Index futures (ES) lead the corresponding ETF (SPY) and the cash basket at millisecond-to-second horizons: price discovery happens where leverage is cheapest and trading is fastest. The lag has compressed from minutes (1980s) to single-digit milliseconds, but it never fully closes because arbitrage capital is finite and latency is physical.

**Practical notes.**
- The lead-lag is the raw material of [[Latency Arbitrage]] (Budish et al.'s ES–SPY races) — as a *predictive signal* it is only harvestable with top-tier speed.
- Slower uses: futures returns as a conditioning variable for equity signals, hedging market makers' inventory in the leading instrument, and detecting which instrument currently leads (it shifts with relative volume and volatility).
- Generalizes widely: options→stock ([[Options Order Flow as Equity Signal]]), large-caps→small-caps, US close→Asia open, crypto perps→spot.
- Hasbrouck information shares / VECM estimates quantify where discovery happens.

**Related.** [[Latency Arbitrage]], [[Cross-Venue Fragmentation]], [[Pairs Trading and Statistical Arbitrage]], [[Futures Term Structure and Carry]]

**Key references.** Hasbrouck (2003), *Intraday Price Formation in U.S. Equity Index Markets*; Budish, Cramton, Shim (2015).
