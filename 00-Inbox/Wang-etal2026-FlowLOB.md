---
type: literature
status: inbox
title: "FlowLOB: Efficient and Controllable Limit Order Book Generation with Flow Matching"
authors: [Wang, Zhuohan, Bacalum, Andreea, Olby, Ollie, Ventre, Carmine, Stillman, Namid]
year: 2026
venue: arXiv cs.LG / q-fin.TR (2608.13096)
url: https://arxiv.org/abs/2608.13096
pdf_url: https://arxiv.org/pdf/2608.13096
pdf: 00-Inbox/papers/Wang-etal2026-FlowLOB.pdf
swept: 2026-11-03
tags: [orderbook, machine-learning, simulation]
---

# FlowLOB: Efficient and Controllable Limit Order Book Generation with Flow Matching

## Abstract (verbatim from arXiv)
Limit order book (LOB) simulators are most useful to practitioners when they combine realistic market dynamics, computationally efficient sampling, controllable scenario generation, and the ability to generalize beyond the instruments seen during training---properties that existing agent-based and deep generative simulators provide only partially. We present \textbf{FlowLOB}, a conditional \textbf{flow}-matching generator of \textbf{LOB} trajectories, trained on multiple Hong Kong Exchange (HKEX) symbols at three sampling frequencies ($0.1$s, $1$s, $10$s) in tick-relative representation that transfers to unseen instruments. Because flow and diffusion models admit a common formulation, we train both with identical data, architecture, and budget, and sample both through the same fixed-step ODE solvers, yielding a controlled comparison of sampling efficiency and fidelity. Flow matching attains its best quality with only $10$ ODE-solver steps, whereas diffusion needs many more function evaluations to approach the same fidelity. At this efficient operating point, FlowLOB improves realism over baselines, two learned and two agent-based models, in most distributional metrics at the two finer sampling frequencies. We evaluate counterfactual controllability with a distributional test that asks whether changing a scenario condition moves the generated statistic toward the corresponding real tail regime; FlowLOB satisfies this criterion in most tested settings. Both realism and control effects transfer zero-shot on a held-out symbol. We additionally conduct ablation studies on the network architecture and the learning rate.

## Why staged
LOB simulators are infrastructure for testing everything in [[Limit Order Book Shape as Signal]] and [[Market Maker Inventory Control]]; the tick-relative, transferable representation idea also bears on [[Tick Size Constraints]]. Compare against the Noble-Rosenbaum-Souilmi simulator also staged this sweep.
