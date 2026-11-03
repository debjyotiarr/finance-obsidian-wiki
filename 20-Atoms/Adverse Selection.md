---
type: atom
status: seed
domain: microstructure
assets: [equities, futures, options]
tags: [market-making, risk, information]
created: 2026-11-03
---

# Adverse Selection

**Idea.** A passive quote is disproportionately filled when it is about to be wrong: informed traders hit your bid just before the price falls. The cost of being picked off is the central cost of market making and the reason spreads exist (Glosten–Milgrom).

**Why it matters.** Realized spread = quoted spread − adverse selection cost. A market maker can quote a tight spread and still lose if fills are toxic. Measuring *markouts* (mid-price move N ms/sec after a fill) is the standard diagnostic.

**Practical notes.**
- Markout curves by counterparty type, venue, and time-of-day reveal where toxicity lives.
- Adverse selection is worse around news, auctions, and when [[Order Flow Toxicity (VPIN)]] is elevated.
- Queue priority interacts with it: fills from the front of the queue are less adversely selected — see [[Queue Position Value]].

**Related.** [[Bid-Ask Spread Decomposition]], [[Market Maker Inventory Control]], [[Latency Arbitrage]], [[Hidden Liquidity and Iceberg Orders]]

**Key references.** Glosten & Milgrom (1985); Hendershott, Jones & Menkveld (2011) for empirical markout methodology.
