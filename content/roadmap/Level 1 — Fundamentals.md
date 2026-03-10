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

- **Resource:** [[Khan Academy — Algebra II & Precalculus]]. Skip what you know, but don't skip [[Logarithms and Exponentials]].

#### Calculus
[[Derivatives]] (single and partial), [[Integrals]], [[Chain Rule]], product rule. You need to understand "rate of change of X with respect to Y" intuitively. [[Taylor Series]] / asymptotic expansions are used heavily in the [[Avellaneda-Stoikov]] paper and in approximating nonlinear systems.

- **Resource:** [[3Blue1Brown — Essence of Calculus]] (~3 hours, for intuition). Then [[Khan Academy — Calculus]] for drill. Focus on: derivatives, partial derivatives, chain rule, basic integration, Taylor series.

#### Linear Algebra
Vectors, matrices, dot products, systems of equations. But also eigenvalue decomposition, quadratic forms, and covariance matrices — these are the machinery behind [[Portfolio Optimization]], PCA, and neural networks. The covariance matrix Σ encodes all pairwise relationships. Portfolio variance is a quadratic form: `w^T Σ w`. The first 5 eigenvectors of stock returns typically explain ~70% of variance — this is the basis of factor investing.

- **Resource:** [[3Blue1Brown — Essence of Linear Algebra]] (~3 hours, for intuition). Then [[MIT 18.06 — Linear Algebra]] for depth. [[Introduction to Linear Algebra — Gilbert Strang]] for problems.
- **Exercise:** PCA on a basket of crypto returns — plot the eigenvalue spectrum, identify what the top components represent. Implement Markowitz mean-variance optimization from scratch using numpy.

### 1.2 Probability & Statistics

#### Core Probability
Random variables (discrete and continuous), [[Probability Distributions]], [[Expected Value]], [[Variance]], standard deviation, probability density functions, [[Conditional Probability]], independence, [[Bayes' Theorem]]. The core question: "What are the odds, and are the odds in my favor?" Expected value is conviction, variance is risk. [[Bayes' Theorem]] is how you update beliefs with new information — this is conditional thinking applied everywhere.

- **Resource:** [[Introduction to Probability — Blitzstein & Hwang]], chapters 1-6 (free Harvard PDF). Or [[Harvard Stat 110]] lectures on YouTube.
- **Exercise:** Simulate 10,000 coin flips and verify the law of large numbers. Implement a Bayesian updater: start with a prior, feed in observations, watch the posterior converge.

#### Key Distributions
Each of these shows up repeatedly in quant finance:

- **[[Normal Distribution]]** — price returns are modeled as normal. Understand the bell curve, standard deviations, z-scores.
- **[[Log-Normal Distribution]]** — prices themselves (not returns) are often log-normal. This is why [[Geometric Brownian Motion]] uses `dS/S = σdW`.
- **[[Exponential Distribution]]** — models waiting times between random events. "How long until the next order arrives?"
- **[[Poisson Distribution]]** — counts events in a time window. "How many orders arrive per second?" The [[Avellaneda-Stoikov]] paper models order arrivals as [[Poisson Process]]es. This is essential.
- **[[Power Law Distribution]]** — heavy-tailed distributions. Market order sizes follow power laws. Understand what "[[Fat Tails]]" means — extreme events happen far more often than a normal distribution predicts.

- **Resource:** Continue [[Harvard Stat 110]], or [[Introduction to Probability — Blitzstein & Hwang]] (free PDF). For power laws: first sections of [[Power-Law Distributions in Empirical Data — Clauset et al.]].

#### Stochastic Processes — Intro
This bridges basic probability into the continuous-time world:

- **[[Random Walk]]** — a sequence of random steps. The discrete version of what stock prices do. Simulate one in code.
- **[[Markov Property]]** — the future depends only on the present state, not the path taken to get there. Most financial models assume this.
- **[[Poisson Process]]** — events arriving randomly at rate λ. Understand intensity, inter-arrival times ([[Exponential Distribution]]), and how to model "orders arrive at rate λ(δ)."
- **[[Brownian Motion]]** (conceptual) — the continuous limit of a [[Random Walk]]. The mid-price in [[Avellaneda-Stoikov]] follows `dS = σdW`. For now, understand it intuitively as "a continuous random wiggle with volatility σ."

- **Resource:** [[Introduction to Probability Models — Sheldon Ross]], chapters 5 (Poisson) and 10 (Brownian motion). Read for understanding, not for solving every exercise.

### 1.3 Programming for Quant (parallel with math)

#### Python Data Science Stack
Python is the lingua franca. Focus on the quant-specific libraries:

- **numpy** — numerical computation, arrays, vectorized operations
- **pandas** — DataFrames, time series manipulation. You will live in pandas.
- **matplotlib / plotly** — visualization. Plot everything you study.
- **scipy** — statistics functions, optimization, signal processing
- **statsmodels** — regression, time series models, statistical tests

- **Resource:** [[Python for Data Analysis — Wes McKinney]]. Get productive fast.

#### Practical Exercises
- Fetch historical price data (use `ccxt` library for crypto exchange data)
- Plot candlestick charts, order book snapshots, volume profiles
- Calculate returns, rolling volatility, correlation matrices
- Simulate a [[Random Walk]] and a [[Poisson Process]] in code

### 1.4 Market Mechanics from Zero

#### How Markets Work
Start from absolute basics:

- **[[Order Types]]:** market orders (execute now at best available) vs limit orders (execute only at my price or better). This distinction is the entire foundation of [[Market Making]].
- **[[Order Book]]:** a live queue of all outstanding limit orders organized by price. Bid side (buyers), ask side (sellers). The [[Spread]] = best ask minus best bid.
- **How trades happen:** a market order arrives and "eats" limit orders from the book. "Lifting the ask" = buying. "Hitting the bid" = selling.
- **Depth and [[Liquidity]]:** how many orders sit at each price level and why it matters for execution.
- **[[Slippage]]:** the difference between the price you expected and the price you got, caused by consuming multiple price levels.

**Hands-on:** Open Binance or Bybit, pick BTC/USDT, and watch the [[Order Book]] live for 30 minutes. See orders placed, cancelled, and filled in real time.

- **Resource:** [[Trading and Exchanges — Larry Harris]], chapters 1-6. THE book for market structure from scratch.

#### Market Making
This is what the [[Avellaneda-Stoikov]] paper models:

- **What a [[Market Maker]] does:** posts limit orders on both sides, earns the [[Spread]], carries [[Inventory Risk]].
- **[[Inventory Risk]]:** if you keep buying and price drops, your accumulated inventory loses value. This is the central problem the paper solves.
- **[[Adverse Selection]]:** sometimes counterparties know something you don't. When informed traders hit your quotes, you're on the wrong side.
- **The [[Spread]] as compensation:** bid-ask spread exists because market makers need payment for these risks.

- **Resource:** [[Trading and Exchanges — Larry Harris]] chapters 7-13. Also: [[The Economics of the Dealer Function — Treynor]]. Search YouTube for Jane Street and Optiver talks on market making.

#### DEX and CEX Specifics
Map general concepts to crypto venues:

- **CEX [[Order Book]]s:** Binance, Bybit, Coinbase — traditional limit order books for crypto. APIs, websocket feeds, L2 data.
- **[[AMM]]s and DEXs:** Uniswap, Curve. Fundamentally different — liquidity via mathematical formulas. Understand [[Constant Product Formula]] (`x*y=k`), how swaps work, [[Slippage]], [[Impermanent Loss]] for LPs.
- **Key difference:** on CEX you choose your price; on AMM the formula determines price. [[Avellaneda-Stoikov]] models order book markets, but understanding both is essential for cross-venue arb.

- **Resource:** [[Uniswap v2 Whitepaper]] (5 pages, very readable). Binance API docs — connect to a websocket and stream order book data.

## Prerequisites
None — this is the starting level.

## Unlocks
- [[Level 2 — Basic Probabilistic Arbitrage]]
