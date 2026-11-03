---
type: atom
status: seed
domain: mid-frequency
assets: [equities, futures]
tags: [anomaly, intraday, alpha]
created: 2026-11-03
---

# Overnight vs Intraday Returns

**Idea.** In US equities, nearly all of the long-run equity premium has accrued overnight (close-to-open), while intraday (open-to-close) returns average near zero or negative — strikingly persistent across decades and many markets. At the single-stock level, overnight and intraday returns have *opposite* cross-sectional predictability (Lou, Polk, Skouras 2019): overnight winners keep winning overnight, intraday reverses.

**Candidate mechanisms.** Clientele differences (retail/institutions trade at different times), opening-auction price pressure, inventory risk premia for holding overnight, short-sale constraints overnight.

**Practical notes.**
- A "tug of war" decomposition of any daily signal into overnight/intraday legs often reveals that the alpha lives in one leg only.
- Execution implication: strategies harvesting the overnight premium concentrate risk in gaps that cannot be stopped out.
- Futures (24h) let you localize exactly *when* in the night the premium accrues.

**Related.** [[Intraday Momentum]], [[Short-Term Reversal]], [[Futures-ETF Lead-Lag]]

**Key references.** Lou, Polk, Skouras (2019), *A Tug of War: Overnight Versus Intraday Expected Returns*; Cliff, Cooper, Gulen on overnight returns.
