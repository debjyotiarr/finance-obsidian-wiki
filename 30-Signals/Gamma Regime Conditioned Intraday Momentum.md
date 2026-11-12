---
type: signal
status: idea
horizon: intraday
assets: [futures, equities]
atoms: ["Gamma Exposure and Dealer Hedging", "Intraday Momentum", "Opening and Closing Auctions"]
tags: [options, momentum, intraday]
created: 2026-11-04
---

# Gamma Regime Conditioned Intraday Momentum

## Hypothesis
The first-half-hour → last-half-hour momentum effect ([[Intraday Momentum]]) is not unconditional: it is concentrated in *short-gamma* dealer regimes, where hedging flows chase the market into the close, and flips toward reversion in long-gamma regimes where dealers fade moves. Conditioning the classic Gao et al. signal on a dealer gamma estimate ([[Gamma Exposure and Dealer Hedging]]) should roughly double its information ratio while cutting exposure on the days the raw signal loses. Mechanism literature: Baltussen et al. (2021) attribute much of intraday momentum to hedging demand.

## Construction
- Universe: ES futures (or SPY) to start; extend to NQ/liquid index products.
- Gamma regime: strike-level open-interest-weighted dealer gamma from OPRA/CBOE open-close data (or a public GEX proxy at first); classify day as short/long/neutral gamma at the open, update mid-day for 0DTE turnover.
- Signal: sign of (open → 15:00) return, traded 15:00 → close, only on short-gamma days; optionally reverse (fade) on strongly long-gamma days.
- Interaction with [[Opening and Closing Auctions]]: exit via MOC order; check whether published auction imbalance already subsumes the effect.

## Economics
- Horizon: ~1 hour hold, ~1 trade/day, so capacity is large in index products; cost hurdle is a single spread + impact on entry (MOC exit is benchmark-neutral).
- Expected edge: Gao et al. report ~6-7 bps/day unconditional pre-cost; conditioning aims to concentrate that into ~40-50% of days.

## Validation plan
- Labels: signed last-hour return; also [[Triple Barrier Labeling]] variant with vol-scaled stops for the tradable version.
- Sample: 2016–present (0DTE era break at 2022 — test stability across it).
- Trials budget: gamma-proxy definition (3 variants) × regime threshold (2) = 6 trials, declared up front per [[Backtest Overfitting and Deflated Sharpe]].
- Kill criteria: effect absent in short-gamma subset post-2022, or subsumed by auction-imbalance data.

## Status log
- 2026-11-04 — created from atom recombination (dry-run of the recombine pass).
