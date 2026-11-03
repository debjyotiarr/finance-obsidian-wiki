---
type: atom
status: seed
domain: microstructure
assets: [equities, futures]
tags: [orderbook, alpha, machine-learning]
created: 2026-11-03
---

# Limit Order Book Shape as Signal

**Idea.** The full shape of the limit order book — depth profile across levels, slope, gaps, recent add/cancel activity — carries predictive information beyond top-of-book imbalance. Deep-book features feed both handcrafted signals and ML models (e.g., DeepLOB-style CNNs/LSTMs on book snapshots).

**Practical notes.**
- Marginal value of deeper levels is real but small and decays with level; most predictability sits in levels 1–3 and in *changes* (flow) rather than static depth.
- Beware spoofing-era artifacts and venue-specific quirks (hidden size, odd lots) — see [[Hidden Liquidity and Iceberg Orders]].
- ML on raw book snapshots overfits easily; stationarize (normalize by tick, by average depth) and test across regimes — see [[Backtest Overfitting and Deflated Sharpe]].
- Signals from book shape are capacity-constrained and latency-sensitive: edge accrues to fast infrastructure — see [[Latency Arbitrage]].

**Related.** [[Order Flow Imbalance]], [[Microprice]], [[Hawkes Processes for Order Flow]], [[Queue Position Value]]

**Key references.** Zhang, Zohren, Roberts (2019), *DeepLOB*; Sirignano & Cont (2019), *Universal Features of Price Formation*.
