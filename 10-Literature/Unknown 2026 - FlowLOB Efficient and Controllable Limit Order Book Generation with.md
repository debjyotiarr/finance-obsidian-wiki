---
type: literature
status: skimmed
title: "FlowLOB: Efficient and Controllable Limit Order Book Generation with Flow Matching"
authors: 
year: 2026
venue: arXiv cs.LG / q-fin.TR (2608.13096)
url: https://arxiv.org/abs/2608.13096
pdf: 10-Literature/pdfs/Unknown 2026 - FlowLOB Efficient and Controllable Limit Order Book Generation with.pdf
pages: 9
maths: light
costs_discussed: yes
latency_discussed: no
tags: []
created: 2026-11-16
---

# FlowLOB: Efficient and Controllable Limit Order Book Generation with Flow Matching

> Draft produced by `pipeline/extract.py` (keyword extraction, not read by anyone yet). Quotes are verbatim from the PDF with page numbers. Maths is not extracted; this paper's maths load is **light**.

## One-line summary
*To be written in the refine pass.*

## Abstract
Limit order book (LOB) simulators are most useful to practitioners when they combine realistic market dynamics, computationally efficient sampling, controllable scenario generation, and the ability to generalize beyond the instruments seen during training---properties that existing agent-based and deep generative simulators provide only partially. We present \textbf{FlowLOB}, a conditional \textbf{flow}-matching generator of \textbf{LOB} trajectories, trained on multiple Hong Kong Exchange (HKEX) symbols at three sampling frequencies ($0.1$s, $1$s, $10$s) in tick-relative representation that transfers to unseen instruments. Because flow and diffusion models admit a common formulation, we train both with identical data, architecture, and budget, and sample both through the same fixed-step ODE solvers, yielding a controlled comparison of sampling efficiency and fidelity. Flow matching attains its best quality with only $10$ ODE-solver steps, whereas diffusion needs many more function evaluations to approach the same fidelity. At this efficient operating point, FlowLOB improves realism over baselines, two learned and two agent-based models, in most distributional metrics at the two finer sampling frequencies. We evaluate counterfactual controllability with a distributional test that asks whether changing a scenario condition moves the generated statistic toward the corresponding real tail regime; FlowLOB satisfies this criterion in most tested settings. Both realism and control effects transfer zero-shot on a held-out symbol. We additionally conduct ablation studies on the network architecture and the learning rate.

## Implementation: how it is built
- (p.1) Second, these models are almost universally trained improves realism over baselines, two learned and two agent-based one-model-per-symbol, so nothing can be said about instruments models, in most distributional metrics at the two finer sampling outside the training set.
- (p.1) Our contributions are fourfold: Backtesting a trading strategy, stress-testing an execution algo- rithm, and training a reinforcement-learning agent all require far • Generality.
- (p.3) We use one token, so a target window is represented as 20 × 32 tokens.
- (p.3) Thus market conditioning enters through the token features, generative dynamics and their ease of numerical integration, rather while the generative process time enters through modulation of than a different architecture or sampling budget. the transformer dynamics.
- (p.3) Each sweep varies only the numerical method for that same step. and step count applied to a fixed checkpoint; the training data, con- We use separate learned embeddings for book level and time step, ditioning variables, backbone, and optimizer are unchanged.
- (p.6) We interpret this as a limitation of the current model at coarse sampling frequencies, where the same calendar span provides fewer 0.1s 1s 10s training windows and where returns occupy a wider multi-tick Symbol Channel Sel.
- (p.6) Counterfactual samples replace future step, so their signal is closely aligned with the output tensor. one scenario variable with values drawn from the corresponding For 700.HK, the less reliable cases are concentrated in trend and high or low 5% tail of its training-set distribution, while all other volatility.

## Data used
- (p.1) For each sampling frequency, FlowLOB is trained more market data than history provides: for any instrument, the as a shared simulator across eight HKEX symbols rather market offers exactly one realized path [5, 35].
- (p.1) The tick-relative representa- peated trials and no counterfactuals—no way to observe how the tion enables zero-shot transfer to a ninth held-out symbol same trading day would have unfolded under higher volatility or without retraining, and we repeat the evaluation at 0.1s, 1s, thinner liquidity.
- (p.2) FlowLOB attains 3 Methodology the smallest distance in 30 of the 32 resulting parameter The methodology section has four parts: a matched flow/diffusion combinations at the 0.1s and 1s frequencies, on both the training setup, a common ODE sampling protocol, a tick-relative in-distribution and the held-out symbol. representation for multi-symbol LOB data, and a transformer back- • Controllability.
- (p.2) This pairing lets us compare two ways of learning ments including unseen ones, and outputs L2 book states suitable a transport from noise to realistic book trajectories while holding for snapshot-based policies such as dynamic execution. the data, conditioning, architecture, and optimizer fixed.
- (p.3) At each sampling frequency, we resample the 4 Experimental Results top ten ask and bid levels by taking the first observation in each In this section, we first specify the data, model settings, and basebin and forward-filling empty bins.
- (p.3) This is changes (Sec. 4.4) and ablate the main architectural and optimizaimportant for HKEX data because different symbols can trade at tion choices (Sec. 4.5).
- (p.3) We use level-2 order book data from the Hong Kong Exchange log(𝑉 + 1).

## Costs and frictions
- (p.7) For the backbone giving a practical low-NFE operating point for generating many ablation, we replace the transformer with a UNet of comparable market trajectories across symbols and regimes.

## Latency and infrastructure
**No discussion of latency or infrastructure found. Whether the idea survives realistic delays is untested.**

## Reported results
- (p.4) Once flow solver error is small, more ODE steps mainly integrate the same imperfect vector field more accurately, 10 1 (c) (d) which need not improve distributional quality.

## Section outline
- 4.3 Realism

## Implementation checklist (fill in during refine)
- Signal / decision rule in one line:
- Inputs and data granularity needed:
- Key parameters and how they are set:
- Horizon and turnover:
- Cost assumption vs. what we would actually pay:
- Latency needed for the edge to exist:
- What would break it:

## Atoms extracted
LOB simulators are infrastructure for testing everything in [[Limit Order Book Shape as Signal]] and [[Market Maker Inventory Control]]; the tick-relative, transferable representation idea also bears on [[Tick Size Constraints]]. Compare against the Noble-Rosenbaum-Souilmi simulator also staged this sweep.

## Critique / open questions
