---
type: literature
status: inbox
title: "TAPES: Terminal Adjoint-Propagated Error Scheduling for Financial Diffusion Samplers"
authors: ["Yilie Huang"]
year: 2026
venue: "arXiv q-fin.CP (2611.16484)"
url: https://arxiv.org/abs/2611.16484
pdf_url: https://arxiv.org/pdf/2611.16484
pdf:
swept: 2026-11-15
posted: 2026-11-12
origin: daily sweep script
relevance: low
tags: []
---

# TAPES: Terminal Adjoint-Propagated Error Scheduling for Financial Diffusion Samplers

## Abstract (verbatim from arXiv)
Financial diffusion samplers are often reused with a small number of function evaluations (NFE) inside scenario and risk pipelines, where numerical time-grid error can distort terminal quantities such as covariances, tails, and drawdown proxies. We study offline grid construction for a frozen probability-flow ODE: the score network, conditioning, Euler solver, report normalization, and deployment NFE remain fixed. TAPES (Terminal Adjoint-Propagated Error Scheduling) estimates signed local defects by Richardson comparisons, transports them through the remaining discrete flow and a terminal-report adjoint, and optimizes the squared norm of their sum before a capped direct refinement. We show that this transported signed sum is the first-order terminal-report error and quantify, under an aligned-defect model, the inefficiency of diagonal criteria. Across six budgets on a regime-switching simulation and chronologically held-out Mag7 contexts, TAPES gives the lowest design- and audit-report errors in all 24 dataset--budget--report rows within the reported five-pipeline panel. Cross-budget mean relative audit-error reductions are about 10--11% on Regime-SV and about 1% on Mag7, with Bonferroni intervals excluding zero; all displayed winners persist under a doubled-resolution reference, and a small Regime-SV Heun probe preserves the TAPES-first audit ordering. TAPES changes only the offline schedule and retains the prescribed deployment NFE; claims concern numerical fidelity to frozen generators.

## Why staged
Auto-staged by the daily sweep (keyword filter, unreviewed). Possible related notes: no obvious match.
