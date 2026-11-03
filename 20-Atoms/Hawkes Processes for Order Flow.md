---
type: atom
status: seed
domain: microstructure
assets: [equities, futures]
tags: [modeling, orderflow, point-process]
created: 2026-11-03
---

# Hawkes Processes for Order Flow

**Idea.** Order arrivals are self- and cross-exciting: a trade raises the short-term probability of further trades (same and opposite side), cancellations trigger cancellations, etc. Hawkes processes — point processes whose intensity jumps on each event and decays — capture this clustering and give a tractable generative model of the order flow.

**Why it's useful.**
- Forecasting event intensity → short-horizon volatility and fill-probability estimates.
- The branching ratio (fraction of events caused by other events) measures market *reflexivity*; estimates near 1 indicate highly endogenous activity (flash-crash-prone regimes).
- Cross-excitation kernels between buy/sell/cancel events give an interpretable decomposition of book dynamics.

**Practical notes.**
- Exponential kernels fit fast and are usually enough; power-law kernels fit the data better but complicate estimation.
- Useful as a simulator for testing market-making logic before live data — complements [[Limit Order Book Shape as Signal]].

**Related.** [[Order Flow Imbalance]], [[Trade Sign Autocorrelation]], [[Volume Clock]]

**Key references.** Bacry, Mastromatteo, Muzy (2015), *Hawkes Processes in Finance*; Hardiman, Bercot, Bouchaud (2013) on reflexivity.
