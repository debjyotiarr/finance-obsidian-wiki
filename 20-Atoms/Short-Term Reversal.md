---
type: atom
status: seed
domain: mid-frequency
assets: [equities]
tags: [reversal, liquidity-provision, alpha]
created: 2026-11-03
---

# Short-Term Reversal

**Idea.** Stocks that underperformed peers over the last few days to a month tend to outperform next period (Jegadeesh 1990, Lehmann 1990). At daily/weekly horizons, reversal is best understood as the *premium for providing liquidity*: you buy what others dumped and carry the inventory until price pressure reverts.

**Practical notes.**
- Returns are gross-cost impressive, net-cost thin: reversal trades against the spread in exactly the names where spreads widened. Costs decide everything — see [[Implementation Shortfall]].
- Stronger after high-volume, high-volatility declines (true price pressure) than after low-volume drift (information). Conditioning on volume/[[Order Flow Imbalance|flow]] separates the two.
- Industry/factor-residual reversal is cleaner than raw-return reversal.
- At intraday horizons it shades into market making; at monthly horizons it flips into momentum.

**Related.** [[Pairs Trading and Statistical Arbitrage]], [[Intraday Momentum]], [[Market Maker Inventory Control]]

**Key references.** Nagel (2012), *Evaporating Liquidity* (reversal profits as liquidity-provision returns); Jegadeesh (1990).
