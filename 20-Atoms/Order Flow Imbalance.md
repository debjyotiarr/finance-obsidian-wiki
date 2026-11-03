---
type: atom
status: seed
domain: microstructure
assets: [equities, futures]
tags: [orderflow, alpha, orderbook]
created: 2026-11-03
---

# Order Flow Imbalance

**Idea.** Net signed changes at the best bid and ask (additions, cancellations, and trades) predict short-horizon price moves. Cont, Kukanov & Stoikov (2014) showed that price changes over short windows are approximately *linear* in order flow imbalance (OFI), with slope inversely proportional to market depth.

**Why it works.** The order book is a queueing system: when buy pressure (bid additions + ask depletions) outweighs sell pressure, the mid price is mechanically pushed up. OFI aggregates this pressure into a single, surprisingly linear predictor.

**Practical notes.**
- OFI at the best level captures most of the signal; multi-level OFI adds some power (deeper levels matter more for [[Tick Size Constraints|large-tick assets]]).
- Normalize by average depth to make the signal comparable across names and regimes.
- Horizon: seconds to minutes. Decays fast — see [[Signal Decay and Alpha Horizon]].

**Related.** [[Microprice]], [[Limit Order Book Shape as Signal]], [[Price Impact and Kyle's Lambda]], [[Trade Sign Autocorrelation]], [[Order Flow Toxicity (VPIN)]]

**Key references.** Cont, Kukanov, Stoikov (2014), *The Price Impact of Order Book Events*, J. Financial Econometrics.
