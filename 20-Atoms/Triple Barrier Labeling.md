---
type: atom
status: seed
domain: methodology
assets: [equities, futures]
tags: [machine-learning, labeling, research-process]
created: 2026-11-03
---

# Triple Barrier Labeling

**Idea.** Fixed-horizon labels ("return over next k bars") ignore how trades actually end — at profit targets, stop losses, or time exits. López de Prado's triple-barrier method labels each observation by which of three barriers is touched first: upper (profit), lower (stop), vertical (time). Labels then match the strategy's real exit logic, and barrier widths scale with current volatility.

**Meta-labeling.** Train a primary model (or rule) for *direction*, then a secondary model on triple-barrier outcomes to predict whether each primary signal should be *taken* and at what size. Separating side from size improves precision and is a clean way to add ML on top of interpretable signals.

**Practical notes.**
- Overlapping labels are serially dependent: weight samples by uniqueness and purge/embargo in cross-validation, or metrics are inflated — see [[Backtest Overfitting and Deflated Sharpe]].
- Works naturally on volume-sampled bars — see [[Volume Clock]].

**Related.** [[Backtest Overfitting and Deflated Sharpe]], [[Volume Clock]], [[Signal Decay and Alpha Horizon]]

**Key references.** López de Prado (2018), *Advances in Financial Machine Learning*, ch. 3.
