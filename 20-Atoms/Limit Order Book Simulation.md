---
type: atom
status: seed
domain: methodology
assets: [equities, futures]
tags: [simulation, orderbook, research-process, machine-learning]
created: 2026-11-16
---

# Limit Order Book Simulation

**Idea.** History gives one realised path per instrument, so strategies that depend on the order book are tested on simulated books. A simulator is only as useful as two properties: whether its output looks like a real market, and whether it *reacts* to the orders you place. Most simulators have one property and not the other.

**The two families.**
- **Agent-based / model-based** (zero-intelligence traders, [[Hawkes Processes for Order Flow|Hawkes order flow]], ABIDES): interactive by construction, since your order enters the same matching engine. Transparent and steerable, but they reproduce only some features of real markets.
- **Learned generators** (GANs, autoregressive event models, diffusion, flow matching): much closer to real data on distributional tests, but many generate book *snapshots* conditioned on the past and do not respond to your orders at all.

**Practical notes.**
- **Match the simulator to the strategy.** Market making and anything queue-dependent needs an interactive, event-level simulator with fills ([[Queue Position Value]]). Snapshot generators are only valid for logic that reads the book without materially moving it.
- **Distributional realism is not backtest realism.** A generator can match price and volume distributions and still give wrong strategy PnL. The test that matters is whether a known strategy earns in simulation what it earned live. Few papers run it. Unrealistic fills are a main route to fabricated results ([[Backtest Overfitting and Deflated Sharpe]]).
- **Tick-relative inputs transfer across instruments.** Expressing prices as mid change and level gaps in ticks, and volumes in logs, let one model work on a symbol it never saw (Wang et al. 2026). See [[Tick Size Constraints]].
- **Sampling cost matters at scale.** Flow matching reached its best quality in 10 network evaluations per window, where diffusion needed far more (Wang et al. 2026).
- **Time grid.** Generators on a 0.1 s or coarser grid say nothing about sub-100 ms dynamics.
- **Steering.** Conditioning on liquidity and imbalance works reliably; conditioning on trend is weak (Wang et al. 2026). Useful for stress scenarios, not for generating directional paths.

**Related.** [[Backtest Overfitting and Deflated Sharpe]], [[Hawkes Processes for Order Flow]], [[Queue Position Value]], [[Tick Size Constraints]], [[Limit Order Book Shape as Signal]]

**Key references.** Wang et al. (2026), *FlowLOB* — see the literature note [[Wang et al 2026 - FlowLOB Efficient and Controllable Limit Order Book Generation with]]; Byrd, Hybinette, Balch (2020), *ABIDES*; Vyetrenko et al. (2020), *Get Real: Realism Metrics for Robust Limit Order Book Market Simulations*.
