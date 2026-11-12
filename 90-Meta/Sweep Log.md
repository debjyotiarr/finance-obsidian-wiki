---
type: meta
tags: [meta, ingestion, log]
created: 2026-11-12
---

# Sweep Log

Every paper any sweep has staged, one row each, newest last. **Idea** is the paper's core claim in one line — what it would add to the vault — not the abstract. The full stub (abstract, links, relevance) is in `00-Inbox/` until reviewed.

## Papers

| Date | Paper | Idea |
|---|---|---|
| 2026-11-03 | Chávez Casillas & Gan — [Optimal Order Placement under a State-Dependent Hawkes LOB](https://arxiv.org/abs/2610.37324) | Market-making quotes when market-order arrivals follow a state-dependent Hawkes process instead of Poisson. |
| 2026-11-03 | Cheridito & Weiss — [Multi-Level Market Making with RL](https://arxiv.org/abs/2608.18195) | RL market maker quoting across several book levels, with queue position in the state. |
| 2026-11-03 | Moret & Lillo — [Robust Market Making under Regime-Switching Order Flow](https://arxiv.org/abs/2609.11614) | Classic MM rules lose money under directional flow regimes; change-point detection on flow bias restores PnL. |
| 2026-11-03 | Yang & Xu — [Adversarial RL MM with Hawkes Flow and Impact](https://arxiv.org/abs/2609.22785) | Adversarial training makes RL market makers robust to self-exciting flow and price impact. |
| 2026-11-03 | Wang et al. — [FlowLOB](https://arxiv.org/abs/2608.13096) | Flow-matching generator for realistic LOB paths that transfers to unseen instruments. |
| 2026-11-03 | Noble, Rosenbaum & Souilmi — [Bridging the Reality Gap in LOB Simulation](https://arxiv.org/abs/2603.24137) | Large-tick LOB simulator on spread + imbalance state that reproduces realistic execution costs and latency races. |
| 2026-11-03 | Prakash et al. — [FOMO: FLEX Options and Market Outcomes](https://arxiv.org/abs/2610.13044) | Customised FLEX option trades spill into listed-option open interest; unsigned gamma doesn't predict IV. |
| 2026-11-03 | Deng & Zhang — [Lead-Lag Clustering Comparison](https://arxiv.org/abs/2608.24703) | Benchmarks clustering methods for finding leader/lagger groups across a universe; KShape beats DTW. |
| 2026-11-03 | Barzykin, Boyce, Neuman & Tuschmann — [Optimal Execution with Passive Market Impact](https://arxiv.org/abs/2607.28323) | Executing with limit orders has its own impact; optimal passive schedule sits nearer TWAP under transient impact. |

## Runs

| Date | Lookback | Staged | Sites (direct / search fallback / unreachable) | Notes |
|---|---|---|---|---|
| 2026-11-03 | ~2026-08-05 → 2026-11-03 | 9 | arXiv: search fallback | Manual dry run, strict filter. arxiv.org blocked by network policy; no PDFs. 5 borderline papers skipped. |
