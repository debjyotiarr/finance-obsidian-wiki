---
type: literature
status: inbox
title: "Improving Algorithmic Trading for BESS on Intraday Electricity Markets through Distributional Price Forecasts"
authors: ["Simon Hirsch", "David Schaurecker", "David Wozabal"]
year: 2026
venue: "arXiv q-fin.ST (2611.17170)"
url: https://arxiv.org/abs/2611.17170
pdf_url: https://arxiv.org/pdf/2611.17170
pdf: 00-Inbox/papers/Hirsch2026-Improving-Algorithmic-Trading-for-BESS-on-261117170.pdf
swept: 2026-11-15
posted: 2026-11-12
origin: daily sweep script
relevance: medium
tags: [intraday, orderbook]
---

# Improving Algorithmic Trading for BESS on Intraday Electricity Markets through Distributional Price Forecasts

## Abstract (verbatim from arXiv)
Grid-scale battery energy storage systems (BESS) are becoming increasingly important in short-term energy markets, where they help balance fluctuations in variable renewable generation. In many countries, the continuous intraday market is the most important wholesale market for BESS to monetize their flexibility. In this paper, we propose an extension to the myopic rolling intrinsic policy that incorporates intraday price forecasts tailored specifically to the BESS trading problem. While a large literature addresses intraday price forecasting, most existing work focuses on volume-weighted prices during the last hours of trading and consequently fails to capture the features most relevant to BESS trading. Our approach addresses this gap by introducing a novel target variable derived from the limit order book and its dynamics. The resulting forecasts are designed to inform the optimization about future profit opportunities while preserving computational efficiency and avoiding the burden of full stochastic optimization. In a realistic high-frequency simulation setting covering 2023 and 2024, our method improves profits by up to 42% over the naive rolling intrinsic formulation. We further analyze the relationship between forecast accuracy, stability, and financial performance, establishing a clear inverse relationship between accuracy and stability. Finally, we find evidence that BESS size and duration jointly influence both overall profitability and the marginal benefit of incorporating forecasts.

## Why staged
Auto-staged by the daily sweep (keyword filter, unreviewed). Possible related notes: [[Limit Order Book Shape as Signal]], [[Intraday Momentum]].
