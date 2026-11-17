---
type: literature
status: inbox
title: "Dynamic Spatio-Temporal Graph Attention Networks with Nested Clustered Optimization for Multi-Asset Portfolios"
authors: [" Supriadi"]
year: 2026
venue: "arXiv q-fin.PM (2611.19903)"
url: https://arxiv.org/abs/2611.19903
pdf_url: https://arxiv.org/pdf/2611.19903
pdf: 00-Inbox/papers/Supriadi2026-Dynamic-Spatio-Temporal-Graph-Attention-Networks-261119903.pdf
swept: 2026-11-17
posted: 2026-11-15
origin: daily sweep script
relevance: medium
tags: [execution]
---

# Dynamic Spatio-Temporal Graph Attention Networks with Nested Clustered Optimization for Multi-Asset Portfolios

## Abstract (verbatim from arXiv)
Nested Clustered Optimization (NCO) insulates asset allocation from Markowitz covariance ill-conditioning. However, classical tree clustering relies on static pairwise Pearson correlation, failing to capture time-varying, asymmetric downside risk contagion across multi-asset markets. We propose a unified deep graph machine learning architecture: Dynamic Spatio-Temporal Graph Attention Networks with Nested Clustered Optimization (ST-GAT-NCO) for multi-asset tactical allocation. The framework extracts temporal momentum and downside risk dynamics via causal dilated 1D-convolutions, then deploys a multi-head Graph Attention Network (GAT) over dynamic market topologies to learn latent spatial node representations. These learned embeddings define an angular metric distance space that guides two-stage downside NCO optimization under institutional constraints and turnover smoothing. Evaluated over a 73-month non-anticipative walk-forward out-of-sample window (January 2020 to January 2026) across 13 global asset classes net of 10 bps transaction costs, ST-GAT-NCO achieves a 5.32% CAGR and 37.06% cumulative net return, delivering an excess Sharpe ratio of 0.30 and a Sortino ratio of 0.48. This substantially outperforms classical Minimum Variance (3.68% CAGR, 0.08 Sharpe), Hierarchical Risk Parity (2.65% CAGR), and Plain Symmetric NCO (4.11% CAGR, 0.15 Sharpe), while restricting maximum drawdown to -13.07% (versus -19.44% for Equal-Weight and -16.36% for Downside NCO) under a controlled one-way turnover of 15.31%/month. Regime analysis confirms active capital preservation across the 2020 COVID-19 crash, 2022 monetary tightening, and 2023-2026 disinflation rallies.

## Why staged
Auto-staged by the daily sweep (keyword filter, unreviewed). Possible related notes: [[Implementation Shortfall]].
