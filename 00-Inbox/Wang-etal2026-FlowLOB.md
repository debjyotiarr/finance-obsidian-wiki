---
type: literature
status: inbox
title: "FlowLOB: Efficient and Controllable Limit Order Book Generation with Flow Matching"
authors: [Wang, Zhuohan, Bacalum, Andreea, Olby, Ollie, Ventre, Carmine, Stillman, Namid]
year: 2026
venue: arXiv cs.LG / q-fin.TR (2608.13096)
url: https://arxiv.org/abs/2608.13096
pdf_url: https://arxiv.org/pdf/2608.13096
pdf:
swept: 2026-11-03
tags: [orderbook, machine-learning, simulation]
---

# FlowLOB: Efficient and Controllable Limit Order Book Generation with Flow Matching

## Abstract (summarized — arxiv.org unreachable from this environment; verify at url)
Conditional flow-matching generator for LOB trajectories, trained on multiple HKEX symbols at 0.1s/1s/10s sampling, using a tick-relative representation that transfers to unseen instruments. Reaches best generation quality in ~10 ODE-solver steps where diffusion models need many more. Goal: simulators combining realistic dynamics, fast sampling, controllable scenarios, and cross-instrument generalization. Submitted 2026-08-13; 8 pp.

## Why staged
LOB simulators are infrastructure for testing everything in [[Limit Order Book Shape as Signal]] and [[Market Maker Inventory Control]]; the tick-relative, transferable representation idea also bears on [[Tick Size Constraints]]. Compare against the Noble-Rosenbaum-Souilmi simulator also staged this sweep.
