---
type: atom
status: seed
domain: mid-frequency
assets: [equities, futures, options]
tags: [events, alpha, volatility]
created: 2026-11-03
---

# News and Announcement Effects

**Idea.** Scheduled announcements (FOMC, CPI, NFP, earnings) concentrate information arrival at known times, producing predictable patterns *around* them even when the content is unpredictable: pre-announcement drift (Lucca & Moench's pre-FOMC equity drift), liquidity withdrawal before release, instantaneous repricing, and elevated-then-decaying volatility after.

**Practical notes.**
- Microstructure behavior around releases is its own regime: spreads widen, depth vanishes, [[Order Flow Toxicity (VPIN)]] spikes. Market-making systems need explicit event calendars and pre-event quote-pulling rules.
- Post-earnings announcement drift (PEAD) remains one of the more durable mid-frequency anomalies; standardized earnings surprise + early reaction predicts weeks of drift.
- Macro surprises transmit through futures first ([[Futures-ETF Lead-Lag]]); option-implied event variance (straddle-implied move) prices the expected jump — rich/cheap vs realized is tradable ([[Variance Risk Premium]] localized to events).

**Related.** [[Intraday Momentum]], [[Order Flow Toxicity (VPIN)]], [[Options Order Flow as Equity Signal]]

**Key references.** Lucca & Moench (2015), *The Pre-FOMC Announcement Drift*; Bernard & Thomas (1989) on PEAD.
