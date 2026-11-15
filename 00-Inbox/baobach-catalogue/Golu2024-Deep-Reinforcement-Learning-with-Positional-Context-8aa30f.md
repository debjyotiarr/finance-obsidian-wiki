---
type: literature
status: inbox
title: "Deep Reinforcement Learning with Positional Context for Intraday Trading"
authors: ["Sven Goluža", "Tomislav Kovačević", "Tessa Bauman", "Zvonko Kostanjčar"]
year: 2024
venue: "arXiv 2406.08013"
url: http://arxiv.org/abs/2406.08013
pdf_url:
pdf: 00-Inbox/papers/Golu2024-Deep-Reinforcement-Learning-with-Positional-Context-8aa30f.pdf
swept: 2026-11-12
origin: baobach/hft_papers catalogue
relevance: medium
tags: [arxiv, intraday]
---

# Deep Reinforcement Learning with Positional Context for Intraday Trading

## Abstract (verbatim from arXiv)
Deep reinforcement learning (DRL) is a well-suited approach to financial decision-making, where an agent makes decisions based on its trading strategy developed from market observations. Existing DRL intraday trading strategies mainly use price-based features to construct the state space. They neglect the contextual information related to the position of the strategy, which is an important aspect given the sequential nature of intraday trading. In this study, we propose a novel DRL model for intraday trading that introduces positional features encapsulating the contextual information into its sparse state space. The model is evaluated over an extended period of almost a decade and across various assets including commodities and foreign exchange securities, taking transaction costs into account. The results show a notable performance in terms of profitability and risk-adjusted metrics. The feature importance results show that each feature incorporating contextual information contributes to the overall performance of the model. Additionally, through an exploration of the agent's intraday trading activity, we unveil patterns that substantiate the effectiveness of our proposed model.

## Why staged
Auto-triaged by keyword from the baobach/hft_papers catalogue (unreviewed; quality unknown). Possible atoms: [[Intraday Momentum]].
