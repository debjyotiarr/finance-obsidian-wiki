---
type: literature
status: inbox
title: "Marked INAR model and the rough Hawkes--Heston limit"
authors: ["Xiaoyu Wang", "Yingli Wang", "Lingjiong Zhu"]
year: 2026
venue: "arXiv q-fin.CP (2611.29565)"
url: https://arxiv.org/abs/2611.29565
pdf_url: https://arxiv.org/pdf/2611.29565
pdf: 00-Inbox/papers/Wang2026-Marked-INAR-model-and-the-rough-261129565.pdf
swept: 2026-11-24
posted: 2026-11-22
origin: daily sweep script
relevance: high
tags: [options, point-process]
---

# Marked INAR model and the rough Hawkes--Heston limit

## Abstract (verbatim from arXiv)
We develop a discrete-time Monte Carlo algorithm for the rough Hawkes-Heston model based on a nearly unstable marked integer-valued autoregressive (INAR) process. We implement the algorithm with a block fast Fourier transform (FFT) scheme that evaluates the excitation convolution in $O(N\log^2 N)$ operations per path on an $N$-bin grid. We prove joint convergence in law of the spot variance, log price and common marked point measure to their rough Hawkes-Heston limits. We prove convergence of European call and put option prices, as well as convergence of arithmetic Asian and down-and-out put option prices to their continuously monitored values. For European options, the one-year implied volatility smiles computed from the grid transform approach the continuous affine reference across four roughness levels. Monte Carlo experiments on the same three grids compare arithmetic Asian and down-and-out put option prices with a finer-grid reference and demonstrate the efficiency of the proposed algorithm.

## Why staged
Auto-staged by the daily sweep (keyword filter, unreviewed). Possible related notes: [[Hawkes Processes for Order Flow]], [[Implied Volatility Surface Dynamics]].
