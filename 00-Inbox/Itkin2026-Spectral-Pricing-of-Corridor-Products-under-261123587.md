---
type: literature
status: inbox
title: "Spectral Pricing of Corridor Products under Layered Local Volatility"
authors: ["Andrey Itkin", "Dmitry Muravey"]
year: 2026
venue: "arXiv q-fin.CP (2611.23587)"
url: https://arxiv.org/abs/2611.23587
pdf_url: https://arxiv.org/pdf/2611.23587
pdf: 00-Inbox/papers/Itkin2026-Spectral-Pricing-of-Corridor-Products-under-261123587.pdf
swept: 2026-11-19
posted: 2026-11-17
origin: daily sweep script
relevance: low
tags: []
---

# Spectral Pricing of Corridor Products under Layered Local Volatility

## Abstract (verbatim from arXiv)
We price corridor products under a $N$-layered local volatility, piecewise constant in the price and in time, with knock-out barriers. A spatial scale transformation and the GIT method reduce the killed Green's function to a symmetric tridiagonal system of fixed size $N-1$. With equal scaled layer widths the spectrum follows from one tridiagonal eigen-decomposition together with the explicit eigenfunctions that vanish at every interface. For general scaled layer widths an exact counting theorem locates every eigenvalue. Consecutive time intervals of constant volatility are connected by a matrix that re-expands the solution in the eigenbasis of the preceding interval, and the result converges exponentially in the number of retained terms in the eigenfunction expansion. Allowing the killing rate to vary between layers preserves this construction. On a single time interval, the corridor accrual distribution is then recovered by inverting the time and Fourier transforms, without introducing an additional state variable. Exact representations for Greeks and layer vegas follow by differentiation. In our benchmarks the method agrees with independent calculations near rounding error and keeps full accuracy at volatility interfaces, where the tested uniform finite-difference (FD) grids lose one order of convergence. The method computes the accrual law about sixty times faster than the tested FD scheme that includes accrued time as a second state variable.

## Why staged
Auto-staged by the daily sweep (keyword filter, unreviewed). Possible related notes: no obvious match.
