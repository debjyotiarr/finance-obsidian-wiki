---
type: signal
status: idea
horizon: seconds
assets: [futures, equities]
atoms: ["Order Flow Imbalance", "Order Flow Toxicity (VPIN)", "Microprice", "Volume Clock"]
tags: [orderflow, hft, orderbook]
created: 2026-11-04
---

# OFI Gated by Flow Toxicity

## Hypothesis
[[Order Flow Imbalance]] predicts short-horizon returns on average, but its errors are not uniform: when flow is toxic (informed metaorder executing — high [[Order Flow Toxicity (VPIN)]]), OFI-based mean-reversion entries get run over, while OFI-based continuation works better. A two-regime signal — follow OFI with larger size in low-toxicity regimes for liquidity-provision-style capture, switch to continuation/stand-aside in high-toxicity regimes — should beat unconditional OFI on both PnL and tail risk.

## Construction
- Universe: ES futures first (clean single venue, large tick), then liquid large-tick equities.
- OFI: level-1 (optionally 3-level) signed flow per [[Volume Clock]] bucket, normalized by average depth; fair value from [[Microprice]].
- Toxicity gate: rolling VPIN over N volume buckets, *volatility-adjusted* (regress out realized vol; use the residual per the Andersen-Bondarenko critique).
- Trade rule: quote/lean with OFI when residual-VPIN below threshold; reduce size or require stronger OFI confirmation above it.

## Economics
- Horizon: seconds to ~1 minute; this is an HFT-class signal — viability depends on queue position and latency, not just the forecast ([[Queue Position Value]]).
- Edge per trade is sub-tick: fee/rebate structure and fill simulation realism decide everything. Capacity small; this is a market-making enhancer, not a standalone book.

## Validation plan
- Simulator realism first: queue-position-aware fills, pessimistic latency (the Noble-Rosenbaum-Souilmi large-tick simulator staged in the inbox is directly on point).
- Labels: [[Triple Barrier Labeling]] on volume bars; purged CV.
- Trials budget: VPIN window (2) × gate threshold (3) × OFI depth (2) = 12 trials declared.
- Kill criteria: edge disappears under one-tick adverse fill assumption, or gate adds nothing over a plain volatility filter.

## Status log
- 2026-11-04 — created from atom recombination (dry-run of the recombine pass).
