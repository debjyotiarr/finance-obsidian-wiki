---
type: literature
status: inbox
title: "Which Past Matters? Training History and Multi-Forecast Horizon in Equity Transformers"
authors: ["Chariton Chalvatzis"]
year: 2026
venue: "arXiv q-fin.ST (2611.23126)"
url: https://arxiv.org/abs/2611.23126
pdf_url: https://arxiv.org/pdf/2611.23126
pdf: 00-Inbox/papers/Chalvatzis2026-Which-Past-Matters-Training-History-and-261123126.pdf
swept: 2026-11-18
posted: 2026-11-17
origin: daily sweep script
relevance: medium
tags: [intraday]
---

# Which Past Matters? Training History and Multi-Forecast Horizon in Equity Transformers

## Abstract (verbatim from arXiv)
More historical data can improve estimation while introducing relationships that transfer poorly to current market conditions. We therefore examine how training quantity and historical selection interact with forecast horizon in intraday equity prediction. We deploy twelve configurations which combine four sampling and validation policies with 6, 12 and 24 month training quantities under a fixed cross-sectional Transformer and feature set. A monthly walk-forward experiment produces 264 refits and eight cumulative return forecasts from 5 to 120 minutes. Evaluation covers January 2025 through 20 October 2026 and uses cross-sectional Spearman information coefficients against future five-factor residual returns. Six-month recency sampling leads individual models at 5-15 minutes, while multi recency configurations lead at 20-30 minutes and uniform configurations at 60-120 minutes. Increasing training quantity does not uniformly improve accuracy while an equal-weight ensemble of all twelve models exceeds every individual mean at 15, 20 and 25 minutes, but not at the remaining horizons. These findings support evaluating historical selection jointly with forecast horizon without identifying a universal policy or a causal benefit from recency.

## Why staged
Auto-staged by the daily sweep (keyword filter, unreviewed). Possible related notes: [[Intraday Momentum]].
