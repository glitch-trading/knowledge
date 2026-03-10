---
type: concept
title: "Calculus"
tags:
  - concept
  - math
level: 1
prerequisites: []
---

## What It Is

The mathematics of change and accumulation. [[Derivatives]] measure instantaneous rates of change; [[Integrals]] measure accumulated quantities. Together they form the foundation for continuous-time finance.

## Why It Matters

Nearly every quantitative model in finance is expressed in continuous time. The [[Black-Scholes]] PDE, the [[HJB Equation]], and [[Itô Calculus]] all require fluency with derivatives, partial derivatives, and the [[Chain Rule]]. [[Taylor Series]] expansions approximate nonlinear payoffs — the Greeks are literally Taylor coefficients of option prices.

## Key Equations

- Derivative: `f'(x) = lim_{h→0} [f(x+h) - f(x)] / h`
- Chain rule: `d/dx f(g(x)) = f'(g(x)) · g'(x)`
- Fundamental theorem: `∫_a^b f'(x) dx = f(b) - f(a)`
- Taylor expansion: `f(x+h) ≈ f(x) + f'(x)h + ½f''(x)h²`

## Resources

- [[3Blue1Brown — Essence of Calculus]] for intuition
- [[Khan Academy — Calculus]] for drill
- [[Khan Academy — Algebra II & Precalculus]] for prerequisite review

## Connections

- Extends into [[Itô Calculus]] for stochastic settings
- [[Derivatives]] and [[Integrals]] are the core operations
- [[Taylor Series]] used throughout options pricing and the [[Avellaneda-Stoikov]] paper
