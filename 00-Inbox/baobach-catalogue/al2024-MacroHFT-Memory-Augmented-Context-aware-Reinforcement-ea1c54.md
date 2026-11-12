---
type: literature
status: inbox
title: "MacroHFT: Memory Augmented Context-aware Reinforcement Learning On High Frequency Trading"
authors: ["CHUQIAO ZONG et. al."]
year: 2024
venue: "KDD (conference)"
url: https://doi.org/10.1145/3637528.3672064
pdf_url:
pdf:
swept: 2026-11-12
origin: baobach/hft_papers catalogue
relevance: medium
tags: []
---

# MacroHFT: Memory Augmented Context-aware Reinforcement Learning On High Frequency Trading

## Abstract
*Not available — the source catalogue has no abstracts. Fetch from the URL above before extracting.*
Catalogue description: However, existing RL methods for HFT still have some defects: 1) standard RL-based trading agents suffer from the overfitting issue, preventing them from making effective policy adjustments based on financial context; 2) due to the rapid changes in market conditions, investment decisions made by an individual agent are usually one-sided and highly biased, which might lead to significant loss in extreme markets. To tackle these problems, we propose a novel Memory Augmented Context-aware Reinforcement learning method On HFT, a.k.a. MacroHFT, which consists of two training phases: 1) we first train multiple types of sub-agents with the market data decomposed according to various financial indicators, specifically market trend and volatility, where each agent owns a conditional adapter to adjust its trading policy according to market conditions; 2) then we train a hyper-agent to mix the decisions from these sub-agents and output a consistently profitable meta-policy to handle rapid market fluctuations, equipped with a memory mechanism to enhance the capability of decision-making

## Why staged
Auto-triaged by keyword from the baobach/hft_papers catalogue (unreviewed; quality unknown). Possible atoms: no obvious atom match.
