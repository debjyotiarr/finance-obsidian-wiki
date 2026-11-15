---
type: literature
status: inbox
title: "Maximizing Battery Storage Profits Via High-Frequency Intraday Trading"
authors: ["David Schaurecker", "David Wozabal", "Nils Löhndorf", "Thorsten Staake"]
year: 2025
venue: "arXiv 2504.06932"
url: http://arxiv.org/abs/2504.06932
pdf_url:
pdf: 00-Inbox/papers/Schaurecker2025-Maximizing-Battery-Storage-Profits-Via-High-e77a12.pdf
swept: 2026-11-12
origin: baobach/hft_papers catalogue
relevance: medium
tags: [arxiv, intraday]
---

# Maximizing Battery Storage Profits Via High-Frequency Intraday Trading

## Abstract (verbatim from arXiv)
Maximizing revenue for grid-scale battery energy storage systems in continuous intraday electricity markets requires strategies that are able to seize trading opportunities as soon as new information arrives. This paper introduces and evaluates a computationally efficient, high-frequency implementation of the rolling intrinsic trading strategy for battery energy storage systems on the intraday market for power. By combining the established rolling intrinsic logic with a full limit order book representation and a fast dynamic programming approximation, our method explicitly considers the continuously updated list of buy and sell offers, market rules, a linear approximation of degradation, and other technical parameters at a millisecond resolution. The standard rolling intrinsic strategy is adapted for continuous intraday electricity markets and solved using a dynamic programming approximation that is two to three orders of magnitude faster than an exact mixed-integer linear programming solution. A detailed backtest over a full year of German order book data demonstrates that the proposed dynamic programming formulation does not reduce trading profits and enables the policy to react to every relevant order book update, enabling realistic rapid backtesting. Our results show the significant revenue potential of high-frequency trading: our policy earns 58% more than when re-optimizing only once every hour and 14% more than when re-optimizing once per minute, highlighting that profits critically depend on trading speed. Furthermore, we leverage the speed of our algorithm to train a parametric extension of the rolling intrinsic, increasing yearly revenue by 8.4% out of sample.

## Why staged
Auto-triaged by keyword from the baobach/hft_papers catalogue (unreviewed; quality unknown). Possible atoms: [[Intraday Momentum]].
