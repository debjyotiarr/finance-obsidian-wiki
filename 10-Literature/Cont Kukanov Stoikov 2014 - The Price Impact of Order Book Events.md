---
type: literature
status: extracted
authors: [Rama Cont, Arseniy Kukanov, Sasha Stoikov]
year: 2014
venue: Journal of Financial Econometrics
url: https://arxiv.org/abs/1011.6402
pdf:
tags: [orderflow, orderbook, impact]
created: 2026-11-03
---

# Cont, Kukanov & Stoikov (2014) — The Price Impact of Order Book Events

## One-line summary
Short-horizon price changes are a linear function of order flow imbalance at the best quotes, with slope inversely proportional to market depth.

## Key contributions
- Defines OFI from level-1 events (limit order additions, cancellations, market orders) as a single signed flow measure.
- Shows ΔP ≈ OFI / (2·depth) fits across stocks and time with high R² at ~10-second windows.
- Impact of *trades alone* is much noisier — the book events matter, not just executions.

## Data and method
NYSE TAQ + order book data, 50 S&P 500 stocks, April 2010; linear regressions per stock-day.

## Atoms extracted
- [[Order Flow Imbalance]] — the core result.
- [[Price Impact and Kyle's Lambda]] — empirical linear-impact evidence at short horizons.
- [[Microprice]] — motivation for depth-weighted fair value.

## Critique / open questions
Level-1 only; multi-level OFI (Xu et al. extensions) adds modest power. Linearity degrades at longer horizons where impact concavity ([[Square-Root Law of Market Impact]]) takes over. Pre-dates modern odd-lot/fragmentation regime — re-estimate on current data.
