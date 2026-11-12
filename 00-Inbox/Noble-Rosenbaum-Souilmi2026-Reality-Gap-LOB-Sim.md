---
type: literature
status: inbox
title: "Bridging the Reality Gap in Limit Order Book Simulation"
authors: [Noble, Patrick, Rosenbaum, Mathieu, Souilmi, Saad]
year: 2026
venue: arXiv q-fin.TR (2603.24137)
url: https://arxiv.org/abs/2603.24137
pdf_url: https://arxiv.org/pdf/2603.24137
pdf:
swept: 2026-11-03
tags: [orderbook, simulation, large-tick, execution]
---

# Bridging the Reality Gap in Limit Order Book Simulation

## Abstract (summarized — arxiv.org unreachable from this environment; verify at url)
Practical interactive LOB simulator for large-tick assets targeting realistic execution costs and PnL. Reduces book state to spread + volume imbalance for estimability; calibrates event timing to fine-scale temporal structure, reproducing the spike at exchange round-trip latency attributed to simultaneous reactions and latency races. Framed as a four-step recipe: project, estimate, validate, adapt. Submitted 2026-03-25. **Note: outside the 90-day lookback — staged for exceptional fit (Rosenbaum, large-tick focus).**

## Why staged
Backtest-simulator realism is the Achilles heel flagged in [[Backtest Overfitting and Deflated Sharpe]]; the spread-imbalance state ties to [[Microprice]] and [[Tick Size Constraints]], and the latency-race timing spike gives empirical texture to [[Latency Arbitrage]].
