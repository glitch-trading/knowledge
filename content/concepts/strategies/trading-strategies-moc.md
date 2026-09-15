---
title: "Trading Strategies — Map of Content"
type: MOC
tags:
  - MOC
  - strategies
---

## Arbitrage Types
- [[spatial-arbitrage|Spatial Arbitrage]]
- [[triangular-arbitrage|Triangular Arbitrage]]
- [[cross-chain-arbitrage|Cross-Chain Arbitrage]]
- [[cex-dex-arbitrage|CEX-DEX Arbitrage]]
- [[funding-rate-arbitrage|Funding Rate Arbitrage]]
- [[statistical-arbitrage|Statistical Arbitrage]]

## Stat Arb Specifics
- [[cointegration|Cointegration]]-based pairs trading
- Prediction market ↔ spot/derivatives signals
- Cross-venue information flow

## Strategy Archetypes
- [[mean-reversion|Mean Reversion]]
- Trend following / momentum
- Breakout vs. range-extremity fade (HTF-context dependent)

## Signal Construction
- [[technical-indicators-moc|Technical Indicators MOC]] — trend/volatility/momentum/volume features that feed strategy rules

## Prediction Markets
- [[prediction-markets|Prediction Markets]] (Polymarket, Kalshi, Azuro)
- [[logarithmic-market-scoring-rule|Logarithmic Market Scoring Rule]] (LMSR AMM)
- [[interpreting-prediction-market-prices-manski|Interpreting Prediction Market Prices — Manski]] — price ≠ probability under realistic conditions
- Edge measurement: [[kl-divergence|KL Divergence]] in bits per trade
- Signal fusion: [[maximum-entropy-principle|Maximum Entropy Principle]]
- Anomaly / insider-flow detection: rolling [[shannon-entropy|Shannon Entropy]] with $|dH/dt|$ threshold

## Combinatorial / Prediction-Market Arbitrage (Level 5)
- [[combinatorial-prediction-markets|Combinatorial Prediction Markets]] — marginal-polytope arbitrage across logically linked events
- [[bregman-divergence|Bregman Divergence]] / [[frank-wolfe-algorithm|Frank-Wolfe Algorithm]] — math + algorithm for projection onto the arbitrage-free polytope
- Integer Programming for arbitrage detection (constraint generation; Gurobi / HiGHS / CPLEX)

## Execution Risk
- [[leg-risk|Leg Risk]] — non-atomic multi-leg fills; capacity bound = $\Delta p \cdot \min$(leg volumes)

## DeFi Strategies
- Stablecoin DEX arb
- [[liquidation-botting|Liquidation Botting]]
- JIT liquidity provision
- LP as options (short gamma)
- New protocol launch dynamics
- Token unlock trading

## Carry / Yield
- Funding rate harvesting
- Basis trading (perp vs spot)

## Alpha Construction & Combination
- [[information-coefficient|Information Coefficient]]
- [[information-ratio|Information Ratio]]
- [[fundamental-law-of-active-management|Fundamental Law of Active Management]] (IR ≈ IC · √breadth)
- [[alpha-combination|Alpha Combination]] — weighting many weak signals into a single forecast
- [[fama-french-factor-model|Fama-French Factor Model]] — canonical multi-factor decomposition

## Risk & Sizing
- [[kelly-criterion|Kelly Criterion]] (incl. uncertainty-adjusted empirical Kelly)
- [[position-sizing|Position Sizing]]
- [[sharpe-ratio|Sharpe Ratio]] / [[sortino-ratio|Sortino Ratio]] / [[information-ratio|Information Ratio]]
- [[maximum-drawdown|Maximum Drawdown]]
- [[overfitting|Overfitting]] and backtest pitfalls

## Process & Execution Discipline
- [[trade-journaling|Trade Journaling]]
- [[trading-psychology|Trading Psychology]]
- [[market-profile|Market Profile]] (TPO — trade location & confluence)
