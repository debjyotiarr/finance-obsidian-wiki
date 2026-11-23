---
type: literature
status: inbox
title: "Do Econophysics-Inspired Inputs Improve Neural Covariance Forecasting? A Leakage-Free Walk-Forward Study of Intraday DJIA Data"
authors: ["Gabriele Ranco"]
year: 2026
venue: "arXiv q-fin.CP (2611.27616)"
url: https://arxiv.org/abs/2611.27616
pdf_url: https://arxiv.org/pdf/2611.27616
pdf: 00-Inbox/papers/Ranco2026-Do-Econophysics-Inspired-Inputs-Improve-Neural-261127616.pdf
swept: 2026-11-23
posted: 2026-11-20
origin: daily sweep script
relevance: medium
tags: [execution, intraday, point-process]
---

# Do Econophysics-Inspired Inputs Improve Neural Covariance Forecasting? A Leakage-Free Walk-Forward Study of Intraday DJIA Data

## Abstract (verbatim from arXiv)
Tools from econophysics, including Random Matrix Theory (RMT), Tsallis q-Gaussian tails, Hawkes self-excitation and diffusion-inspired regularization, are often proposed as ingredients for financial risk models, but their incremental value over strong contemporary benchmarks remains unclear. We introduce a Physics-Inspired Neural Covariance (PINC) framework for one-day-ahead covariance forecasting using 1-minute data from the 29 Dow Jones Industrial Average constituents over 545 trading days. The model incorporates RMT-cleaned correlations, Tsallis tail indices and Hawkes intensities as inputs and optionally includes a Fokker-Planck-inspired regularization term selected strictly on validation data. Evaluation is performed through a nested walk-forward design with 11 folds, 231 out-of-sample trading days and multiple random seeds, with explicit leakage controls and reproducibility tests. Neural models outperform static covariance estimators such as sample, Ledoit-Wolf, RMT and EVT-based estimators, but show no statistically significant improvement over HAR-RV or LSTM benchmarks. Validation consistently rejects the physics-inspired regularizer, and ablation studies find no measurable contribution from the RMT, Tsallis or Hawkes features. Portfolio experiments show no statistically significant Sharpe ratio improvement after transaction costs. These results suggest that, for this dataset and forecasting horizon, econophysics-inspired components do not provide measurable benefits beyond strong financial forecasting benchmarks.

## Why staged
Auto-staged by the daily sweep (keyword filter, unreviewed). Possible related notes: [[Hawkes Processes for Order Flow]], [[Implementation Shortfall]], [[Intraday Momentum]].
