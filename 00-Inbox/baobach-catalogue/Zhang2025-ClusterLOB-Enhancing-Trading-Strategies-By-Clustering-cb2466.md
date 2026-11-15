---
type: literature
status: inbox
title: "ClusterLOB: Enhancing Trading Strategies By Clustering Orders in Limit Order Books"
authors: ["Yichi Zhang", "Mihai Cucuringu", "Alexander Y. Shestopaloff", "Stefan Zohren"]
year: 2025
venue: "arXiv 2504.20349"
url: http://arxiv.org/abs/2504.20349
pdf_url:
pdf: 00-Inbox/papers/Zhang2025-ClusterLOB-Enhancing-Trading-Strategies-By-Clustering-cb2466.pdf
swept: 2026-11-12
origin: baobach/hft_papers catalogue
relevance: high
tags: [arxiv, orderbook]
---

# ClusterLOB: Enhancing Trading Strategies By Clustering Orders in Limit Order Books

## Abstract (verbatim from arXiv)
In the rapidly evolving world of financial markets, understanding the dynamics of limit order book (LOB) is crucial for unraveling market microstructure and participant behavior. We introduce ClusterLOB as a method to cluster individual market events in a stream of market-by-order (MBO) data into different groups. To do so, each market event is augmented with six time-dependent features. By applying the K-means++ clustering algorithm to the resulting order features, we are then able to assign each new order to one of three distinct clusters, which we identify as directional, opportunistic, and market-making participants, each capturing unique trading behaviors. Our experimental results are performed on one year of MBO data containing small-tick, medium-tick, and large-tick stocks from NASDAQ. To validate the usefulness of our clustering, we compute order flow imbalances across each cluster within 30-minute buckets during the trading day. We treat each cluster's imbalance as a signal that provides insights into trading strategies and participants' responses to varying market conditions. To assess the effectiveness of these signals, we identify the trading strategy with the highest Sharpe ratio in the training dataset, and demonstrate that its performance in the test dataset is superior to benchmark trading strategies that do not incorporate clustering. We also evaluate trading strategies based on order flow imbalance decompositions across different market event types, including add, cancel, and trade events, to assess their robustness in various market conditions. This work establishes a robust framework for clustering market participant behavior, which helps us to better understand market microstructure, and inform the development of more effective predictive trading signals with practical applications in algorithmic trading and quantitative finance.

## Why staged
Auto-triaged by keyword from the baobach/hft_papers catalogue (unreviewed; quality unknown). Possible atoms: [[Limit Order Book Shape as Signal]].
