---
type: literature
status: inbox
title: "Bridging the Reality Gap in Limit Order Book Simulation"
authors: [Noble, Patrick, Rosenbaum, Mathieu, Souilmi, Saad]
year: 2026
venue: arXiv q-fin.TR (2603.24137)
url: https://arxiv.org/abs/2603.24137
pdf_url: https://arxiv.org/pdf/2603.24137
pdf: 00-Inbox/papers/Noble-Rosenbaum-Souilmi2026-Reality-Gap-LOB-Sim.pdf
swept: 2026-11-03
tags: [orderbook, simulation, large-tick, execution]
---

# Bridging the Reality Gap in Limit Order Book Simulation

## Abstract (verbatim from arXiv)
We introduce a practical, interactive simulator of the limit order book for large-tick assets, designed to produce realistic execution, costs, and P&L. The book state is projected onto a tractable representation based on spread and volume imbalance, enabling robust estimation from market data. Event timing is calibrated to reproduce the fine-scale temporal structure of real markets, revealing a pronounced mode at exchange round-trip latency consistent with simultaneous reactions and latency races among participants. We further incorporate a feedback mechanism that accumulates signed trade flow through a power-law decay kernel, reproducing both concave market impact during execution and partial post-trade reversion. Across several stocks and strategy case studies, the simulator yields realistic behavior where profitability becomes highly sensitive to execution parameters. We present the approach as a practical recipe: project, estimate, validate, adapt, for building realistic limit order book simulations.

## Why staged
Backtest-simulator realism is the Achilles heel flagged in [[Backtest Overfitting and Deflated Sharpe]]; the spread-imbalance state ties to [[Microprice]] and [[Tick Size Constraints]], and the latency-race timing spike gives empirical texture to [[Latency Arbitrage]].
