---
type: literature
status: inbox
title: "Asynchronous Deep Double Duelling Q-Learning for Trading-Signal Execution in Limit Order Book Markets"
authors: ["Peer Nagy", "Jan-Peter Calliess", "Stefan Zohren"]
year: 2023
venue: "arXiv 2301.08688"
url: http://arxiv.org/abs/2301.08688
pdf_url:
pdf: 00-Inbox/papers/Nagy2023-Asynchronous-Deep-Double-Duelling-Q-Learning-ecef26.pdf
swept: 2026-11-12
origin: baobach/hft_papers catalogue
relevance: high
tags: [arxiv, execution, orderbook]
---

# Asynchronous Deep Double Duelling Q-Learning for Trading-Signal Execution in Limit Order Book Markets

## Abstract (verbatim from arXiv)
We employ deep reinforcement learning (RL) to train an agent to successfully translate a high-frequency trading signal into a trading strategy that places individual limit orders. Based on the ABIDES limit order book simulator, we build a reinforcement learning OpenAI gym environment and utilise it to simulate a realistic trading environment for NASDAQ equities based on historic order book messages. To train a trading agent that learns to maximise its trading return in this environment, we use Deep Duelling Double Q-learning with the APEX (asynchronous prioritised experience replay) architecture. The agent observes the current limit order book state, its recent history, and a short-term directional forecast. To investigate the performance of RL for adaptive trading independently from a concrete forecasting algorithm, we study the performance of our approach utilising synthetic alpha signals obtained by perturbing forward-looking returns with varying levels of noise. Here, we find that the RL agent learns an effective trading strategy for inventory management and order placing that outperforms a heuristic benchmark trading strategy having access to the same signal.

## Why staged
Auto-triaged by keyword from the baobach/hft_papers catalogue (unreviewed; quality unknown). Possible atoms: [[Limit Order Book Shape as Signal]], [[Optimal Execution (Almgren-Chriss)]].
