---
type: atom
status: seed
domain: microstructure
assets: [equities, futures]
tags: [impact, execution, information]
created: 2026-11-03
---

# Price Impact and Kyle's Lambda

**Idea.** Trades move prices in proportion to their size relative to available liquidity. Kyle (1985) derived a linear impact model: Δp = λ · (signed order flow), where λ measures market depth and rises with the information content of flow relative to noise-trader volume.

**Why it matters.** λ is simultaneously a *cost* (for execution) and a *signal input* (impact of others' flow is what [[Order Flow Imbalance]] exploits). Estimating λ per instrument and regime is foundational for both.

**Practical notes.**
- Empirically, impact of metaorders is concave, not linear — see [[Square-Root Law of Market Impact]].
- λ varies intraday (high at open, low at close for equities) and spikes when depth is withdrawn.
- Permanent vs temporary impact split drives optimal execution — see [[Optimal Execution (Almgren-Chriss)]].

**Related.** [[Order Flow Imbalance]], [[Square-Root Law of Market Impact]], [[Optimal Execution (Almgren-Chriss)]], [[Order Flow Toxicity (VPIN)]]

**Key references.** Kyle (1985), *Continuous Auctions and Insider Trading*; Hasbrouck (2007), *Empirical Market Microstructure*.
