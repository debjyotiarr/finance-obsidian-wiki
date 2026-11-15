---
type: literature
status: inbox
title: "Automated Market Making and Decentralized Finance"
authors: ["Marcello Monga"]
year: 2024
venue: "arXiv 2407.16885"
url: http://arxiv.org/abs/2407.16885
pdf_url:
pdf: 00-Inbox/papers/Monga2024-Automated-Market-Making-and-Decentralized-Finance-f4d0ba.pdf
swept: 2026-11-12
origin: baobach/hft_papers catalogue
relevance: high
tags: [arxiv, market-making]
---

# Automated Market Making and Decentralized Finance

## Abstract (verbatim from arXiv)
Automated market makers (AMMs) are a new type of trading venues which are revolutionising the way market participants interact. At present, the majority of AMMs are constant function market makers (CFMMs) where a deterministic trading function determines how markets are cleared. Within CFMMs, we focus on constant product market makers (CPMMs) which implements the concentrated liquidity (CL) feature. In this thesis we formalise and study the trading mechanism of CPMMs with CL, and we develop liquidity provision and liquidity taking strategies. Our models are motivated and tested with market data. We derive optimal strategies for liquidity takers (LTs) who trade orders of large size and execute statistical arbitrages. First, we consider an LT who trades in a CPMM with CL and uses the dynamics of prices in competing venues as market signals. We use Uniswap v3 data to study price, liquidity, and trading cost dynamics, and to motivate the model. Next, we consider an LT who trades a basket of crypto-currencies whose constituents co-move. We use market data to study lead-lag effects, spillover effects, and causality between trading venues. We derive optimal strategies for strategic liquidity providers (LPs) who provide liquidity in CPMM with CL. First, we use stochastic control tools to derive a self-financing and closed-form optimal liquidity provision strategy where the width of the LP's liquidity range is determined by the profitability of the pool, the dynamics of the LP's position, and concentration risk. Next, we use a model-free approach to solve the problem of an LP who provides liquidity in multiple CPMMs with CL. We do not specify a model for the stochastic processes observed by LPs, and use a long short-term memory (LSTM) neural network to approximate the optimal liquidity provision strategy.

## Why staged
Auto-triaged by keyword from the baobach/hft_papers catalogue (unreviewed; quality unknown). Possible atoms: [[Market Maker Inventory Control]].
