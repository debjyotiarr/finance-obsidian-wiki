---
type: atom
status: seed
domain: microstructure
assets: [equities]
tags: [market-structure, fees, market-making]
created: 2026-11-03
---

# Maker-Taker Fee Economics

**Idea.** Most equity venues rebate liquidity provision and charge liquidity taking (or the inverse). Fees are of the same order as the spread in liquid names, so net-of-fee economics — not the quoted spread — determine where quoting and routing are profitable.

**Practical notes.**
- A one-tick spread in a large-tick name may be entirely rebate-driven: makers quote for the rebate and break even or lose on the spread itself.
- Routing decisions (which venue to post on) trade off rebate size against queue length and fill toxicity — venues attract different flow quality.
- Inverted venues (taker rebate) fill earlier and signal urgency; prints there carry information.
- Fee changes are natural experiments on liquidity supply elasticity.

**Related.** [[Bid-Ask Spread Decomposition]], [[Queue Position Value]], [[Cross-Venue Fragmentation]], [[Tick Size Constraints]]

**Key references.** Colliard & Foucault (2012); Battalio, Corwin, Jennings (2016), *Can Brokers Have It All?*
