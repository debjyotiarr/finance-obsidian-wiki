---
type: literature
status: inbox
title: "Who Should Be on the Panel? Task-Conditioned Persona Selection for LLM Trading Agents"
authors: ["Boming Yang", "Yuquan Wang", "Jiaxian Guo", "Yusuke Iwasawa", "Yutaka Matsuo"]
year: 2026
venue: "arXiv q-fin.TR (2611.18150)"
url: https://arxiv.org/abs/2611.18150
pdf_url: https://arxiv.org/pdf/2611.18150
pdf: 00-Inbox/papers/Yang2026-Who-Should-Be-on-the-Panel-261118150.pdf
swept: 2026-11-16
posted: 2026-11-13
origin: daily sweep script
relevance: medium
tags: []
---

# Who Should Be on the Panel? Task-Conditioned Persona Selection for LLM Trading Agents

## Abstract (verbatim from arXiv)
Multi-agent LLM systems are built by fixing a cast of roles and then designing how the cast coordinates. Which agents should make up the group for a given task is left to the designer, and the same cast is reused for every task. Financial trading makes the cost of that choice visible: stocks trade differently, and the trading styles suited to one need not suit another. We study task-conditioned persona selection, composing the group from the characteristics of the task it will face, and instantiate it with FinPanel, an LLM multi-agent trading system in which a recruiter selects a panel of named trader personas for each stock from a direction-blind statistical sketch of how the stock trades, each persona gives an independent daily call in its own style, and a manager commits the trade after reading the panel's arguments and their desk-kept, hierarchical track records. Because nothing is returned to the traders, the panel stays the panel that was selected, and it can trade a new stock from an empty record. On eight US stocks over the out-of-knowledge year 2025, against three prior LLM trading agents re-implemented in the same framework and against rule-based, predictive and reinforcement-learning baselines, the selected panel is ahead of a fixed panel of the same size and of the prior agents run as their papers prescribe, with a shallower drawdown than buy-and-hold on every stock; it keeps its performance with no warm-up and with no record at all, whereas the memory-augmented agents' returns swing with their warm-up; and neither more seats nor the manager's reading of the arguments substitutes for selecting the right ones. Who is in the group is a design decision to be made per task, before how the group coordinates.

## Why staged
Auto-staged by the daily sweep (keyword filter, unreviewed). Possible related notes: no obvious match.
