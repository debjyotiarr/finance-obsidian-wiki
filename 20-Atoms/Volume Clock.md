---
type: atom
status: seed
domain: microstructure
assets: [equities, futures]
tags: [sampling, modeling, volatility]
created: 2026-11-03
---

# Volume Clock

**Idea.** Markets do not run on clock time: information arrives in bursts and activity clusters. Sampling by volume (or trade count, or dollar value) instead of seconds yields returns that are closer to i.i.d. Gaussian and signals that are stable across slow and frantic regimes.

**Why it works.** Volatility is roughly proportional to trading activity (mixture-of-distributions hypothesis). Subordinating the price process to a volume clock absorbs the activity fluctuations that make clock-time returns heavy-tailed and heteroskedastic.

**Practical notes.**
- Volume bars / dollar bars / imbalance bars (López de Prado) are the standard constructions; imbalance bars sample faster when flow turns one-sided.
- Most microstructure estimators (e.g., [[Order Flow Toxicity (VPIN)]]) and many ML pipelines work better on volume-sampled data.
- Caution: volume itself is forecastable intraday (U-shape); mixing clock-based features with volume-sampled labels leaks.

**Related.** [[Order Flow Toxicity (VPIN)]], [[Hawkes Processes for Order Flow]], [[Intraday Momentum]], [[Triple Barrier Labeling]]

**Key references.** Clark (1973); Ané & Geman (2000); López de Prado (2018), *Advances in Financial Machine Learning*, ch. 2.
