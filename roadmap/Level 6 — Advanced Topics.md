---
type: roadmap
level: 6
status: not-started
tags:
  - level-6
  - roadmap
prerequisites:
  - "[[Level 5 — Profitable Strategies]]"
---

# Level 6 — Advanced Topics

**Goal:** Push the frontier — ML-driven signal generation, infrastructure optimization, and sophisticated multi-asset strategies. This is where you compete with (or become) a professional quant operation.

## Sections

### 6.1 Machine Learning for Finance

#### Classification & Prediction
- Random forests, gradient boosting (XGBoost / LightGBM / CatBoost), SVMs
- Application: "Given these 20 features about a prediction market event and current prices, will there be an arb opportunity in the next hour?"
- Key insight: signal-to-noise in finance is terrible compared to typical ML. Regularization and feature selection matter enormously.

- **Resource:** [[Introduction to Statistical Learning (ISLR)]] chapters 5-8. Kaggle "Jane Street Market Prediction" competition notebooks. Microsoft Qlib (17K+ stars) for end-to-end quant research.

#### Feature Engineering for Markets
Raw prices are useless as features. Transform data into signals:
- Returns over multiple windows, rolling volatilities, volume ratios
- [[Order Book]] imbalance metrics (bid volume vs ask volume at various depths)
- Funding rate differentials, open interest changes
- Prediction market probability momentum and acceleration
- Cross-asset features (BTC vol as a feature for altcoin strategies)

- **Resource:** [[Advances in Financial Machine Learning — López de Prado]], chapters 2-5.

#### Cross-Validation in Finance
Standard k-fold CV doesn't work for time series (leaks future into training). You need:
- Walk-forward validation (train on past, test on future, roll forward)
- Purging and embargo to prevent lookahead bias
- Combinatorial purged cross-validation

This is the single biggest source of false confidence in quant backtests.

- **Resource:** [[Advances in Financial Machine Learning — López de Prado]] chapters 7-8.

#### NLP & Sentiment Signals
Process CT posts, news headlines, governance proposals, Discord/Telegram chatter. Use pre-trained models (FinBERT, or Claude API) and focus on the pipeline: unstructured text → quantitative signal → trading decision. Don't train from scratch — build the data flow.

#### Transformers for Time Series (exploratory)
Transformer architectures adapted for financial time series forecasting. Attention mechanisms can capture long-range dependencies that RNNs miss. Still early in finance but promising for multi-asset regime detection.

#### Reinforcement Learning for Trading (exploratory)
RL agents that learn optimal execution or [[Market Making]] policies. Conceptually elegant but hard to make work in practice due to non-stationarity.

- Deep Q-Networks for order execution
- Policy gradient methods for market making
- The challenge of reward signal design in financial RL
- **Resource:** FinRL (10K+ stars) — open-source RL framework for trading

### 6.2 Advanced Infrastructure

#### Low-Latency Architecture
- Event-driven systems vs polling
- In-memory data structures for order book management
- Connection pooling, websocket multiplexing
- Language choice: Python for research, Rust/C++ for latency-critical execution paths
- Consider polars as a 10-50x faster alternative to pandas for large datasets
- FPGA infrastructure for ultra-low-latency strategies (sub-microsecond)
- If pursuing on-chain [[MEV]]: understand block builder APIs, bundle submission, tips

#### Database & Data Engineering
- TimescaleDB for time-series (tick data, order book snapshots)
- Redis for real-time state (current positions, P&L, risk metrics)
- Data pipeline architecture: ingestion → normalization → storage → feature computation → signal → execution
- Handle millions of data points per day without bottlenecks

#### Monitoring & Alerting
- Real-time P&L dashboards
- Strategy health metrics (fill rates, slippage vs expected, latency percentiles)
- Anomaly detection on execution quality
- Automated kill switches triggered by drawdown, error rate, or latency degradation

### 6.3 Advanced Market Microstructure

#### Order Flow Analysis
- Order flow imbalance as a predictor of short-term price movement
- Toxic vs non-toxic flow (informed vs noise traders)
- Volume clock vs time clock — resampling data by volume rather than time reveals different patterns

#### [[Market Impact]] Models (Advanced)
- [[Optimal Execution of Portfolio Transactions — Almgren & Chriss|Almgren-Chriss]] optimal execution model
- Kyle's lambda (permanent price impact per unit of order flow)
- Propagator models for transient impact

#### High-Frequency Patterns
- Lead-lag relationships across venues (which exchange moves first?)
- Microstructure noise and its effect on volatility estimation
- Bid-ask bounce and how it biases naive return calculations

- **Resource:** [[Algorithmic and High-Frequency Trading — Cartea et al.]] (extends [[Avellaneda-Stoikov]]). [[Trades, Quotes and Prices — Bouchaud et al.]] — the best book on empirical market microstructure.

### 6.4 DeFi Quantitative Deep Dives

#### JIT Liquidity Provision
- Provide concentrated liquidity on Uniswap v3 in a tight range right before a large swap, earn fees, withdraw immediately after
- MEV-adjacent, competitive on mainnet, thinner on L2s
- Requires tick math mastery and mempool monitoring

#### LP as Options
- Providing liquidity is economically equivalent to selling options (short gamma/straddle)
- Price this correctly using options theory: Black-Scholes analog for AMM LP positions
- Understand when LPing is +EV vs just being short vol

#### MEV Supply Chain Participation
Instead of competing as a searcher:
- Running a builder
- Operating a relay
- Providing order flow
- Different risk/reward profile, less zero-sum than searching

### 6.5 Advanced Derivatives

#### Exotic Options
Barrier options, Asian options, lookback options — these appear in structured DeFi products and require MC simulation or PDE methods to price.

#### Advanced Volatility Models
- Heston stochastic volatility model — vol is itself a random process, captures the vol smile
- Merton jump-diffusion — adds Poisson jumps to GBM for sudden moves (crypto-relevant)
- Local volatility (Dupire) — calibrate the vol surface from market prices

#### Martingale Pricing
Discounted prices are martingales under the risk-neutral measure. Understand the change of measure (Girsanov's theorem) and why it matters for derivative pricing. This is the theoretical foundation beneath Black-Scholes.

### 6.6 Advanced Statistical Methods

#### Bayesian Methods for Trading
- Prior beliefs + new data → updated beliefs. Natural framework for combining prediction market signals with other information sources.
- Bayesian updating of strategy parameters as market regime changes
- Bayesian portfolio optimization (Black-Litterman model)

#### Kalman Filters
- State-space models for tracking hidden variables (true price, true spread, true volatility)
- Application: estimate the "true" fair value of an asset given noisy observations from multiple venues
- Pairs trading with Kalman filter for dynamic hedge ratio estimation

#### Extreme Value Theory
- Model the tails of return distributions properly (not just assume normal)
- Estimate the probability and magnitude of extreme losses
- Critical for proper risk management in crypto (where 20%+ daily moves happen)

- **Resource:** [[Quantitative Risk Management — McNeil, Frey & Embrechts]] for EVT. Any Bayesian statistics textbook + [[Dynamic Replication and Hedging — Kolm & Ritter]] for Kalman filters in finance.

## Prerequisites
- [[Level 5 — Profitable Strategies]]
