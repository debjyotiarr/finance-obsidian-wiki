---
type: literature
status: inbox
title: "Vibe-Trading: Towards Agent-Native Trading"
authors: ["Haozhe Wu", "Zhonghang Li", "Chao Huang"]
year: 2026
venue: "arXiv cs.AI (2611.24845)"
url: https://arxiv.org/abs/2611.24845
pdf_url: https://arxiv.org/pdf/2611.24845
pdf: 00-Inbox/papers/Wu2026-Vibe-Trading-Towards-Agent-Native-Trading-261124845.pdf
swept: 2026-11-19
posted: 2026-11-18
origin: daily sweep script
relevance: low
tags: [execution]
---

# Vibe-Trading: Towards Agent-Native Trading

## Abstract (verbatim from arXiv)
Existing AI agents can retrieve information, call tools, run experiments, and produce multi-step outputs. Yet most are built around relatively static workflows and struggle to preserve reliable state as the environment changes. Financial trading makes this limitation especially consequential: prices, news, market conditions, portfolio positions, and available capital evolve continuously. A result is useful only when it remains tied to the correct time, data snapshot, and execution context. We present Vibe-Trading, a comprehensive agent-native trading framework and all-in-one workspace for building, evaluating, and evolving agents for financial trading. It unifies market research, financial data, strategy generation, backtesting, portfolio analysis, paper trading, multi-agent collaboration, and optional broker execution. Its central contribution is an architecture that keeps results, evidence, research history, and trading authority connected throughout the research-to-action process. Each result retains its source, temporal scope, configuration, and producing run. Shared evidence grounding enables verification, versioned research records support reproducible continuation, and an explicit authority gate separates strategy research from live execution. Together, these designs provide a practical foundation for trading agents whose results can be traced, reproduced, and acted on only under explicit authority.

## Why staged
Auto-staged by the daily sweep (keyword filter, unreviewed). Possible related notes: [[Optimal Execution (Almgren-Chriss)]].
