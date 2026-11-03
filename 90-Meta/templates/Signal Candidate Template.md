---
type: signal
status: idea    # idea | researching | backtested | live | retired
horizon:        # e.g. seconds | minutes | intraday | 1-5 days
assets: []
atoms: []       # the atom notes this signal combines
tags: []
created: {{date}}
---

# {{title}}

## Hypothesis
What is predicted, over what horizon, and the mechanism (which atoms combine and why their combination is new).

## Construction
Inputs, transformation, normalization, sampling scheme (see [[Volume Clock]]).

## Economics
Expected IC/edge per trade, turnover, capacity sketch (via [[Square-Root Law of Market Impact]]), cost hurdle (via [[Implementation Shortfall]]).

## Validation plan
Labels ([[Triple Barrier Labeling]]), CV scheme, trials budget ([[Backtest Overfitting and Deflated Sharpe]]).

## Status log
- {{date}} — created.
