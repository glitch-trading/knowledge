---
type: concept
title: "Logarithmic Market Scoring Rule"
tags:
  - concept
  - prediction-markets
  - market-making
level: 3
prerequisites:
  - "[[Probability Distributions]]"
  - "[[Expected Value]]"
---

## What It Is

An automated market maker mechanism for prediction markets, designed by Robin Hanson. The LMSR maintains a cost function over outstanding shares for each outcome and derives prices as a softmax (the same function used in neural network classifiers). Prices always sum to 1 and lie in (0, 1), mapping directly to implied probabilities.

## Why It Matters

LMSR solves the liquidity bootstrapping problem in prediction markets — it always quotes a price, even with zero counterparties. The market maker's maximum loss is bounded at `b × ln(n)`, making risk quantifiable upfront. Understanding LMSR is essential for trading on AMM-based prediction markets (Azuro) and for modeling the cost of information acquisition in CLOB-based markets (Polymarket, Kalshi).

## Key Equations

- Cost function: `C(q) = b × ln(Σ_i e^{q_i/b})`
- Price for outcome i: `p_i = e^{q_i/b} / Σ_j e^{q_j/b}` (softmax)
- Max loss: `b × ln(n)` where n = number of outcomes
- `b` = liquidity parameter (larger b = deeper market, higher max loss)

## Resources

- Robin Hanson, "Logarithmic Market Scoring Rules for Modular Combinatorial Information Aggregation" (2003)
- Polymarket and Kalshi documentation for CLOB alternatives

## Connections

- Used in prediction market AMMs alongside [[AMM]] mechanisms like [[Constant Product Formula]]
- Prices are implied probabilities — connects to [[Conditional Probability]] and [[Bayes' Theorem]]
- Bounded loss connects to [[Position Sizing]] and risk management
- The softmax function appears in ML classifiers — same mathematical structure
