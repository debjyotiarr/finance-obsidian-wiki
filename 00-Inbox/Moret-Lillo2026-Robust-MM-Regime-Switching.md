---
type: literature
status: inbox
title: "Deep Learning of Robust Market Making under Regime-Switching Order Flow"
authors: [Moret, Felipe, Lillo, Fabrizio]
year: 2026
venue: arXiv q-fin.TR (2609.11614)
url: https://arxiv.org/abs/2609.11614
pdf_url: https://arxiv.org/pdf/2609.11614
pdf:
swept: 2026-11-03
tags: [market-making, machine-learning, orderflow, regimes]
---

# Deep Learning of Robust Market Making under Regime-Switching Order Flow

## Abstract (summarized — arxiv.org unreachable from this environment; verify at url)
Argues Avellaneda-Stoikov/GLFT quoting rules break under non-stationary order flow with regimes (plausibly metaorder execution), where they produce negative PnL. Builds a distributional DQN (C51) market maker in a zero-intelligence LOB; identifies inventory saturation under persistent directional flow as the key failure mode; fine-tunes on regime-switching flow using a Bayesian online change-point filter for latent flow bias plus a queue-adjusted quote-exposure imbalance. Reported to substantially restore profitability under regime switching. Submitted 2026-09-10.

## Why staged
Lillo is a core microstructure author. Connects [[Market Maker Inventory Control]] failure modes to [[Trade Sign Autocorrelation]] (metaorder regimes) — the change-point filter on flow bias is a candidate atom of its own.
