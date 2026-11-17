---
type: literature
status: inbox
title: "PIRanNN: Random-Feature Pricing and Calibration under Jump-Diffusion and Stochastic-Volatility Models"
authors: ["Saurabh Bansal", "Srikanth K. Iyer", "Shashi Jain"]
year: 2026
venue: "arXiv q-fin.CP (2611.19792)"
url: https://arxiv.org/abs/2611.19792
pdf_url: https://arxiv.org/pdf/2611.19792
pdf: 00-Inbox/papers/Bansal2026-PIRanNN-Random-Feature-Pricing-and-Calibration-261119792.pdf
swept: 2026-11-17
posted: 2026-11-15
origin: daily sweep script
relevance: low
tags: []
---

# PIRanNN: Random-Feature Pricing and Calibration under Jump-Diffusion and Stochastic-Volatility Models

## Abstract (verbatim from arXiv)
We study a random-feature method for pricing and calibrating European options under jump-diffusion (Merton, Kou) and stochastic-volatility (Heston, SABR) models. The network has one hidden layer with a probit activation and fixed random inner weights, so fitting it to the pricing equation, the payoff and the boundary conditions is a single regularised least-squares problem, with no iterative training. For Merton and Kou the jump integral of each feature is explicit, so no quadrature is needed. One factorisation of the least-squares matrix gives the price at every state and time, its Greeks, and the exact derivatives of the prices with respect to the model parameters for gradient-based calibration. For the jump models, subtracting the Black-Scholes price removes the payoff kink and reduces the pricing error by about two orders of magnitude. The method is then about as accurate as a standard Crank-Nicolson finite-difference scheme at the same run time, although a finite-difference scheme that also subtracts the Black-Scholes price is about two orders of magnitude more accurate still. On the test problems of a recent physics-informed neural network study, the method matches that network's accuracy in seconds instead of about half an hour. The calibration experiments show that a solver can fit the quotes and still return wrong parameters when its pricing error is not small compared with the effect of the parameters on the prices: without the subtraction the solver misses the jump parameters by up to 50%, and with it they are recovered to within 3%. For Heston and SABR, used as an applicability study with boundary conditions that need no reference prices, pricing errors are about one percent and the calibrated parameters are within about 15% of the true values.

## Why staged
Auto-staged by the daily sweep (keyword filter, unreviewed). Possible related notes: no obvious match.
