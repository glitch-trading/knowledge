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

## Combinatorial / Prediction-Market Arbitrage (Level 5)
- [[Combinatorial Prediction Markets]] — marginal-polytope arbitrage across logically linked events
- [[Bregman Divergence]] / [[Frank-Wolfe Algorithm]] — math + algorithm for projection onto the arbitrage-free polytope
- Integer Programming for arbitrage detection (constraint generation; Gurobi / HiGHS / CPLEX)

## Execution Risk
- [[Leg Risk]] — non-atomic multi-leg fills; capacity bound = $\Delta p \cdot \min$(leg volumes)

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

## Risk & Sizing
- [[Kelly Criterion]]
- [[Position Sizing]]
- [[Sharpe Ratio]] / [[Sortino Ratio]]
- [[Maximum Drawdown]]
- [[Overfitting]] and backtest pitfalls
