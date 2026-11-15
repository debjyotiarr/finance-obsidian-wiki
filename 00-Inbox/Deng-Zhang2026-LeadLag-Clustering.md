---
type: literature
status: inbox
title: "Lead-Lag Relationships in Financial Markets: A Comparison of Multiple Clustering Algorithms"
authors: [Deng, Ruichen, Zhang, Yichi]
year: 2026
venue: arXiv q-fin.ST (2608.24703)
url: https://arxiv.org/abs/2608.24703
pdf_url: https://arxiv.org/pdf/2608.24703
pdf: 00-Inbox/papers/Deng-Zhang2026-LeadLag-Clustering.pdf
swept: 2026-11-03
tags: [lead-lag, methodology, machine-learning]
---

# Lead-Lag Relationships in Financial Markets: A Comparison of Multiple Clustering Algorithms

## Abstract (verbatim from arXiv)
Lead-lag relationships are widely used in financial time series, and many clustering algorithms based on them have been developed. The traditional DTW-KMedoids algorithm performs well both on the synthetic dataset and the real financial dataset. However, there are still several limitations to these algorithms: low efficiency caused by high time complexity, poor mathematical properties from DTW distance, the clustering effect is sensitive to the number of clusters. To solve the problems above and improve the performance, this paper introduces three clustering algorithms: MiniRocket-KMeans, KShape, Ensemble algorithm (a combination of KShape and DTW-KMedoids) and compares their performance on synthetic and real stock datasets with DTW-KMedoids algorithm under the same trade strategy. In addition, this paper also finds the best number of clusters by maximizing the silhouette coefficient in each clustering algorithm to improve the stability of the experiment results. Our main conclusions are as follows: MiniRocket-KMeans performs best under the lead strategy, achieving a Sharpe ratio of 0.866 with a maximum drawdown controlled at -63.9\%; the ensemble algorithm exhibits excellent stability; the robustness is significantly improved after finding the best number of clusters; the p-values of the hypothesis test on the Sharpe ratio of all strategies are 0.0, verifying the statistical validity of the lead-lag trading strategy. Finally, future improvement directions such as customized lead-lag matrices and optimized ensemble voting mechanisms are proposed.

## Why staged
Methods paper for systematizing [[Futures-ETF Lead-Lag]]-style discovery across the whole universe rather than known pairs — feeds [[Pairs Trading and Statistical Arbitrage]] universe construction. Quality uncertain (unfamiliar authors, q-fin.ST): skim before extracting.
