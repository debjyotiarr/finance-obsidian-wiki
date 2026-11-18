---
type: literature
status: inbox
title: "Beyond Strike Remapping: Conditional-Gamma Pricing of Leveraged ETF Options under Local Volatility"
authors: ["Guolin Chen", "Jiang Zhou", "Richard Ma", "Xia Sheng", "Anson Tse", "Terry Wei"]
year: 2026
venue: "arXiv q-fin.CP (2611.22604)"
url: https://arxiv.org/abs/2611.22604
pdf_url: https://arxiv.org/pdf/2611.22604
pdf: 00-Inbox/papers/Chen2026-Beyond-Strike-Remapping-Conditional-Gamma-Pricing-261122604.pdf
swept: 2026-11-18
posted: 2026-11-17
origin: daily sweep script
relevance: medium
tags: [microstructure, options]
---

# Beyond Strike Remapping: Conditional-Gamma Pricing of Leveraged ETF Options under Local Volatility

## Abstract (verbatim from arXiv)
Options on leveraged ETFs (LETFs) are priced and hedged off the LETF volatility surface, but path-dependent variance drag makes that surface difficult to build consistently with the underlying index smile. We study three methods for constructing it: a closed-form first-order strike remapping, a new conditional-Gamma method, and a two-dimensional joint-law PDE that makes no distributional assumption and serves as the benchmark. The conditional-Gamma method is our main contribution. It conditions on the terminal underlying return, which preserves the state dependence of variance drag that a single remapped strike discards. Three one-dimensional forward PDEs under a calibrated local-volatility model give the conditional mean and variance of integrated variance, and a Gamma law matched to these moments keeps realised variance non-negative and prices the option in closed form. A shifted-Gamma variant that also matches the conditional third moment gives its clearest gains for inverse products at longer maturities, and a Gamma-mixture extension covers the full range of conditional skewness compatible with non-negative realised variance. On S&P 500 and Nikkei 225 surfaces the conditional-Gamma smile tracks the benchmark closely at every leverage tested, including the wings where the strike remapping drifts. A full LETF smile takes 0.85-1.42 seconds against 197-224 seconds for the benchmark, a 158- to 236-fold speed-up. Against listed TQQQ quotes the conditional-Gamma smile lies inside the market bid-ask at most strikes.

## Why staged
Auto-staged by the daily sweep (keyword filter, unreviewed). Possible related notes: [[Gamma Exposure and Dealer Hedging]], [[Bid-Ask Spread Decomposition]].
