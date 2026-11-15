---
type: literature
status: inbox
title: "Robust Market Making with Hawkes Order Flow and Price Impact via Adversarial Reinforcement Learning"
authors: [Yang, Hao, Xu, Zhenguo]
year: 2026
venue: arXiv cs.LG (2609.22785)
url: https://arxiv.org/abs/2609.22785
pdf_url: https://arxiv.org/pdf/2609.22785
pdf: 00-Inbox/papers/Yang-Xu2026-Adversarial-RL-Hawkes-MM.pdf
swept: 2026-11-03
tags: [market-making, machine-learning, point-process, robustness]
---

# Robust Market Making with Hawkes Order Flow and Price Impact via Adversarial RL

## Abstract (verbatim from arXiv)
Market-making strategies in real limit order book markets face substantial model uncertainty and regime-shift risk. Existing adversarial reinforcement learning approaches improve robustness by formulating the Avellaneda--Stoikov market-making problem as a zero-sum game between a market maker and an environmental adversary. However, these approaches typically rely on Poisson order arrivals and neglect trade-induced price impact, limiting their ability to capture important high-frequency market microstructure effects such as clustered order flow, self-excitation, and post-trade price feedback. We extend adversarial reinforcement learning for market making to a more complex environment with Hawkes self-exciting order arrivals and trade-induced price impact. To mitigate the increased non-stationarity introduced by the expanded regime space, we incorporate an LSTM module that explicitly models the temporal structure of recent observations. We further characterize the equilibrium properties of the proposed framework through both game-theoretic analysis and numerical experiments, and introduce a robustness evaluation protocol focused on improvements in the left tail of the return distribution. Experimental results across a range of market regimes show that the proposed method achieves improved left-tail performance in most complex microstructure environments. In particular, the gains are pronounced in regimes with strong Hawkes excitation and low-to-moderate price impact. Bootstrap tests provide no evidence that these improvements are obtained through a stronger terminal directional inventory bias. These results suggest that combining adversarial training with temporal state representation can improve the robustness of reinforcement-learning-based market-making strategies under order-flow self-excitation, price impact, and regime uncertainty.

## Why staged
Same cluster as Moret-Lillo and Chávez Casillas-Gan — robustness of [[Market Maker Inventory Control]] under [[Hawkes Processes for Order Flow]] and [[Price Impact and Kyle's Lambda]]. Quality uncertain (cs.LG venue, unfamiliar authors) — review before extraction; three papers on one theme may merit a single combined atom update.
