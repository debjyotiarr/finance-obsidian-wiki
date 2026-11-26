---
type: literature
status: inbox
title: "Graph-Informed Deep Factor Model for Statistical Arbitrage"
authors: ["Evelyn Zhu", "Mucheng Zhu", "Brendan Martin", "Mihai Cucuringu"]
year: 2026
venue: "arXiv q-fin.ST (2611.34209)"
url: https://arxiv.org/abs/2611.34209
pdf_url: https://arxiv.org/pdf/2611.34209
pdf: 00-Inbox/papers/Zhu2026-Graph-Informed-Deep-Factor-Model-for-261134209.pdf
swept: 2026-11-26
posted: 2026-11-25
origin: daily sweep script
relevance: medium
tags: [stat-arb]
---

# Graph-Informed Deep Factor Model for Statistical Arbitrage

## Abstract (verbatim from arXiv)
Statistical arbitrage exploits temporary mispricings between similar assets in the cross-section of daily equity returns. We propose a nonlinear single-factor model, called a Graph-Informed Deep Factor (GIDF) model, whose per-stock loadings have cross-sectional dependence conditional on a latent network. The network captures cross-sectional return dependencies that remain after removing the dominant eigenmodes of the return correlation matrix, thereby providing a complementary representation of inter-asset relationships beyond the leading sources of systematic variation. It is reconstructed from data using a novel method that we call the Factor-Adjusted Dynamic EWMA (FADE). A signed-edge graph attention mechanism then combines the reconstructed network with exogenous firm characteristics and macroeconomic variables. This graph-informed specification is designed to produce residuals that more effectively separate idiosyncratic mean-reverting dynamics from cross-sectional co-movements, yielding economically useful signals for daily statistical arbitrage. In a comprehensive empirical study on daily U.S. equities from 2015 to 2024, GIDF outperforms classical factor models and state-of-the-art deep learning methods, achieving an out-of-sample Sharpe ratio of 1.78 under the canonical Avellaneda--Lee rule.

## Why staged
Auto-staged by the daily sweep (keyword filter, unreviewed). Possible related notes: [[Pairs Trading and Statistical Arbitrage]].
