---
title: "Trading Strategies — Map of Content"
type: MOC
tags:
  - MOC
  - strategies
---

## Arbitrage Types
- [[Spatial Arbitrage]]
- [[Triangular Arbitrage]]
- [[Cross-Chain Arbitrage]]
- [[CEX-DEX Arbitrage]]
- [[Funding Rate Arbitrage]]
- [[Statistical Arbitrage]]

## Stat Arb Specifics
- [[Cointegration]]-based pairs trading
- Prediction market ↔ spot/derivatives signals
- Cross-venue information flow

## Strategy Archetypes
- [[Mean Reversion]]
- Trend following / momentum
- Breakout vs. range-extremity fade (HTF-context dependent)

## Prediction Markets
- [[Prediction Markets]] (Polymarket, Kalshi, Azuro)
- [[Logarithmic Market Scoring Rule]] (LMSR AMM)
- [[Interpreting Prediction Market Prices — Manski]] — price ≠ probability under realistic conditions
- Edge measurement: [[KL Divergence]] in bits per trade
- Signal fusion: [[Maximum Entropy Principle]]
- Anomaly / insider-flow detection: rolling [[Shannon Entropy]] with $|dH/dt|$ threshold

## DeFi Strategies
- Stablecoin DEX arb
- [[Liquidation Botting]]
- JIT liquidity provision
- LP as options (short gamma)
- New protocol launch dynamics
- Token unlock trading

## Carry / Yield
- Funding rate harvesting
- Basis trading (perp vs spot)

## Alpha Construction & Combination
- [[Information Coefficient]]
- [[Information Ratio]]
- [[Fundamental Law of Active Management]] (IR ≈ IC · √breadth)
- [[Alpha Combination]] — weighting many weak signals into a single forecast
- [[Fama-French Factor Model]] — canonical multi-factor decomposition

## Risk & Sizing
- [[Kelly Criterion]] (incl. uncertainty-adjusted empirical Kelly)
- [[Position Sizing]]
- [[Sharpe Ratio]] / [[Sortino Ratio]] / [[Information Ratio]]
- [[Maximum Drawdown]]
- [[Overfitting]] and backtest pitfalls

## Process & Execution Discipline
- [[Trade Journaling]]
- [[Trading Psychology]]
- [[Market Profile]] (TPO — trade location & confluence)
