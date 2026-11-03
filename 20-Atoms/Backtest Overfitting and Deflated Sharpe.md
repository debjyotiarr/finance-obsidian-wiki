---
type: atom
status: seed
domain: methodology
assets: [equities, futures, options]
tags: [research-process, statistics, validation]
created: 2026-11-03
---

# Backtest Overfitting and Deflated Sharpe

**Idea.** Trying N strategy variants and reporting the best one guarantees an inflated Sharpe: the expected maximum of N random Sharpes grows like √(2·ln N). Bailey & López de Prado's *Deflated Sharpe Ratio* corrects the observed Sharpe for the number of trials, non-normality, and track length; the companion concept PBO (probability of backtest overfitting) estimates how often the in-sample winner underperforms out-of-sample.

**Practical notes.**
- Log every trial, including abandoned ones — the deflation term needs the true N, which researchers systematically under-report.
- Combinatorially purged cross-validation (CPCV) and walk-forward with embargoes reduce leakage; see [[Triple Barrier Labeling]] for label-driven leakage.
- Microstructure backtests add simulator risk on top: fill assumptions (queue position, latency) can fabricate the entire PnL. Simulate pessimistically ([[Queue Position Value]]).
- A strategy with a mediocre but honest backtest and a clear mechanism beats a spectacular mined one — mechanism is the prior that survives deflation.

**Related.** [[Signal Decay and Alpha Horizon]], [[Triple Barrier Labeling]], [[Limit Order Book Shape as Signal]]

**Key references.** Bailey & López de Prado (2014), *The Deflated Sharpe Ratio*; Harvey, Liu, Zhu (2016), *…and the Cross-Section of Expected Returns*.
