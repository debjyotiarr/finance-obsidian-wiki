---
type: literature
status: inbox
title: "Time Matters: Exploring The Effects of Urgency and Reaction Speed in Automated Traders"
authors: ["Henry Hanifan", "Ben Watson", "John Cartlidge", "Dave Cliff"]
year: 2021
venue: "arXiv 2103.00600"
url: http://arxiv.org/abs/2103.00600
pdf_url:
pdf: 00-Inbox/papers/Hanifan2021-Time-Matters-Exploring-The-Effects-of-40cc46.pdf
swept: 2026-11-12
origin: baobach/hft_papers catalogue
relevance: medium
tags: [arxiv, auctions, orderbook]
---

# Time Matters: Exploring The Effects of Urgency and Reaction Speed in Automated Traders

## Abstract (verbatim from arXiv)
We consider issues of time in automated trading strategies in simulated financial markets containing a single exchange with public limit order book and continuous double auction matching. In particular, we explore two effects: (i) reaction speed - the time taken for trading strategies to calculate a response to market events; and (ii) trading urgency - the sensitivity of trading strategies to approaching deadlines. Much of the literature on trading agents focuses on optimising pricing strategies only and ignores the effects of time, while real-world markets continue to experience a race to zero latency, as automated trading systems compete to quickly access information and act in the market ahead of others. We demonstrate that modelling reaction speed can significantly alter previously published results, with simple strategies such as SHVR outperforming more complex adaptive algorithms such as AA. We also show that adding a pace parameter to ZIP traders (ZIP-Pace, or ZIPP) can create a sense of urgency that significantly improves profitability.

## Why staged
Auto-triaged by keyword from the baobach/hft_papers catalogue (unreviewed; quality unknown). Possible atoms: [[Limit Order Book Shape as Signal]], [[Opening and Closing Auctions]].
