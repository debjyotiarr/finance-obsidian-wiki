---
type: literature
status: inbox
title: "Deep Learning of Robust Market Making under Regime-Switching Order Flow"
authors: [Moret, Felipe, Lillo, Fabrizio]
year: 2026
venue: arXiv q-fin.TR (2609.11614)
url: https://arxiv.org/abs/2609.11614
pdf_url: https://arxiv.org/pdf/2609.11614
pdf: 00-Inbox/papers/Moret-Lillo2026-Robust-MM-Regime-Switching.pdf
swept: 2026-11-03
tags: [market-making, machine-learning, orderflow, regimes]
---

# Deep Learning of Robust Market Making under Regime-Switching Order Flow

## Abstract (verbatim from arXiv)
Classical market-making strategies based on stochastic control, such as the Avellaneda--Stoikov and the Guéant--Lehalle--Fernandez-Tapia (GLFT) extension, provide closed-form quoting approximations, but rest on assumptions that break down at realistic microstructure timescales. One of them is that order flow is stationary, while empirical evidence points to the existence of regimes, possibly associated with algorithmic execution of metaorders. In our experiments, persistent directional flow makes stationary controllers unprofitable. In this paper, we develop a deep reinforcement-learning market maker (RLMM)---a Rainbow-style distributional deep Q-network which is calibrated and tested in a zero-intelligence limit order book. We find that, in the stationary setting, RLMM outperforms GLFT at comparable levels of profit and loss (PnL) dispersion. The stationarily trained RLMM is more robust to flow asymmetry than GLFT, but still suffers inventory saturation and large drawdowns under persistent directional flow. Training a separate RLMM under regime-switching flow, with a Bayesian flow-belief signal and a queue-adjusted quote exposure signal, restores positive mean PnL in our experiments. A final scenario-bandit step prioritizes low-return scenarios and improves performance under varying regime persistence and directional correlation.

## Why staged
Lillo is a core microstructure author. Connects [[Market Maker Inventory Control]] failure modes to [[Trade Sign Autocorrelation]] (metaorder regimes) — the change-point filter on flow bias is a candidate atom of its own.
