---
type: moc
tags: [moc, cheat-sheet]
created: 2026-11-12
---

# Ideas Cheat Sheet

Every idea in the vault: name, core maths, one-line summary. 38 atoms + 4 signal candidates. Click a name to open the full note.

## Market Microstructure — order book and flow

**[[Order Flow Imbalance]]**
$e_n = \mathbb{1}_{P^b_n \ge P^b_{n-1}} q^b_n - \mathbb{1}_{P^b_n \le P^b_{n-1}} q^b_{n-1} - \mathbb{1}_{P^a_n \le P^a_{n-1}} q^a_n + \mathbb{1}_{P^a_n \ge P^a_{n-1}} q^a_{n-1}$, $\;\mathrm{OFI}_k=\sum_{n\in k} e_n$, $\;\Delta P_k \approx \beta\,\mathrm{OFI}_k$, $\beta \propto 1/\text{depth}$
Net signed best-level book events predict short-horizon price moves almost linearly.

**[[Microprice]]**
$P_{\text{micro}} = \dfrac{P^a Q^b + P^b Q^a}{Q^a+Q^b} = P^b + I\cdot s,\quad I=\dfrac{Q^b}{Q^a+Q^b}$; Stoikov: $P_{\text{micro}} = \lim_{t\to\infty}\mathbb{E}[M_t \mid I, s]$
Fair value is pulled toward the side with the *thinner* queue; better than mid for quoting and signals.

**[[Limit Order Book Shape as Signal]]**
$\hat r_{t+h} = f\big(\{Q^b_{\ell}, Q^a_{\ell}, \Delta Q_\ell\}_{\ell=1}^{L}\big)$, features normalised by tick and mean depth
Deeper book levels and their changes add (small) predictive power beyond top-of-book; ML on snapshots overfits easily.

**[[Trade Sign Autocorrelation]]**
$C(\tau)=\mathbb{E}[\epsilon_t\epsilon_{t+\tau}] \sim \tau^{-\gamma},\ 0<\gamma<1$; propagator $p_t = \sum_{s<t} G(t-s)\,\epsilon_s + \text{noise}$
Market-order signs have long memory (order splitting), yet prices stay near-martingale; alpha is in flow *surprises*.

**[[Hawkes Processes for Order Flow]]**
$\lambda_i(t)=\mu_i+\sum_j\sum_{t^j_k<t}\alpha_{ij}e^{-\beta_{ij}(t-t^j_k)}$; branching ratio $n=\alpha/\beta$
Order events self- and cross-excite; $n\to 1$ signals an endogenous, fragile market.

**[[Hidden Liquidity and Iceberg Orders]]**
Detect: $V^{\text{exec}}_\ell > Q^{\text{displayed}}_\ell$ or instant refill at same price; $\;\hat Q^{\text{true}} = Q^{\text{disp}} + \mathbb{E}[\text{reserve}\mid \text{refills}]$
Much liquidity is undisplayed; detected icebergs reveal patient large traders and bias displayed imbalance.

## Market Microstructure — market making

**[[Adverse Selection]]**
Markout $m(\tau) = \mathrm{side}\cdot(M_{t+\tau}-P_{\text{fill}})$; $\;\text{realised spread} = \text{quoted spread} - \text{adverse selection}$
Passive fills come disproportionately just before the price moves against you; markouts measure the cost.

**[[Bid-Ask Spread Decomposition]]**
$s = \underbrace{c_{\text{order}}}_{\text{processing}} + \underbrace{c_{\text{inv}}}_{\text{inventory}} + \underbrace{c_{\text{AS}}}_{\text{adverse sel.}}$; effective $=2|P-M|$, realised $=2\,\mathrm{side}(P-M_{t+\tau})$
Which cost dominates the spread tells you which strategy the instrument rewards.

**[[Market Maker Inventory Control]]**
$r = s - q\gamma\sigma^2(T-t)$, $\;\delta^a+\delta^b = \gamma\sigma^2(T-t) + \tfrac{2}{\gamma}\ln\!\big(1+\tfrac{\gamma}{\kappa}\big)$ (Avellaneda–Stoikov)
Skew quotes around an inventory-adjusted reservation price; spread widens with volatility and risk aversion.

**[[Queue Position Value]]**
$V(x) = \mathbb{E}\big[\mathbb{1}_{\text{fill}}\,(\tfrac{s}{2} - \text{AS}\mid \text{fill}, x) + \text{rebate}\big]$, $x$ = volume ahead in queue
In large-tick books, front-of-queue orders earn the spread with little adverse selection; back-of-queue fills are toxic.

**[[Order Flow Toxicity (VPIN)]]**
$\mathrm{VPIN} = \dfrac{1}{n}\sum_{\tau=1}^{n}\dfrac{|V^B_\tau - V^S_\tau|}{V}$ over volume buckets; bulk classification $V^B=V\,\Phi\!\big(\Delta P/\sigma_{\Delta P}\big)$
One-sidedness of volume in volume time; high VPIN = dangerous to provide liquidity (use vol-adjusted residual).

## Market Microstructure — market structure

**[[Tick Size Constraints]]**
Regime by $\bar s/\text{tick}$: $\approx 1$ → large-tick (queue competition), $\gg 1$ → small-tick (price competition)
Tick-to-price ratio splits assets into two regimes where almost every book signal behaves differently.

**[[Maker-Taker Fee Economics]]**
Net maker PnL per fill $= \tfrac{s}{2} - \text{AS} + \text{rebate}$; taker cost $= \tfrac{s}{2} + \text{fee}$
Fees are spread-sized in liquid equities, so net-of-fee economics drive quoting and routing.

**[[Cross-Venue Fragmentation]]**
Hasbrouck information share $IS_j = \dfrac{([\psi F]_j)^2}{\psi\Omega\psi^\top}$ from a VECM across venues
Price discovery concentrates on a few venues; the rest echo with latency — routing and lead-lag both follow.

**[[Latency Arbitrage]]**
Profit per race $\approx |\Delta P^{\text{lead}}| - \tfrac{s}{2} - \text{fees}$ when $\Delta t_{\text{info}} < \Delta t_{\text{cancel}}$
Fastest trader snipes stale quotes after a move in a correlated venue; makers price this into spreads.

**[[Opening and Closing Auctions]]**
Clearing price $P^* = \arg\max_P \min\big(D(P), S(P)\big)$; signal: published imbalance $I_{\text{MOC}}$ and its revisions
Call auctions (close ≈ 10%+ of US volume) have their own predictable flow and post-auction reversion.

## Market Microstructure — cross-instrument

**[[Futures-ETF Lead-Lag]]**
$r^{\text{ETF}}_t = \sum_{k\ge0}\beta_k\, r^{\text{fut}}_{t-k} + \varepsilon_t$, lead $=\arg\max_k \mathrm{corr}(r^{\text{fut}}_{t-k}, r^{\text{ETF}}_t)$
Index futures lead ETF and cash by milliseconds; raw material for latency arb and a conditioning signal for slower strategies.

**[[ETF Arbitrage and Flows]]**
Premium $\pi_t = \dfrac{P^{\text{ETF}}_t - \mathrm{iNAV}_t}{\mathrm{iNAV}_t}$ (mean-reverts); leveraged rebalance $\Delta = \mathrm{AUM}\cdot L(L-1)\, r_t$
Creation/redemption ties ETF to basket and transmits flows both ways; leveraged ETFs trade with the move at the close.

## Market Microstructure — measurement foundations

**[[Microstructure Noise and Price Discovery]]**
$p^{\text{obs}}_t = p^*_t + u_t$; Roll spread $s = 2\sqrt{-\mathrm{Cov}(\Delta p_t,\Delta p_{t-1})}$; $\mathbb{E}[RV^{(n)}] = IV + 2n\,\mathbb{E}[u^2]$
Observed prices are efficient price plus noise; at high frequency the noise dominates naive estimators.

**[[Volume Clock]]**
Sample bar $k$ when $\sum_{i\in k} V_i \ge \bar V$; under subordination $r_k \approx \text{i.i.d. } \mathcal{N}(0,\sigma^2)$
Sampling by volume instead of time absorbs activity bursts and makes returns closer to Gaussian.

## Execution

**[[Price Impact and Kyle's Lambda]]**
$\Delta P = \lambda\,(x+u)$, $\;\lambda = \dfrac{\sigma_v}{2\sigma_u}$ (Kyle 1985); estimate by regressing $\Delta P_t$ on signed volume
Price moves linearly in net order flow; $\lambda$ is both execution cost and the engine behind OFI-type signals.

**[[Square-Root Law of Market Impact]]**
$\mathcal{I}(Q) = Y\,\sigma_D\sqrt{\dfrac{Q}{V_D}},\quad Y\sim 1$
Metaorder impact is concave in size, near-universally; ~2/3 reverts after completion.

**[[Optimal Execution (Almgren-Chriss)]]**
$\min_{x(t)} \mathbb{E}[C] + \lambda_{\text{risk}}\mathrm{Var}[C]$ ⇒ $x(t) = X\,\dfrac{\sinh(\kappa(T-t))}{\sinh(\kappa T)}$, $\;\kappa=\sqrt{\lambda_{\text{risk}}\sigma^2/\eta}$
Trade off impact (go slow) vs timing risk (go fast); risk aversion front-loads the schedule. TWAP is $\kappa\to0$.

**[[Implementation Shortfall]]**
$IS = \underbrace{\textstyle\sum_i q_i(P_i - P_{\text{dec}})}_{\text{executed}} + \underbrace{(X-\sum_i q_i)(P_{\text{end}} - P_{\text{dec}})}_{\text{opportunity}}$
True trading cost vs a paper portfolio at decision price; the hurdle every signal must clear net.

## Mid-Frequency Signals

**[[Intraday Momentum]]**
$r_{\text{last 30m}} = \alpha + \beta_1\, r_{\text{first 30m}} + \beta_2\, r_{\text{2nd-last 30m}} + \varepsilon$, $\beta_1>0$
The first half-hour (incl. overnight gap) predicts the last half-hour on SPY; strongest on volatile, high-volume days.

**[[Overnight vs Intraday Returns]]**
$r^{\text{daily}}_t = r^{\text{night}}_t + r^{\text{day}}_t$, $\;r^{\text{night}} = \ln\tfrac{O_t}{C_{t-1}}$, $r^{\text{day}} = \ln\tfrac{C_t}{O_t}$
Nearly all of the equity premium accrues overnight; cross-sectional predictability differs by leg.

**[[Short-Term Reversal]]**
$w_i \propto -\big(r_{i,t-k:t} - \bar r_{\text{ind}(i)}\big)$, $k\approx$ 1 day–1 month
Buy recent losers, sell winners: a premium for providing liquidity; profitable gross, thin net of costs.

**[[Pairs Trading and Statistical Arbitrage]]**
$s_t = \ln P^A_t - \beta \ln P^B_t$, $\;ds = \theta(\mu - s)\,dt + \sigma\,dW$, enter at $|z_t| = |s_t-\mu|/\sigma_{\text{eq}} > z^*$; half-life $=\ln 2/\theta$
Trade divergences of economically linked securities back to equilibrium; classic pairs decayed, residual stat-arb survives.

**[[Futures Term Structure and Carry]]**
Carry $C_t = \dfrac{S_t - F_t}{F_t}$ (annualised by maturity); index basis fair value $F = S\,e^{(r-q)T}$
Backwardation predicts positive roll returns for longs; basis dislocations and roll-period flow are tradable.

**[[News and Announcement Effects]]**
Event study $CAR(\tau_1,\tau_2) = \sum_{\tau=\tau_1}^{\tau_2}(r_\tau - \hat r_\tau)$; PEAD on $SUE = \dfrac{E - \mathbb{E}[E]}{\sigma(E)}$; implied move $\approx 0.8\cdot\text{ATM straddle}/S$
Scheduled releases create predictable drift, liquidity withdrawal, and vol patterns around unpredictable content.

**[[Realized Volatility Forecasting]]**
$RV_t = \sum_i r_{t,i}^2$; HAR: $RV_{t+1} = \beta_0 + \beta_d RV_t + \beta_w RV^{(5)}_t + \beta_m RV^{(22)}_t + \varepsilon$
Volatility is highly forecastable from intraday data; three-term HAR is brutally hard to beat.

## Options and Volatility

**[[Options Order Flow as Equity Signal]]**
$O/S = \dfrac{\text{option volume (shares-equiv.)}}{\text{stock volume}}$; signed flow $=\text{open-buy calls} - \text{open-buy puts}$ (delta-weighted)
Informed traders use options for leverage, so option flow leads stock returns over days.

**[[Gamma Exposure and Dealer Hedging]]**
$GEX = \sum_k \mathrm{sign}_k\,\Gamma_k\,OI_k \cdot 100\cdot S^2\cdot 0.01$; hedge flow $\approx -GEX\cdot \Delta S/S$
Long-gamma dealers damp moves, short-gamma dealers amplify them; predicts vol regime, pinning, and momentum vs reversion.

**[[Implied Volatility Surface Dynamics]]**
SVI: $w(k) = a + b\big(\rho(k-m) + \sqrt{(k-m)^2+\sigma^2}\big)$, $w=\sigma_{\text{imp}}^2 T$; signal $= \sigma_{\text{imp}}(K,T) - \hat\sigma_{\text{fit}}(K,T)$
The surface moves in a few modes (level, slope, skew); residuals vs a smooth fit mean-revert.

**[[Variance Risk Premium]]**
$VRP_t = \mathbb{E}^{\mathbb{Q}}_t[RV_{t,t+\tau}] - \mathbb{E}^{\mathbb{P}}_t[RV_{t,t+\tau}] \approx VIX_t^2 - \widehat{RV}_{t+\tau}$
Implied variance exceeds realised on average — crash insurance premium; high VRP also forecasts equity returns.

## Research Methodology

**[[Signal Decay and Alpha Horizon]]**
$IC(h) = \mathrm{corr}(s_t, r_{t,t+h})$, half-life where $IC(h)=\tfrac12 IC(0)$; capacity $\approx \dfrac{\alpha_{\text{per trade}}}{\text{impact per \$}}$
Every signal has a predictive horizon and a lifetime; published anomalies lose ~58% post-publication.

**[[Backtest Overfitting and Deflated Sharpe]]**
$\mathbb{E}[\max_N SR] \approx \sqrt{2\ln N}$; $\;DSR = \Phi\!\left(\dfrac{(\widehat{SR}-SR_0)\sqrt{T-1}}{\sqrt{1-\hat\gamma_3\widehat{SR}+\tfrac{\hat\gamma_4-1}{4}\widehat{SR}^2}}\right)$
Best-of-$N$ backtests inflate Sharpe; deflate for trials, skew, kurtosis and track length.

**[[Triple Barrier Labeling]]**
$y_i = \begin{cases} +1 & \text{upper } P_0(1+k\sigma_t) \text{ hit first}\\ -1 & \text{lower } P_0(1-k\sigma_t) \text{ hit first}\\ \text{sign}(r) \text{ or } 0 & \text{vertical } t_0+h\end{cases}$
Label by which of profit, stop or time barrier is hit first; meta-labeling separates side from size.

## Signal Candidates (`30-Signals/`)

**[[Gamma Regime Conditioned Intraday Momentum]]**
$\text{pos}_{15{:}00\to\text{close}} = \mathrm{sign}(r_{\text{open}\to 15{:}00})\cdot \mathbb{1}_{GEX_t<0}$ (optionally $-1\times$ when $GEX_t \gg 0$)
Take the intraday-momentum trade only on short-dealer-gamma days, where hedging flow chases the move.

**[[OFI Gated by Flow Toxicity]]**
$\text{size}_t = f(\mathrm{OFI}_t)\cdot \mathbb{1}_{\widetilde{VPIN}_t < \theta}$, $\;\widetilde{VPIN} = VPIN - \hat\beta\,\sigma_t$ (vol-adjusted residual)
Follow order-flow imbalance only when flow is benign; stand aside when informed flow would run you over.

**[[Close Auction Imbalance vs Leveraged ETF Flows]]**
$\widehat{D}_{\text{close}} = \sum_{e\in\text{LETFs}} \mathrm{AUM}_e L_e(L_e-1)\, r_t$; surprise $= I_{\text{MOC}}^{\text{published}} - \widehat{D}_{\text{close}}$
Leveraged-ETF rebalance demand is computable before 15:50 imbalance data; trade the prediction and the surprise.

**[[Option Flow Informed Reversal Gate]]**
$w_i = -\tilde r_{i,t-5:t}\cdot \mathbb{1}[N_i < 2]$, $\;N_i = \#\{z_{O/S},\, z_{\text{flow}},\, \Delta\text{skew} \text{ above threshold}\}$
Fade recent moves only when option flow shows no informed footprint; cuts reversal's left tail and turnover.
