---
type: concept
title: "Geometric Brownian Motion"
tags:
  - concept
  - stochastic-calculus
level: 2
prerequisites:
  - "[[Brownian Motion]]"
  - "[[Logarithms and Exponentials]]"
---

# Geometric Brownian Motion

## What It Is
Geometric Brownian Motion (GBM) is the standard continuous-time model for stock prices. It describes a process where the *percentage* changes in price are normally distributed, rather than the absolute changes. The process is defined by a drift (expected return) and a volatility (randomness).

The key property: if S follows GBM, then log(S) follows ordinary Brownian Motion with drift. This means S itself is log-normally distributed — always positive, right-skewed, and multiplicative.

## Why It Matters
GBM is the foundational price model in quantitative finance. It underlies Black-Scholes option pricing and is the assumed price process in Avellaneda-Stoikov's market-making model. Understanding GBM is essential for:
- Knowing what assumptions your models bake in (constant volatility, no jumps, independent returns)
- Understanding why log-returns are used instead of arithmetic returns
- Recognizing when real markets deviate from GBM (fat tails, volatility clustering)

## Key Equations

The SDE for GBM:

$$dS = \mu S \, dt + \sigma S \, dW$$

Equivalently, in terms of returns:

$$\frac{dS}{S} = \mu \, dt + \sigma \, dW$$

The explicit solution (via [[Itô's Lemma]]):

$$S(t) = S(0) \exp\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W(t)\right]$$

Note the $-\sigma^2/2$ correction — this is the Itô correction, absent in ordinary calculus.

## Resources
- Shreve, *Stochastic Calculus for Finance II*, Chapter 4
- Avellaneda-Stoikov paper, Section 2 (assumes GBM for midprice)

## Connections
- [[Brownian Motion]] — GBM is the exponential of Brownian Motion with drift
- [[Log-Normal Distribution]] — the distribution of S(t) under GBM
- [[Itô Calculus]] — needed to solve the GBM SDE and get the σ²/2 correction
