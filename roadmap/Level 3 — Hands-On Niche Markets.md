---
type: roadmap
level: 3
status: not-started
tags:
  - level-3
  - roadmap
prerequisites:
  - "[[Level 2 — Basic Probabilistic Arbitrage]]"
---

# Level 3 — Hands-On, Barely Profitable Quant in Niche Markets

**Goal:** Run your first real strategies on small capital in low-competition niches. Learn what actually works vs what looks good on paper. Expect to break even or lose small amounts — you're paying tuition.

## Sections

### 3.1 Statistics & Econometrics for Trading

#### [[Regression]] & [[Correlation]]
Linear regression, multiple regression, R², residuals, p-values. This is your primary tool for modeling "when prediction market probability moves X%, spot price moves Y%." [[Logistic Regression]] for binary outcome modeling (prediction markets output probabilities).

Deeply understand correlation ≠ causation. In markets, spurious correlations will bankrupt you.

- **Resource:** [[Introduction to Statistical Learning (ISLR)]], chapters 2-4. Free PDF, excellent writing.

#### [[Time Series Analysis]]
Financial data is sequential. You need:

- **[[Autocorrelation]]** / partial autocorrelation — does today's return predict tomorrow's?
- **[[Stationarity]]** — prices are non-stationary, but returns and spreads often are. Augmented Dickey-Fuller test to check.
- **[[ARIMA]]** — AR, MA, ARMA, ARIMA — workhorses of time series. Model mean-reverting processes.
- **[[Cointegration]]** — arguably the single most important concept for stat arb. Two prices can each be random walks, but their *spread* is mean-reverting. This is the math behind pairs trading and cross-venue arb. Engle-Granger method, Johansen test.
- **[[GARCH]]** — volatility is predictable. Big moves follow big moves (volatility clustering). Model and forecast it.

- **Resource:** [[Analysis of Financial Time Series — Ruey Tsay]], chapters 1-3 and 8. Or [[Algorithmic Trading — Ernie Chan]] for code-first approach with cointegration strategies.

#### Maximum Likelihood Estimation
MLE is how you fit distributions to data properly. Financial returns aren't normal — fitting a t-distribution via MLE gives you fatter tails and better risk estimates. Understand likelihood functions, log-likelihood, and why MLE is the workhorse of parametric statistics.

- **Exercise:** Download real stock/crypto returns, test for normality (they'll fail), fit a t-distribution via MLE, compare tail probabilities.

#### Hypothesis Testing & Avoiding Self-Deception
p-values, confidence intervals, multiple testing correction (test 100 strategies → 5 look significant by chance). [[Overfitting]] and data snooping are the graveyard of quant strategies. Know Bonferroni correction (conservative) and Benjamini-Hochberg (less conservative, controls false discovery rate). Use Newey-West standard errors for financial data — standard errors are wrong when returns are autocorrelated or heteroskedastic.

- **Resource:** [[All of Statistics — Larry Wasserman]], chapters 1-13. [[Introduction to Statistical Learning (ISLR)]] chapters 2-3. [[The Deflated Sharpe Ratio — Bailey & López de Prado]] for finance-specific multiple testing.
- **Exercise:** Run a Fama-French 3-factor regression using statsmodels — decompose returns into market, size, and value factors. Then run a permutation test: shuffle returns 10,000 times and compare your strategy's Sharpe to the shuffled distribution.

### 3.2 Prediction Market Theory

#### How Prediction Markets Work
- Order book-based (Polymarket, Kalshi) vs AMM-based (Azuro). CLOB prediction markets = normal exchange but the asset is a binary contract paying $1 on event resolution.
- How prices map to implied probabilities. How resolution works. How liquidity provision works.
- The [[Logarithmic Market Scoring Rule]] (LMSR) by Robin Hanson: the cost function tracks outstanding shares, the price function is a softmax (same function powering neural network classifiers). Prices always sum to 1 and lie in (0,1). Market maker's max loss is bounded at `b × ln(n)` where n is the number of outcomes.

#### Calibration and Efficiency
How well-calibrated are prediction markets? Generally good in aggregate but significantly wrong on individual events, especially illiquid or asymmetric-information ones. Read Manski on interpreting prediction market prices.

#### Cross-Venue Information Flow
This is your [[Statistical Arbitrage]] edge:
- Event happens → informed traders move prediction market → signal propagates to spot/derivatives
- Participant pools differ: prediction market traders are event-focused, CEX/DEX traders are price-action focused. Information transfer isn't instant.
- Build a taxonomy: event types × affected assets × typical propagation delay × historical edge

- **Resource:** Robin Hanson's papers on prediction markets. Polymarket docs + historical resolution data. Academic literature on "event studies."

### 3.3 Backtesting & Simulation

#### Build a Backtesting Framework
Either build your own or learn vectorbt / Backtrader. The framework must model:
- Realistic transaction costs (exchange fees, gas, slippage)
- [[Market Impact]] (your order moves the price)
- Latency (you see a price, but by the time you execute, it's moved)
- Funding rates (for perp strategies)

#### Critical Pitfalls
- **Survivorship bias** — only testing on assets that still exist / are still listed
- **Lookahead bias** — accidentally using future data in your model
- **[[Overfitting]]** — a strategy that fits historical data perfectly but has zero predictive power
- **Transaction cost underestimation** — the #1 killer of paper-profitable strategies

#### What to Backtest First
- Simple mean reversion on cross-venue spreads (CEX-CEX or CEX-DEX)
- Prediction market probability changes → correlated asset price moves
- Funding rate convergence across perp DEXs

- **Resource:** [[Algorithmic Trading — Ernie Chan]] — the best practical backtesting guide with code. [[Advances in Financial Machine Learning — López de Prado]], chapters 7-8 on cross-validation for financial data.

### 3.4 Risk Management (non-negotiable)

#### [[Position Sizing]]
- **[[Kelly Criterion]]** — mathematically optimal bet size given your edge and variance. In practice use fractional Kelly (1/2 or 1/4) because real tails are fatter than your model assumes.
- Why even a positive-edge strategy ruins you with wrong sizing.

- **Resource:** [[A Man for All Markets — Ed Thorp]] for intuition. Original Kelly paper (short, readable).

#### Risk Metrics
- [[Value at Risk]] (VaR) — nearly useless for crypto due to [[Fat Tails]]
- [[Expected Shortfall]] (Conditional VaR) — better, measures average loss in worst scenarios
- [[Maximum Drawdown]] — what actually kills strategies in practice
- [[Sharpe Ratio]], [[Sortino Ratio]] — risk-adjusted return measures

#### Crypto-Specific Risks
- Exchange counterparty risk (FTX)
- Smart contract risk (exploits, rug pulls)
- [[Liquidity]] risk (order book is deep until it isn't)
- Oracle manipulation risk
- Bridge risk (cross-chain)
- Regulatory risk (exchange delistings, jurisdiction changes)

#### Correlation & Contagion
In calm markets, assets have normal correlations. In a crash, everything goes to 1. Your "diversified" portfolio becomes a single concentrated bet. Stress test against historical crashes (March 2020, May 2021, FTX November 2022).

- **Resource:** [[Quantitative Risk Management — McNeil, Frey & Embrechts]], chapters 1-4, 7.

### 3.5 First Live Strategies

#### Go live with tiny capital. Rules:
- Start with ONE well-understood strategy on ONE venue pair
- Maximum position size: amount you can afford to lose entirely
- Hard stop-loss per hour and per day
- Kill switch that flattens all positions instantly
- Monitor obsessively — check every 30 minutes initially
- Log everything: every order, fill, rejection, error, P&L tick

#### Good First Strategies
- **Stablecoin DEX arb** — USDC/USDT spread across Curve pools on different L2s. Low risk, low reward, teaches execution mechanics.
- **Simple CEX-CEX spread** — BTC or ETH price difference between two exchanges. Mostly competed away but teaches the full pipeline.
- **[[Funding Rate Arbitrage]] harvesting** — go long on a venue with negative funding, short on one with positive funding. Delta neutral. Capital-intensive but conceptually simple.

#### What You're Learning (Not Earning)
The goal isn't profit. It's validating that your system works end-to-end: data ingestion → signal → execution → position management → P&L tracking. Every failure here saves you from a bigger failure later.

## Prerequisites
- [[Level 2 — Basic Probabilistic Arbitrage]]

## Unlocks
- [[Level 4 — MEV & Algorithmic Trading]]
