---
type: atom
status: seed
domain: microstructure
assets: [equities, futures]
tags: [orderflow, empirical-law, impact]
created: 2026-11-03
---

# Trade Sign Autocorrelation

**Idea.** The signs of market orders are positively autocorrelated with very long memory — the autocorrelation of buy/sell signs decays as a slow power law over thousands of trades. Yet prices remain close to a martingale.

**Why.** Long memory comes from order splitting: institutions slice metaorders over hours or days. The market stays efficient because liquidity providers adjust quotes asymmetrically — predictable flow earns no easy profit, but the *interaction* of persistent flow with impact shapes everything.

**Practical notes.**
- Implication for signals: raw "trades were net buy" indicators are mostly stale metaorder flow; the alpha is in flow *surprises* relative to the predictable component.
- Implication for execution: your own child orders leak information; randomization and schedule noise matter.
- Propagator models (Bouchaud) reconcile long-memory flow with diffusive prices.

**Related.** [[Order Flow Imbalance]], [[Square-Root Law of Market Impact]], [[Order Flow Toxicity (VPIN)]]

**Key references.** Bouchaud, Gefen, Potters, Wyart (2004); Lillo & Farmer (2004), *The Long Memory of the Efficient Market*.
