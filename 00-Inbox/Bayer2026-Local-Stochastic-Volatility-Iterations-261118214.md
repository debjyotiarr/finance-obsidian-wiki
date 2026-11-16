---
type: literature
status: inbox
title: "Local Stochastic Volatility Iterations"
authors: ["Christian Bayer", "Denis Belomestny", "Paul P. Hager", "John Schoenmakers"]
year: 2026
venue: "arXiv q-fin.CP (2611.18214)"
url: https://arxiv.org/abs/2611.18214
pdf_url: https://arxiv.org/pdf/2611.18214
pdf: 00-Inbox/papers/Bayer2026-Local-Stochastic-Volatility-Iterations-261118214.pdf
swept: 2026-11-16
posted: 2026-11-13
origin: daily sweep script
relevance: medium
tags: [microstructure, options]
---

# Local Stochastic Volatility Iterations

## Abstract (verbatim from arXiv)
We propose a calibration method for local stochastic volatility models that determines the leverage factor by a fixed-point iteration. Each iteration simulates the model with the current leverage factor and approximates the conditional expectation of the stochastic variance given the spot by a single regression in time and state, with a quasi-likelihood loss for positive responses. The resulting leverage factor is a smooth function of time and spot with relatively few parameters, which can in addition be refined directly against option quotes. We recalibrate the leverage factor to S&P 500 index options on the day of an interest rate announcement, keeping the parameters of a two-factor Bergomi model calibrated four weeks earlier. After five iterations, leverage factors with 63 and 143 coefficients reproduce the implied volatility surface fitted to the quotes within a few basis points over the quoted strikes, the smaller one except in the left wing, and further iterations change them little. A few regularized Gauss-Newton steps against the quotes then bring 87% and 95% of the liquid quotes inside their bid-ask intervals.

## Why staged
Auto-staged by the daily sweep (keyword filter, unreviewed). Possible related notes: [[Implied Volatility Surface Dynamics]], [[Bid-Ask Spread Decomposition]].
