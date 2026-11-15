---
type: literature
status: inbox
title: "Algorithmic and High-Frequency Trading Problems for Semi-Markov and Hawkes Jump-Diffusion Models"
authors: ["Luca Lalor", "Anatoliy Swishchuk"]
year: 2024
venue: "arXiv 2409.12776"
url: http://arxiv.org/abs/2409.12776
pdf_url:
pdf: 00-Inbox/papers/Lalor2024-Algorithmic-and-High-Frequency-Trading-Problems-63936c.pdf
swept: 2026-11-12
origin: baobach/hft_papers catalogue
relevance: high
tags: [arxiv, point-process]
---

# Algorithmic and High-Frequency Trading Problems for Semi-Markov and Hawkes Jump-Diffusion Models

## Abstract (verbatim from arXiv)
This paper introduces a jump-diffusion pricing model specifically designed for algorithmic trading and high-frequency trading (HFT). The model incorporates independent jump and diffusion processes, providing a more precise representation of the limit order book (LOB) dynamics within a scaling-limit framework. Given that algorithmic and HFT strategies now dominate major financial markets, accurately modeling LOB dynamics is crucial for developing effective trading algorithms. Recent research has shown that LOB data often exhibit non-Markovian properties, reinforcing the need for models that better capture its evolution. In this paper, we address acquisition and liquidation problems under more general compound semi-Markov and Hawkes jump-diffusion models. We first develop jump-diffusion frameworks to capture these dynamics and then apply diffusion approximations to the jump components so that robust solutions can be given. Optimal trading strategies are formulated using stochastic optimal control (SOC) and solved numerically. Finally, we present strategy simulations analyzing price paths, inventory evolution, trading speed, and average execution prices. This study provides insights into how these models can improve execution strategies under more general price dynamics.

## Why staged
Auto-triaged by keyword from the baobach/hft_papers catalogue (unreviewed; quality unknown). Possible atoms: [[Hawkes Processes for Order Flow]].
