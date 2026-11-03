---
type: atom
status: seed
domain: methodology
assets: [equities, futures, options]
tags: [research-process, alpha, capacity]
created: 2026-11-03
---

# Signal Decay and Alpha Horizon

**Idea.** Every signal has two clocks: the *horizon* over which one observation predicts returns (its autocorrelation/IC decay curve), and the *lifetime* over which the strategy works before crowding and publication kill it. Both must be measured, not assumed.

**Horizon.** Plot IC (signal-return correlation) against forward horizon. The decay curve sets turnover, required execution speed, and cost tolerance: a 30-second-half-life signal is an HFT business ([[Order Flow Imbalance]]); a 2-week half-life is a stat-arb business.

**Lifetime.** McLean & Pontiff (2016): published anomaly returns drop ~32% out-of-sample and ~58% post-publication. Microstructure edges decay faster — they are capacity-constrained and directly competed.

**Practical notes.**
- Combine signals at the *forecast* level with horizon-matched weights, not at the position level.
- Capacity ≈ (alpha per trade) / (impact per dollar) — use [[Square-Root Law of Market Impact]] for the denominator.
- Monitor live decay explicitly; retire signals by rule, not sentiment.

**Related.** [[Backtest Overfitting and Deflated Sharpe]], [[Implementation Shortfall]], [[Triple Barrier Labeling]]

**Key references.** McLean & Pontiff (2016), *Does Academic Research Destroy Stock Return Predictability?*
