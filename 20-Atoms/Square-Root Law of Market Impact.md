---
type: atom
status: seed
domain: microstructure
assets: [equities, futures]
tags: [impact, execution, empirical-law]
created: 2026-11-03
---

# Square-Root Law of Market Impact

**Idea.** The expected impact of a metaorder of size Q is proportional to σ·√(Q/V) — square root in size, not linear. This holds remarkably universally across asset classes, venues, and decades (Bouchaud and collaborators; ANcerno/CFM datasets).

**Why it works (candidate explanations).** Latent liquidity theory: the visible book is a tiny fraction of true supply/demand, which is distributed so that impact is concave. Slow replenishment of liquidity near the price creates a locally linear-in-√ shape.

**Practical notes.**
- Implies cost per share *falls* with participation spread over time — the basis of schedule-based execution.
- Impact partially reverts after the metaorder ends (temporary component ~2/3 in many studies).
- Use it to sanity-check capacity estimates for any mid-frequency signal — see [[Signal Decay and Alpha Horizon]].

**Related.** [[Price Impact and Kyle's Lambda]], [[Optimal Execution (Almgren-Chriss)]], [[Implementation Shortfall]]

**Key references.** Tóth et al. (2011), *Anomalous Price Impact and the Critical Nature of Liquidity*; Bouchaud, Bonart, Donier, Gould (2018), *Trades, Quotes and Prices*.
