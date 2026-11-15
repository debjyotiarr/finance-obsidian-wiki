---
type: literature
status: inbox
title: "Optimum Output Long Short-Term Memory Cell for High-Frequency Trading Forecasting"
authors: ["Adamantios Ntakaris", "Moncef Gabbouj", "Juho Kanniainen"]
year: 2023
venue: "arXiv 2304.09840"
url: http://arxiv.org/abs/2304.09840
pdf_url:
pdf: 00-Inbox/papers/Ntakaris2023-Optimum-Output-Long-Short-Term-Memory-2b08b4.pdf
swept: 2026-11-12
origin: baobach/hft_papers catalogue
relevance: medium
tags: [arxiv]
---

# Optimum Output Long Short-Term Memory Cell for High-Frequency Trading Forecasting

## Abstract (verbatim from arXiv)
High-frequency trading requires fast data processing without information lags for precise stock price forecasting. This high-paced stock price forecasting is usually based on vectors that need to be treated as sequential and time-independent signals due to the time irregularities that are inherent in high-frequency trading. A well-documented and tested method that considers these time-irregularities is a type of recurrent neural network, named long short-term memory neural network. This type of neural network is formed based on cells that perform sequential and stale calculations via gates and states without knowing whether their order, within the cell, is optimal. In this paper, we propose a revised and real-time adjusted long short-term memory cell that selects the best gate or state as its final output. Our cell is running under a shallow topology, has a minimal look-back period, and is trained online. This revised cell achieves lower forecasting error compared to other recurrent neural networks for online high-frequency trading forecasting tasks such as the limit order book mid-price prediction as it has been tested on two high-liquid US and two less-liquid Nordic stocks.

## Why staged
Auto-triaged by keyword from the baobach/hft_papers catalogue (unreviewed; quality unknown). Possible atoms: no obvious atom match.
