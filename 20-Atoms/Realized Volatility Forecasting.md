---
type: atom
status: seed
domain: mid-frequency
assets: [equities, futures, options]
tags: [volatility, forecasting, modeling]
created: 2026-11-03
---

# Realized Volatility Forecasting

**Idea.** Volatility is the most forecastable quantity in finance. Realized variance computed from intraday returns is a near-observable; the HAR model (Corsi 2009) — regressing tomorrow's RV on daily, weekly, and monthly average RV — captures the long-memory cascade with three coefficients and is brutally hard to beat.

**Why it matters everywhere.** Volatility forecasts size positions, set [[Triple Barrier Labeling|barrier widths]], price options (input to [[Variance Risk Premium]] measurement), schedule execution, and gate market-making aggressiveness ([[Market Maker Inventory Control]]).

**Practical notes.**
- Sampling: 5-minute returns balance microstructure noise against efficiency; realized kernels / pre-averaging handle higher frequencies.
- Separate continuous and jump components (bipower variation) — jumps don't forecast future vol the way the continuous part does.
- Overnight gaps need explicit handling (ties to [[Overnight vs Intraday Returns]]).
- Implied vol is a biased but informative forecast; blending implied + HAR beats either alone.

**Related.** [[Variance Risk Premium]], [[Volume Clock]], [[Hawkes Processes for Order Flow]]

**Key references.** Corsi (2009), *A Simple Approximate Long-Memory Model of Realized Volatility*; Andersen, Bollerslev, Diebold, Labys (2003).
