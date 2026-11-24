---
type: literature
status: inbox
title: "Know When to Abstain: Conformal Confidence Estimation for Text-to-SQL"
authors: ["Avinash Kumar Singh", "Bhaskarjit Sarmah", "Stefano Pasquali"]
year: 2026
venue: "arXiv cs.AI (2611.31190)"
url: https://arxiv.org/abs/2611.31190
pdf_url: https://arxiv.org/pdf/2611.31190
pdf: 00-Inbox/papers/Singh2026-Know-When-to-Abstain-Conformal-Confidence-261131190.pdf
swept: 2026-11-24
posted: 2026-11-23
origin: daily sweep script
relevance: low
tags: [execution]
---

# Know When to Abstain: Conformal Confidence Estimation for Text-to-SQL

## Abstract (verbatim from arXiv)
Text-to-SQL systems often return queries that execute successfully but answer the wrong question. Detecting these errors at deployment is hard because execution correctness is defined against a gold query, which exists only in labeled data. We formulate confidence estimation for Text-to-SQL as probabilistic query validation under a latent correctness variable that is observable at calibration time through gold-SQL execution and latent at deployment. Our estimator separates generation from validation. A generator LLM writes and executes the query, and a different critic LLM judges the query and its execution result. The critic's validation and execution-grounded alignment scores are fused with the generator's verbalized confidence, token-level uncertainty, and SQL-structural features in a Random Forest, using two sequential LLM calls. Two calibration steps give finite-sample guarantees. A Learn-then-Test threshold ensures, with probability $1-δ$, that the error rate among accepted queries stays below a user-chosen budget. A conformal p-value bounds the false abstention rate. On Spider we use GPT-OSS-120B as generator and Gemma-4-31B as critic. The estimator obtains an AUARC of 0.899. Without abstention, 22.6% of queries are wrong. With a 15% risk budget ($δ=0.1$), a threshold is certified on all 10 resampled splits, and the system accepts 52.4% of queries on average with 9.1% observed error. Five different critic models give similar results. In a controlled comparison on Spider with Olmo-3-32B as generator, the estimator obtains an AUARC of 89.5, compared with 81.2 for the strongest logit-based baseline. Applied to BIRD without retraining, the confidence scores remain informative (AUROC 0.72, against 0.79 on Spider), but the risk guarantee does not transfer, as expected without exchangeability.

## Why staged
Auto-staged by the daily sweep (keyword filter, unreviewed). Possible related notes: [[Optimal Execution (Almgren-Chriss)]].
