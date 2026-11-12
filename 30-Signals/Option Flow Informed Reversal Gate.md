---
type: signal
status: idea
horizon: 1-5 days
assets: [equities, options]
atoms: ["Options Order Flow as Equity Signal", "Short-Term Reversal", "Order Flow Imbalance"]
tags: [options, reversal, cross-asset]
created: 2026-11-04
---

# Option Flow Informed Reversal Gate

## Hypothesis
[[Short-Term Reversal]] profits are liquidity-provision income, and its losses come from fading moves that were *informed*. Option flow is a visible footprint of informed trading ([[Options Order Flow as Equity Signal]]): a stock that dropped on elevated, directionally consistent option activity (high O/S ratio, opening put buys, skew steepening) is being repriced, not pressured. Gating the reversal signal — fade only moves *not* accompanied by informed option flow — should remove the left tail of reversal PnL and raise its net Sharpe.

## Construction
- Universe: optionable US equities with liquid chains (top ~800 by option volume).
- Reversal leg: 3-5 day industry-residual return, standard construction.
- Gate per name: O/S volume ratio z-score, signed option flow (open-buy puts minus calls, from open/close flags or quote-rule classification), and 1-day change in 25-delta put skew. Any two of three elevated → informed → do not fade (optionally follow).
- Secondary check: equity-side [[Order Flow Imbalance]] persistence as a cheaper informed-flow proxy where option data is thin.

## Economics
- Horizon: 1-5 days, weekly turnover high (reversal's known weakness) — the gate should *reduce* turnover by dropping ~20-30% of entries, directly cutting cost per [[Implementation Shortfall]].
- Edge target: unconditional residual reversal ≈ 2-4 bps/day gross in liquid names; the gate's value is mostly loss avoidance, so judge on net Sharpe and drawdown, not mean return.

## Validation plan
- Labels: forward residual return and [[Triple Barrier Labeling]] with vol-scaled barriers.
- Sample: 2015–present; separate pre/post-2020 (retail option flow regime change — classify retail flow out if possible).
- Trials budget: gate definitions (3) × thresholds (2) = 6 declared.
- Kill criteria: gate indistinguishable from a plain earnings/news-event filter, or turnover reduction fails to show up net.

## Status log
- 2026-11-04 — created from atom recombination (dry-run of the recombine pass).
