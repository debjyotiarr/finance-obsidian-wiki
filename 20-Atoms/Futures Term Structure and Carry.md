---
type: atom
status: seed
domain: mid-frequency
assets: [futures]
tags: [carry, term-structure, alpha]
created: 2026-11-03
---

# Futures Term Structure and Carry

**Idea.** The shape of the futures curve (basis between contracts, and between front contract and spot) predicts returns: backwardated markets tend to deliver positive roll returns to longs, contangoed ones negative. "Carry" — the return if prices stay unchanged — is a robust cross-asset predictor (Koijen et al. 2018).

**Practical notes.**
- Calendar-spread dynamics around roll periods are a microstructure phenomenon of their own: predictable index-fund roll flow (the "Goldman roll") creates temporary pressure in the deferred contract.
- For equity index futures, the basis embeds funding/dividend expectations; basis dislocations vs fair value signal balance-sheet stress or flow pressure and mean-revert.
- Roll scheduling interacts with liquidity migration between contracts — volume shifts to the back contract over a few days; signals calibrated on the front contract break during the roll.

**Related.** [[Pairs Trading and Statistical Arbitrage]], [[Futures-ETF Lead-Lag]], [[Variance Risk Premium]]

**Key references.** Koijen, Moskowitz, Pedersen, Vrugt (2018), *Carry*; Mou (2010) on index roll congestion.
