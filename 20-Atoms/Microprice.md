---
type: atom
status: seed
domain: microstructure
assets: [equities, futures]
tags: [orderbook, fair-value, alpha]
created: 2026-11-03
---

# Microprice

**Idea.** The mid price is a biased estimate of fair value when the book is imbalanced. The *microprice* weights bid and ask by opposite-side sizes — P_micro = (P_ask·Q_bid + P_bid·Q_ask)/(Q_bid+Q_ask) — so a heavy bid pushes fair value toward the ask. Stoikov (2018) generalizes this to the martingale expectation of the future mid conditional on book state.

**Why it works.** Book imbalance predicts the direction of the next mid move (see [[Order Flow Imbalance]]); the microprice bakes that prediction into the reference price itself.

**Practical notes.**
- Best single-number fair value for quoting, hedging triggers, and signal normalization.
- In [[Tick Size Constraints|large-tick names]], imbalance is *the* dominant short-horizon predictor and the microprice does most of the work.
- Stoikov's estimator conditions on (imbalance, spread) buckets and iterates expectations — simple to fit from book data.

**Related.** [[Order Flow Imbalance]], [[Limit Order Book Shape as Signal]], [[Market Maker Inventory Control]]

**Key references.** Stoikov (2018), *The Micro-Price: A High-Frequency Estimator of Future Prices*.
