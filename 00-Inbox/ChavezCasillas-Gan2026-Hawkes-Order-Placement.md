---
type: literature
status: inbox
title: "Optimal Order Placement under a State-Dependent Hawkes Process Limit Order Book model"
authors: [Chávez Casillas, Jonathan, Gan, Li]
year: 2026
venue: arXiv q-fin.TR (2610.37324)
url: https://arxiv.org/abs/2610.37324
pdf_url: https://arxiv.org/pdf/2610.37324
pdf: 00-Inbox/papers/ChavezCasillas-Gan2026-Hawkes-Order-Placement.pdf
swept: 2026-11-03
tags: [market-making, point-process, orderbook]
---

# Optimal Order Placement under a State-Dependent Hawkes Process LOB model

## Abstract (verbatim from arXiv)
We study optimal quote placement for a market maker facing order flow modeled by a state-dependent Hawkes process. A block-based linear demand specification links market-order counts to execution volumes, providing the demand moments required by a continuous time discrete state dynamic programming formulation. Under a quadratic terminal inventory penalty, we characterize inventory-dependent quotes and derive backward recursions for the coefficients of a quadratic value function. Numerical experiments using LOBSTER data examine quote distributions, inventory exposure, and terminal wealth. The implemented strategy yields higher aggregate terminal wealth than fixed-spread benchmarks at one and three ticks, but lower wealth than the two-tick benchmark. These results illustrate the framework's numerical implementation and distinguish terminal-wealth comparisons from evaluation under the inventory-penalized objective.

## Why staged
Directly extends [[Market Maker Inventory Control]] with realistic arrivals from [[Hawkes Processes for Order Flow]] — exactly the model intersection both atoms flag as the modern direction. LOBSTER calibration makes it testable.
