---
type: meta
tags: [meta, ingestion, log]
created: 2026-11-12
---

# Sweep Log

The master list of papers and ideas: every paper any sweep or import has staged, one row each, newest last. Rows are added once a paper's abstract is available (298 catalogue stubs with no abstract are not listed yet). **Idea** is the paper's core claim in one line — what it would add to the vault — not the abstract. The full stub (abstract, links, relevance) is in `00-Inbox/` until reviewed.

## Papers

| Date | Paper | Idea |
|---|---|---|
| 2026-11-03 | Chávez Casillas & Gan — [Optimal Order Placement under a State-Dependent Hawkes LOB](https://arxiv.org/abs/2610.37324) | Market-making quotes when market-order arrivals follow a state-dependent Hawkes process instead of Poisson. |
| 2026-11-03 | Cheridito & Weiss — [Multi-Level Market Making with RL](https://arxiv.org/abs/2608.18195) | RL market maker quoting across several book levels, with queue position in the state. |
| 2026-11-03 | Moret & Lillo — [Robust Market Making under Regime-Switching Order Flow](https://arxiv.org/abs/2609.11614) | Classic MM rules lose money under directional flow regimes; change-point detection on flow bias restores PnL. |
| 2026-11-03 | Yang & Xu — [Adversarial RL MM with Hawkes Flow and Impact](https://arxiv.org/abs/2609.22785) | Adversarial training makes RL market makers robust to self-exciting flow and price impact. |
| 2026-11-03 | Wang et al. — [FlowLOB](https://arxiv.org/abs/2608.13096) | Flow-matching generator for realistic LOB paths that transfers to unseen instruments. |
| 2026-11-03 | Noble, Rosenbaum & Souilmi — [Bridging the Reality Gap in LOB Simulation](https://arxiv.org/abs/2603.24137) | Large-tick LOB simulator on spread + imbalance state that reproduces realistic execution costs and latency races. |
| 2026-11-03 | Prakash et al. — [FOMO: FLEX Options and Market Outcomes](https://arxiv.org/abs/2610.13044) | Customised FLEX option trades spill into listed-option open interest; unsigned gamma doesn't predict IV. |
| 2026-11-03 | Deng & Zhang — [Lead-Lag Clustering Comparison](https://arxiv.org/abs/2608.24703) | Benchmarks clustering methods for finding leader/lagger groups across a universe; KShape beats DTW. |
| 2026-11-03 | Barzykin, Boyce, Neuman & Tuschmann — [Optimal Execution with Passive Market Impact](https://arxiv.org/abs/2607.28323) | Executing with limit orders has its own impact; optimal passive schedule sits nearer TWAP under transient impact. |
| 2026-11-12 | Abbade & Costa — [Realistic Market Impact Modeling for RL Trading Environments](https://arxiv.org/abs/2603.29086) | RL trading environments with square-root and Almgren-Chriss impact built in, so agents stop learning strategies that only work at zero cost. |
| 2026-11-12 | Aldridge — [Evolution of Market Microstructure in the Age of AI](https://arxiv.org/abs/2609.33058) | Survey: each market-design shift (floor, LOB, HFT, batch auctions, AMMs, AI agents) moved the binding constraint on efficient allocation. |
| 2026-11-12 | Ananova et al. — [Model-free Analysis of Dynamic Trading Strategies](https://arxiv.org/abs/2011.02870) | Decompose any signal path into δ-excursions to get model-free risk and return of mean-reversion and pairs strategies. |
| 2026-11-12 | Bayraktar et al. — [Goal-based Portfolio Selection with Fixed Transaction Costs](https://arxiv.org/abs/2510.21650) | Fixed trading costs create complex no-trade regions in multi-goal investing. Peripheral to the vault. |
| 2026-11-12 | Bhatia — [High-Frequency Options Trading with Portfolio Optimization](https://arxiv.org/abs/2408.08866) | Five-minute SPY option strategies selected by IV and Greeks, then portfolio-optimised; one month of data only. |
| 2026-11-12 | Bilokon & Gunduz — [C++ Design Patterns for Low-latency Applications](https://arxiv.org/abs/2309.04259) | Benchmarked low-latency C++ patterns (incl. Disruptor) applied to a pairs-trading strategy; engineering, not alpha. |
| 2026-11-12 | Briola et al. — [Deep RL for Active High Frequency Trading](https://arxiv.org/abs/2101.07107) | PPO agent trading one unit of INTC from LOB data, trained only on samples with the largest price moves to raise signal-to-noise. |
| 2026-11-12 | Byrd et al. — [The Importance of Low Latency to Order Book Imbalance Trading Strategies](https://arxiv.org/abs/2006.08682) | Agent-based simulation quantifies how profit of an order-book-imbalance strategy decays as latency rises. |
| 2026-11-12 | Cartea et al. — [Decentralised Finance and Automated Market Making](https://arxiv.org/abs/2307.03499) | Execution cost in constant-product AMMs equals the convexity of the trading function; optimal execution and stat-arb follow from it. |
| 2026-11-12 | Chen et al. — [Learning About Latent Dynamic Trading Demand](https://arxiv.org/abs/2105.13401) | Equilibrium where traders filter child-order flow to infer the hidden parent order imbalance and its future price pressure. |
| 2026-11-12 | Chen et al. — [Probabilistic Intraday Electricity Price Forecasting](https://arxiv.org/abs/2506.00044) | Generative path forecasts for German intraday power prices used to time fixed-volume trades. Off-asset-class. |
| 2026-11-12 | Chomei — [LOB Modeling for Nikkei 225 Stocks with Cox-type Intensities](https://arxiv.org/abs/2302.01668) | Cox-type order-intensity models with added covariates predict trade sign across 222 Tokyo stocks. |
| 2026-11-12 | Chriss — [Position Building in Competition Is a Game with Incomplete Information](https://arxiv.org/abs/2501.01241) | Optimal position building when rivals' target sizes and impact models are unknown, solved as a Bayesian game. |
| 2026-11-12 | Cont et al. — [Fast and Slow Optimal Trading with Exogenous Information](https://arxiv.org/abs/2210.01901) | Stochastic game between a slow institution and an HFT sharing price impact; solves each side's optimal use of a common signal. |
| 2026-11-12 | Cucuringu et al. — [Forecasting Intraday Volume in Equity Markets with ML](https://arxiv.org/abs/2505.08180) | Intraday stock volume is highly predictable with ML and cross-stock commonality; better forecasts improve VWAP execution. |
| 2026-11-12 | Das et al. — [Optimal Round-Trip Pairs Trading Under Geometric Brownian Motions](https://arxiv.org/abs/2310.15803) | Optimal open/close thresholds for a pairs trade when both prices are GBMs, with no mean-reversion assumption. |
| 2026-11-12 | Fang & Feng — [Design of HFT Algorithm Based on Machine Learning](https://arxiv.org/abs/1912.10343) | Combines VPIN, GARCH and SVM on order-book data for a market-making return model. |
| 2026-11-12 | Fukasawa — [Loss-versus-rebalancing with External Transaction Costs](https://arxiv.org/abs/2610.21057) | AMM liquidity providers' loss versus rebalancing vanishes once the external market has a bid-ask spread. |
| 2026-11-12 | Goldblum et al. — [Adversarial Attacks on ML Systems for HFT](https://arxiv.org/abs/2002.09565) | Small, cheap order-book perturbations can fool deep price-prediction models; a robustness test for LOB models. |
| 2026-11-12 | Goluža et al. — [Deep RL with Positional Context for Intraday Trading](https://arxiv.org/abs/2406.08013) | Adding the strategy's own position state to an RL agent's features improves intraday trading. |
| 2026-11-12 | Guo et al. — [FutureQuant Transformer for Futures Markets](https://arxiv.org/abs/2505.05595) | Transformer on futures LOB data forecasts the price range and volatility, not a point price. |
| 2026-11-12 | Hanifan et al. — [Time Matters: Urgency and Reaction Speed in Automated Traders](https://arxiv.org/abs/2103.00600) | Simulated LOB market shows reaction speed and deadline urgency change which trading agent wins. |
| 2026-11-12 | Holý & Černý — [Bertram's Pairs Trading Strategy with Bounded Risk](https://arxiv.org/abs/2102.04160) | Optimal OU entry/exit thresholds that maximise profit per unit time under a cap on profit volatility. |
| 2026-11-12 | Hsieh — [Robustness of Double Linear Trading with Transaction Costs](https://arxiv.org/abs/2209.12383) | A 'robust positive expected gain' trading rule loses that property once transaction costs are included; gives the conditions that keep it. |
| 2026-11-12 | Ibikunle et al. — [Data-driven Measures of High-frequency Trading](https://arxiv.org/abs/2405.08101) | ML maps public intraday data to proprietary Nasdaq HFT labels, giving daily liquidity-supplying vs demanding HFT measures for all US stocks. |
| 2026-11-12 | Jafree et al. — [When AI Trading Agents Compete: Adverse Selection of Meta-Orders](https://arxiv.org/abs/2510.27334) | RL market maker in a Hawkes LOB learns to adversely select medium-frequency metaorders. |
| 2026-11-12 | Kang — [Optimal Signal Extraction from Order Flow: A Matched Filter Perspective](https://arxiv.org/abs/2512.18648) | Normalise order flow by the scale that matches who generates it: market cap for institutions, traded value for VWAP-style flow. |
| 2026-11-12 | Karpe — [Key Problems in Algorithmic Trading and Recent Progress](https://arxiv.org/abs/2006.05515) | Short survey of optimal execution, order placement and price impact, and ML approaches to each. |
| 2026-11-12 | Khapko & Zoican — [Do Speed Bumps Curb Low-latency Trading?](https://arxiv.org/abs/1910.03068) | Lab market: asymmetric speed bumps cut investment in speed by only about 20%; symmetric ones do nothing. |
| 2026-11-12 | Khubiev & Semenov — [Deep Learning Models Meet Financial Data Modalities](https://arxiv.org/abs/2504.13521) | How to feed candles, order statistics, LOB and news into deep models for trading signals. |
| 2026-11-12 | Krause & Calliess — [End-to-End Policy Learning of a Statistical Arbitrage Autoencoder](https://arxiv.org/abs/2402.08233) | Autoencoder replaces PCA for building the stat-arb residual and is trained end to end on the trading policy. |
| 2026-11-12 | Lalor & Swishchuk — [Algorithmic and HFT Problems for Semi-Markov and Hawkes Jump-Diffusion Models](https://arxiv.org/abs/2409.12776) | Optimal acquisition, liquidation and market making under non-Markovian (semi-Markov, Hawkes) jump-diffusion price models. |
| 2026-11-12 | Li & Tourin — [Optimal Pairs Trading with Time-Varying Volatility](https://arxiv.org/abs/2111.02834) | Pairs-trading weights by stochastic control when the spread has CEV-type volatility. |
| 2026-11-12 | Monga — [Automated Market Making and Decentralized Finance](https://arxiv.org/abs/2407.16885) | Thesis: liquidity-taking and liquidity-provision strategies for concentrated-liquidity AMMs. |
| 2026-11-12 | Naga et al. — [Decision Trees for Intuitive Intraday Trading Strategies](https://arxiv.org/abs/2405.13959) | Per-stock decision trees over technical indicators for NIFTY50 intraday rules. Low priority. |
| 2026-11-12 | Nagy et al. — [Asynchronous Deep Double Duelling Q-Learning for Signal Execution in LOB Markets](https://arxiv.org/abs/2301.08688) | RL agent in ABIDES turns a high-frequency alpha signal into individual limit-order placements, beating a naive execution. |
| 2026-11-12 | Neufeld et al. — [Robust Statistical Arbitrage with Deep Neural Networks](https://arxiv.org/abs/2203.03179) | Neural nets find stat-arb strategies that stay profitable under model ambiguity, without needing cointegrated pairs. |
| 2026-11-12 | Ning & Lee — [Advanced Statistical Arbitrage with Reinforcement Learning](https://arxiv.org/abs/2403.12180) | Build spreads by minimising an empirical mean-reversion time, then trade them with model-free RL. |
| 2026-11-12 | Ntakaris et al. — [Optimum Output LSTM Cell for HFT Forecasting](https://arxiv.org/abs/2304.09840) | LSTM variant that picks its best internal gate/state as output, tested on LOB mid-price forecasting. |
| 2026-11-12 | Rahman & Upadhye — [Hybrid VAR and Neural Network Model for OFI Prediction](https://arxiv.org/abs/2411.08382) | Forecast order flow imbalance itself: VAR for the linear part, a neural net on the residuals. |
| 2026-11-12 | Schaurecker et al. — [Maximizing Battery Storage Profits via High-Frequency Intraday Trading](https://arxiv.org/abs/2504.06932) | Rolling-intrinsic battery trading on the intraday power LOB. Off-asset-class. |
| 2026-11-12 | Spears et al. — [Investment Sizing with Deep Learning Prediction Uncertainties (Eurodollar Futures)](https://arxiv.org/abs/2007.15982) | Size each trade by the model's own prediction uncertainty; improves Sharpe in high-frequency Eurodollar futures. |
| 2026-11-12 | Suchato et al. — [An Application of the OU Process to Pairs Trading](https://arxiv.org/abs/2412.12458) | OU-based pairs signals underperform a naive rolling z-score on risk-adjusted terms, likely from non-stationary pairs. |
| 2026-11-12 | Wang et al. — [Intraday Trading Strategy for the Chinese Stock Market](https://arxiv.org/abs/2103.13507) | Markowitz weights plus MLP price prediction under China's T+1 rule. Low priority. |
| 2026-11-12 | Xing — [Singular Stochastic Control for Optimal Pairs Trading with Proportional Costs](https://arxiv.org/abs/1911.10450) | Jointly optimal trade times and sizes for a cointegrated pair under proportional transaction costs. |
| 2026-11-12 | Xu & Cheng — [Are Large Traders Harmed by Front-running HFTs?](https://arxiv.org/abs/2211.06046) | An HFT that predicts a large trader's flow always front-runs, yet the large trader gains when noise trading is high or the prediction is vague. |
| 2026-11-12 | Yagi et al. — [Trading Strategies of a Leveraged ETF in a Continuous Double Auction Market](https://arxiv.org/abs/2010.13036) | Agent-based test of how a leveraged ETF should execute its rebalancing to add the least volatility to the underlying. |
| 2026-11-12 | Yang & Malik — [Reinforcement Learning Pair Trading: A Dynamic Scaling Approach](https://arxiv.org/abs/2407.16103) | RL sizes pair-trade positions dynamically; tested on crypto. |
| 2026-11-12 | Zhang — [Pairs Trading with Nonlinear and Non-Gaussian State Space Models](https://arxiv.org/abs/2005.09794) | Treat the spread as a latent state with nonlinear mean reversion and heteroskedastic shocks; trade on the filtered spread. |
| 2026-11-12 | Zhang et al. — [ClusterLOB: Clustering Orders in Limit Order Books](https://arxiv.org/abs/2504.20349) | Cluster market-by-order events into directional, opportunistic and market-making flow; per-cluster OFI gives better signals. |
| 2026-11-12 | Zhao et al. — [Label Unbalance in High-frequency Trading](https://arxiv.org/abs/2503.09988) | After costs, profitable HFT labels are rare; imbalance-aware training improves deep return prediction. |
| 2026-11-12 | Zhou et al. — [High-Frequency Trading on Decentralized On-Chain Exchanges](https://arxiv.org/abs/2009.14021) | Formalises and measures sandwich attacks (front- plus back-running) on AMM exchanges. Crypto-only. |
| 2026-11-12 | Zhou — [Application of Black-Litterman Bayesian in Statistical Arbitrage](https://arxiv.org/abs/2406.06706) | Feed pairs-trading signals in as Black-Litterman views to get a portfolio that holds up in stressed markets. |
| 2026-11-12 | Zhuang et al. — [Quantum Quantitative Trading: High-Frequency Statistical Arbitrage](https://arxiv.org/abs/2104.14214) | Quantum algorithm for stat-arb cointegration tests with claimed speed-up. Not actionable. |
| 2026-11-15 | Bayraktar et al. — [Price-impact Martingale optimal transport](https://arxiv.org/abs/2611.17247) | — |
| 2026-11-15 | Hirsch et al. — [Improving Algorithmic Trading for BESS on Intraday Electricity Markets through Distributional Price Forecasts](https://arxiv.org/abs/2611.17170) | — |
| 2026-11-15 | Gamrani & Pham — [Media Trading with Censored Auction Prices: A Stochastic Control and Reinforcement Learning Approach](https://arxiv.org/abs/2611.16992) | — |
| 2026-11-15 | Fabi & Leloup — [Verifiable Settlement and Pricing for Local Energy Markets: Architecture and Deployment on Hyperledger Besu](https://arxiv.org/abs/2611.16495) | — |
| 2026-11-15 | Mensah et al. — [Dynamic Scenario-Based Portfolio Optimization for Multi-Asset ETFs](https://arxiv.org/abs/2611.16540) | — |
| 2026-11-15 | Huang — [TAPES: Terminal Adjoint-Propagated Error Scheduling for Financial Diffusion Samplers](https://arxiv.org/abs/2611.16484) | — |
| 2026-11-15 | Choulli & Elazkany — [Novel Esscher concepts for informational risks and valuation in market models under random horizon](https://arxiv.org/abs/2611.16129) | — |
| 2026-11-16 | Bayer et al. — [Local Stochastic Volatility Iterations](https://arxiv.org/abs/2611.18214) | — |
| 2026-11-16 | Yang et al. — [Who Should Be on the Panel? Task-Conditioned Persona Selection for LLM Trading Agents](https://arxiv.org/abs/2611.18150) | — |
| 2026-11-16 | Prado et al. — [DECODE: Decomposable Environments for COntrolled Sequential-Decision Evaluation](https://arxiv.org/abs/2611.18367) | — |
| 2026-11-16 | Chassagneux et al. — [Well-Posedness of Semimartingale Optimal Transport with Partial Marginal Constraints for Model Calibration](https://arxiv.org/abs/2611.17902) | — |
| 2026-11-17 | Caglar et al. — [Stochastic Modelling of High-frequency (HF) Crypto Limit Order Book (LOB) with General Compound Marked Hawkes Process](https://arxiv.org/abs/2611.20839) | — |
| 2026-11-17 | Supriadi — [Dynamic Spatio-Temporal Graph Attention Networks with Nested Clustered Optimization for Multi-Asset Portfolios](https://arxiv.org/abs/2611.19903) | — |
| 2026-11-17 | Borrageiro — [Markets for Compute and Inference: Structure, Financing, and Risk Transfer](https://arxiv.org/abs/2611.20242) | — |
| 2026-11-17 | Wang et al. — [AllocFlow: End-to-End Portfolio Trading Action Generation from Raw Market Data](https://arxiv.org/abs/2611.19937) | — |
| 2026-11-17 | Adachi & Hara — [Toward an Admissibility Theory of Aharonov--Bohm Arbitrage](https://arxiv.org/abs/2611.19870) | — |
| 2026-11-17 | Bansal et al. — [PIRanNN: Random-Feature Pricing and Calibration under Jump-Diffusion and Stochastic-Volatility Models](https://arxiv.org/abs/2611.19792) | — |
| 2026-11-17 | Kaissi — [Strategic Repayment and Latent Fragility in Financial Networks: Why Banks Withhold Payable Liquidity](https://arxiv.org/abs/2611.21262) | — |
| 2026-11-17 | Dominguez — [A Second Order Transport Scheme for Dynamic Portfolio Subspaces under a Varying Risk Metric](https://arxiv.org/abs/2611.20911) | — |
| 2026-11-17 | Hu et al. — [Beyond Marginal Risk: ESG and Multidimensional Fragility in Equity Markets](https://arxiv.org/abs/2611.20589) | — |
| 2026-11-17 | Zhang — [Mollification Regularization and Asymptotic Correction for Analytical Expansion of BSDEs with Non-Smooth Terminal Conditions. I. Theory](https://arxiv.org/abs/2611.20550) | — |
| 2026-11-17 | Kim & Zhou — [EWMA Principal Eigenportfolios of Equity Returns: Market Representation and Beta-Hedging Performance](https://arxiv.org/abs/2611.20363) | — |
| 2026-11-18 | Afroz et al. — [Revisiting Equity-Bond Diversification under Tail Risk and Structural Market Change: Evidence from Global ETFs and Model-Implied Option Prices](https://arxiv.org/abs/2611.21897) | — |
| 2026-11-18 | Chalvatzis — [Which Past Matters? Training History and Multi-Forecast Horizon in Equity Transformers](https://arxiv.org/abs/2611.23126) | — |
| 2026-11-18 | Chen et al. — [Beyond Strike Remapping: Conditional-Gamma Pricing of Leveraged ETF Options under Local Volatility](https://arxiv.org/abs/2611.22604) | — |
| 2026-11-19 | Ramachandran — [Algorithmic Market Making Can Lead to Rough Volatility Through the Order Book](https://arxiv.org/abs/2611.24028) | — |
| 2026-11-19 | Itkin & Muravey — [Spectral Pricing of Corridor Products under Layered Local Volatility](https://arxiv.org/abs/2611.23587) | — |
| 2026-11-19 | Glasserman et al. — [Total Positivity Properties of American Options](https://arxiv.org/abs/2611.23495) | — |
| 2026-11-19 | Larsen — [Stock bubbles in limited participation models with power utilities](https://arxiv.org/abs/2611.24912) | — |
| 2026-11-19 | Wu et al. — [Vibe-Trading: Towards Agent-Native Trading](https://arxiv.org/abs/2611.24845) | — |
| 2026-11-19 | Kozlova & Yeomans — [Sensitivity analysis in real options studies: systematic review and recommendations](https://arxiv.org/abs/2611.24266) | — |
| 2026-11-19 | Chen et al. — [When Price Charts Rhyme: Historical Visual Retrieval for Stock Return Prediction](https://arxiv.org/abs/2611.23723) | — |
| 2026-11-20 | Qureshi — [Trading Before a Committed Rebalance](https://arxiv.org/abs/2611.25762) | — |
| 2026-11-20 | Grasselli et al. — [A joint framework for SPX, VIX and VXX](https://arxiv.org/abs/2611.25047) | — |
| 2026-11-20 | Kozhevnikov — [Optimal Control in Pairs Trading with Negative-Power Utility](https://arxiv.org/abs/2611.26568) | — |
| 2026-11-20 | Schlegel & Mamageishvili — [Path-Independent Deleveraging Rules](https://arxiv.org/abs/2611.26623) | — |
| 2026-11-20 | Qadi et al. — [A Three-Factor Hull-White Scenario Generator for Macro-Financial Stress Forecasting](https://arxiv.org/abs/2611.26200) | — |
| 2026-11-20 | Daya et al. — [Feasible sub-replicating portfolios for basket options via the block rearrangement algorithm](https://arxiv.org/abs/2611.26119) | — |
| 2026-11-20 | Laloux & Srinivasan — [Neckpinches in a Positively Curved Market: Ricci Flow with Surgery on the Nikkei-225](https://arxiv.org/abs/2611.25860) | — |
| 2026-11-20 | Cai et al. — [Auto-Alpha: A Framework for Autonomous Factor Research](https://arxiv.org/abs/2611.25732) | — |
| 2026-11-20 | Hoshisashi — [Quantum Calibration of Local-Volatility Surfaces from Sparse Option Quotes](https://arxiv.org/abs/2611.25344) | — |
| 2026-11-23 | Ranco — [Do Econophysics-Inspired Inputs Improve Neural Covariance Forecasting? A Leakage-Free Walk-Forward Study of Intraday DJIA Data](https://arxiv.org/abs/2611.27616) | — |
| 2026-11-23 | Kratsios et al. — [Reconstructing risk preferences from data](https://arxiv.org/abs/2611.27692) | — |
| 2026-11-23 | Miao et al. — [Risk sharing for background risk models with infinite mean](https://arxiv.org/abs/2611.27485) | — |
| 2026-11-23 | Ruelloux et al. — [Nonlinear Shrinkage for Higher Moments Estimation in Large Portfolios](https://arxiv.org/abs/2611.27274) | — |

## Runs

| Date | Lookback | Staged | Sites (direct / search fallback / unreachable) | Notes |
|---|---|---|---|---|
| 2026-11-03 | ~2026-08-05 → 2026-11-03 | 9 | arXiv: search fallback | Manual dry run, strict filter. arxiv.org blocked by network policy; no PDFs. 5 borderline papers skipped. |
| 2026-11-12 | n/a (catalogue import) | 352 (h/m/l: 58/261/33) | baobach/hft_papers CSV, 2,302 rows | Keyword-triaged, not read; stubs in `00-Inbox/baobach-catalogue/`. Per-paper rows omitted from the Papers table (no ideas available without abstracts). See [[baobach HFT Papers Catalogue]]. |
| 2026-11-15 | 2026-11-12 → 2026-11-15 | 7 (h/m/l: 0/4/3) | arXiv: direct (API) | Script sweep, 300 listed. Ideas not yet written. |
| 2026-11-15 | 2026-11-12 → 2026-11-15 | 0 (h/m/l: 0/0/0) | arXiv: direct (API) | Script sweep, 300 listed. Ideas not yet written. |
| 2026-11-16 | 2026-11-13 → 2026-11-16 | 4 (h/m/l: 0/2/2) | arXiv: direct (API) | Script sweep, 300 listed. Ideas not yet written. |
| 2026-11-17 | 2026-11-14 → 2026-11-17 | 11 (h/m/l: 1/1/9) | arXiv: direct (API) | Script sweep, 300 listed. Ideas not yet written. |
| 2026-11-18 | 2026-11-15 → 2026-11-18 | 3 (h/m/l: 0/3/0) | arXiv: direct (API) | Script sweep, 300 listed. Ideas not yet written. |
| 2026-11-19 | 2026-11-16 → 2026-11-19 | 7 (h/m/l: 1/0/6) | arXiv: direct (API) | Script sweep, 300 listed. Ideas not yet written. |
| 2026-11-20 | 2026-11-17 → 2026-11-20 | 9 (h/m/l: 1/2/6) | arXiv: direct (API) | Script sweep, 300 listed. Ideas not yet written. |
| 2026-11-21 | 2026-11-18 → 2026-11-21 | 0 (h/m/l: 0/0/0) | arXiv: direct (API) | Script sweep, 300 listed. Ideas not yet written. |
| 2026-11-22 | 2026-11-19 → 2026-11-22 | 0 (h/m/l: 0/0/0) | arXiv: direct (API) | Script sweep, 300 listed. Ideas not yet written. |
| 2026-11-23 | 2026-11-20 → 2026-11-23 | 4 (h/m/l: 0/1/3) | arXiv: direct (API) | Script sweep, 300 listed. Ideas not yet written. |
