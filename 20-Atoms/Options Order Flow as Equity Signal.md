---
type: atom
status: seed
domain: options
assets: [options, equities]
tags: [orderflow, options, alpha, cross-asset]
created: 2026-11-03
---

# Options Order Flow as Equity Signal

**Idea.** Informed traders prefer options for leverage and embedded downside limits, so option order flow leads stock prices. The option-to-stock volume ratio (O/S, Roll–Schwartz–Subrahmanyam; Johnson & So 2012) and signed option flow predict cross-sectional equity returns over days; put-call implied-vol skew shifts predict news outcomes.

**Mechanisms.** Leverage attracts information; market makers who take the other side hedge in the underlying, mechanically transmitting the flow — which also connects to [[Gamma Exposure and Dealer Hedging]].

**Practical notes.**
- Signed flow matters more than volume: trade classification (quote rule on the option NBBO) or exchange open/close flags (OPRA) separate opening buys from closes.
- Strongest ahead of earnings and M&A; unusually-priced OTM activity in small names is the classic informed-flow footprint.
- Retail option flow (post-2020) is a distinct, largely uninformed-but-impactful component — separating retail from institutional flow sharpens the signal.

**Related.** [[Gamma Exposure and Dealer Hedging]], [[Implied Volatility Surface Dynamics]], [[Futures-ETF Lead-Lag]]

**Key references.** Johnson & So (2012), *The Option to Stock Volume Ratio and Future Returns*; Pan & Poteshman (2006), *The Information in Option Volume*.
