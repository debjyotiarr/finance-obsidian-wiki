---
type: literature
status: inbox
title: "Quantum Calibration of Local-Volatility Surfaces from Sparse Option Quotes"
authors: ["Kentaro Hoshisashi"]
year: 2026
venue: "arXiv q-fin.CP (2611.25344)"
url: https://arxiv.org/abs/2611.25344
pdf_url: https://arxiv.org/pdf/2611.25344
pdf: 00-Inbox/papers/Hoshisashi2026-Quantum-Calibration-of-Local-Volatility-Surfaces-261125344.pdf
swept: 2026-11-20
posted: 2026-11-19
origin: daily sweep script
relevance: low
tags: []
---

# Quantum Calibration of Local-Volatility Surfaces from Sparse Option Quotes

## Abstract (verbatim from arXiv)
Calibrating a volatility surface from sparse option prices requires repeated solutions of a pricing equation as the volatility parameters change. We implement a hybrid quantum and classical method for this inverse problem using the Dupire local-volatility model. A positive coefficient representation specifies the local variance, and linear combinations of Hamiltonian simulations approximate the associated pricing evolution. The circuit propagates through successive maturity intervals and evaluates discrepancies at the observed strikes. Measurement counts provide the objective values used by a classical optimiser to update the volatility coefficients. We implement this calibration cycle in a logical gate simulator and assess it alongside classical pricing solvers and alternative surface models. Multiple-maturity synthetic examples illustrate the reconstruction of smiles and skews, while a separate small circuit experiment tests the complete measured calibration. The comparisons quantify the effects of model flexibility, pricing approximation and measurement precision. Recorded gate counts and sampling budgets identify the main computational costs of the implementation.

## Why staged
Auto-staged by the daily sweep (keyword filter, unreviewed). Possible related notes: no obvious match.
