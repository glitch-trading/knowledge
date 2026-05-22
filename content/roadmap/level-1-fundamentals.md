---
title: "Level 1 — Fundamentals"
type: roadmap
level: 1
status: not-started
tags:
  - level-1
  - roadmap
---

**Goal:** Build the mathematical, programming, and market literacy foundation that everything else sits on. Nothing here is optional.

## Sections

### 1.1 Mathematical Foundations

#### Algebra & Functions Refresher
Logarithms (natural log especially), exponentials, summation/product notation, multi-variable function notation. You'll see `e^(-γx)`, `ln(1 + γ/k)`, and nested functions everywhere — these need to be effortless to read.

- **Resource:** [[khan-academy-algebra-ii-and-precalculus|Khan Academy — Algebra II & Precalculus]]. Skip what you know, but don't skip [[logarithms-and-exponentials|Logarithms and Exponentials]].

#### Calculus
[[derivatives|Derivatives]] (single and partial), [[integrals|Integrals]], [[chain-rule|Chain Rule]], product rule. You need to understand "rate of change of X with respect to Y" intuitively. [[taylor-series|Taylor Series]] / asymptotic expansions are used heavily in the [[avellaneda-stoikov|Avellaneda-Stoikov]] paper and in approximating nonlinear systems.

- **Resource:** [[3blue1brown-essence-of-calculus|3Blue1Brown — Essence of Calculus]] (~3 hours, for intuition). Then [[khan-academy-calculus|Khan Academy — Calculus]] for drill. Focus on: derivatives, partial derivatives, chain rule, basic integration, Taylor series.

#### Linear Algebra
Vectors, matrices, dot products, systems of equations. But also eigenvalue decomposition, quadratic forms, and covariance matrices — these are the machinery behind [[portfolio-optimization|Portfolio Optimization]], PCA, and neural networks. The covariance matrix Σ encodes all pairwise relationships. Portfolio variance is a quadratic form: `w^T Σ w`. The first 5 eigenvectors of stock returns typically explain ~70% of variance — this is the basis of factor investing.

- **Resource:** [[3blue1brown-essence-of-linear-algebra|3Blue1Brown — Essence of Linear Algebra]] (~3 hours, for intuition). Then [[mit-18-06-linear-algebra|MIT 18.06 — Linear Algebra]] for depth. [[introduction-to-linear-algebra-gilbert-strang|Introduction to Linear Algebra — Gilbert Strang]] for problems.
- **Exercise:** PCA on a basket of crypto returns — plot the eigenvalue spectrum, identify what the top components represent. Implement Markowitz mean-variance optimization from scratch using numpy.

### 1.2 Probability & Statistics

#### Core Probability
Random variables (discrete and continuous), [[probability-distributions|Probability Distributions]], [[expected-value|Expected Value]], [[variance|Variance]], standard deviation, probability density functions, [[conditional-probability|Conditional Probability]], independence, [[bayes-theorem|Bayes' Theorem]]. The core question: "What are the odds, and are the odds in my favor?" Expected value is conviction, variance is risk. [[bayes-theorem|Bayes' Theorem]] is how you update beliefs with new information — this is conditional thinking applied everywhere.

- **Resource:** [[introduction-to-probability-blitzstein-and-hwang|Introduction to Probability — Blitzstein & Hwang]], chapters 1-6 (free Harvard PDF). Or [[harvard-stat-110|Harvard Stat 110]] lectures on YouTube. Then drill base-rate problems and indicator-variable tricks from the **MIT Quant Bible** (MIT Sloan Business Club PDF, sections 2-3) — the same patterns repeat across quant phone screens.
- **Exercise:** Simulate 10,000 coin flips and verify the law of large numbers. Implement a Bayesian updater: start with a prior, feed in observations, watch the posterior converge.

#### Key Distributions
Each of these shows up repeatedly in quant finance:

- **[[normal-distribution|Normal Distribution]]** — price returns are modeled as normal. Understand the bell curve, standard deviations, z-scores.
- **[[log-normal-distribution|Log-Normal Distribution]]** — prices themselves (not returns) are often log-normal. This is why [[geometric-brownian-motion|Geometric Brownian Motion]] uses `dS/S = σdW`.
- **[[exponential-distribution|Exponential Distribution]]** — models waiting times between random events. "How long until the next order arrives?"
- **[[poisson-distribution|Poisson Distribution]]** — counts events in a time window. "How many orders arrive per second?" The [[avellaneda-stoikov|Avellaneda-Stoikov]] paper models order arrivals as [[poisson-process|Poisson Process]]es. This is essential.
- **[[power-law-distribution|Power Law Distribution]]** — heavy-tailed distributions. Market order sizes follow power laws. Understand what "[[fat-tails|Fat Tails]]" means — extreme events happen far more often than a normal distribution predicts.

- **Resource:** Continue [[harvard-stat-110|Harvard Stat 110]], or [[introduction-to-probability-blitzstein-and-hwang|Introduction to Probability — Blitzstein & Hwang]] (free PDF). For power laws: first sections of [[power-law-distributions-in-empirical-data-clauset-et-al|Power-Law Distributions in Empirical Data — Clauset et al.]].

#### Stochastic Processes — Intro
This bridges basic probability into the continuous-time world:

- **[[random-walk|Random Walk]]** — a sequence of random steps. The discrete version of what stock prices do. Simulate one in code.
- **[[markov-property|Markov Property]]** — the future depends only on the present state, not the path taken to get there. Most financial models assume this.
- **[[markov-chain|Markov Chain]]** — the discrete companion to the property: a transition matrix $\mathbf{P}$ over a finite state space. MLE is "count transitions, normalize rows." $n$-step forecasts collapse to $\mathbf{P}^n$ (Chapman-Kolmogorov). The stationary distribution $\boldsymbol\pi$ from $\boldsymbol\pi\mathbf{P} = \boldsymbol\pi$ is the long-run baseline. Foundation for [[regime-switching|Regime Switching]] in Level 5 and [[hidden-markov-models|Hidden Markov Models]] in Level 6.
- **[[poisson-process|Poisson Process]]** — events arriving randomly at rate λ. Understand intensity, inter-arrival times ([[exponential-distribution|Exponential Distribution]]), and how to model "orders arrive at rate λ(δ)."
- **[[brownian-motion|Brownian Motion]]** (conceptual) — the continuous limit of a [[random-walk|Random Walk]]. The mid-price in [[avellaneda-stoikov|Avellaneda-Stoikov]] follows `dS = σdW`. For now, understand it intuitively as "a continuous random wiggle with volatility σ."

- **Resource:** [[introduction-to-probability-models-sheldon-ross|Introduction to Probability Models — Sheldon Ross]], chapters 5 (Poisson) and 10 (Brownian motion). Read for understanding, not for solving every exercise.

### 1.3 Programming for Quant (parallel with math)

#### Python Data Science Stack
Python is the lingua franca. Focus on the quant-specific libraries:

- **numpy** — numerical computation, arrays, vectorized operations
- **pandas** — DataFrames, time series manipulation. You will live in pandas.
- **matplotlib / plotly** — visualization. Plot everything you study.
- **scipy** — statistics functions, optimization, signal processing
- **statsmodels** — regression, time series models, statistical tests

- **Resource:** [[python-for-data-analysis-wes-mckinney|Python for Data Analysis — Wes McKinney]]. Get productive fast.

#### Practical Exercises
- Fetch historical price data (use `ccxt` library for crypto exchange data)
- Plot candlestick charts, order book snapshots, volume profiles
- Calculate returns, rolling volatility, correlation matrices
- Simulate a [[random-walk|Random Walk]] and a [[poisson-process|Poisson Process]] in code

### 1.4 Market Mechanics from Zero

#### How Markets Work
Start from absolute basics:

- **[[order-types|Order Types]]:** market orders (execute now at best available) vs limit orders (execute only at my price or better). This distinction is the entire foundation of [[market-making|Market Making]].
- **[[order-book|Order Book]]:** a live queue of all outstanding limit orders organized by price. Bid side (buyers), ask side (sellers). The [[spread|Spread]] = best ask minus best bid.
- **How trades happen:** a market order arrives and "eats" limit orders from the book. "Lifting the ask" = buying. "Hitting the bid" = selling.
- **Depth and [[liquidity|Liquidity]]:** how many orders sit at each price level and why it matters for execution.
- **[[slippage|Slippage]]:** the difference between the price you expected and the price you got, caused by consuming multiple price levels.

**Hands-on:** Open Binance or Bybit, pick BTC/USDT, and watch the [[order-book|Order Book]] live for 30 minutes. See orders placed, cancelled, and filled in real time.

- **Resource:** [[trading-and-exchanges-larry-harris|Trading and Exchanges — Larry Harris]], chapters 1-6. THE book for market structure from scratch.

#### Market Making
This is what the [[avellaneda-stoikov|Avellaneda-Stoikov]] paper models:

- **What a [[market-maker|Market Maker]] does:** posts limit orders on both sides, earns the [[spread|Spread]], carries [[inventory-risk|Inventory Risk]].
- **[[inventory-risk|Inventory Risk]]:** if you keep buying and price drops, your accumulated inventory loses value. This is the central problem the paper solves.
- **[[adverse-selection|Adverse Selection]]:** sometimes counterparties know something you don't. When informed traders hit your quotes, you're on the wrong side.
- **The [[spread|Spread]] as compensation:** bid-ask spread exists because market makers need payment for these risks.

- **Resource:** [[trading-and-exchanges-larry-harris|Trading and Exchanges — Larry Harris]] chapters 7-13. Also: [[the-economics-of-the-dealer-function-treynor|The Economics of the Dealer Function — Treynor]]. Search YouTube for Jane Street and Optiver talks on market making. The **MIT Quant Bible** market-making chapter (Sloan Business Club PDF, section 6) covers the trader-side mental model — three determinants of a quote (theo, last traded, current position) and how to skew when inventory is non-flat.

#### DEX and CEX Specifics
Map general concepts to crypto venues:

- **CEX [[order-book|Order Book]]s:** Binance, Bybit, Coinbase — traditional limit order books for crypto. APIs, websocket feeds, L2 data.
- **[[amm|AMM]]s and DEXs:** Uniswap, Curve. Fundamentally different — liquidity via mathematical formulas. Understand [[constant-product-formula|Constant Product Formula]] (`x*y=k`), how swaps work, [[slippage|Slippage]], [[impermanent-loss|Impermanent Loss]] for LPs.
- **Key difference:** on CEX you choose your price; on AMM the formula determines price. [[avellaneda-stoikov|Avellaneda-Stoikov]] models order book markets, but understanding both is essential for cross-venue arb.

- **Resource:** [[uniswap-v2-whitepaper|Uniswap v2 Whitepaper]] (5 pages, very readable). Binance API docs — connect to a websocket and stream order book data.

## Prerequisites
None — this is the starting level.

## Unlocks
- [[level-2-basic-probabilistic-arbitrage|Level 2 — Basic Probabilistic Arbitrage]]
