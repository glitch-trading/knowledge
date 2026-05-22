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

The mathematics of change and accumulation. [[derivatives|Derivatives]] measure instantaneous rates of change; [[integrals|Integrals]] measure accumulated quantities. Together they form the foundation for continuous-time finance.

## Why It Matters

Nearly every quantitative model in finance is expressed in continuous time. The [[black-scholes-equation|Black-Scholes]] PDE, the [[hjb-equation|HJB Equation]], and [[ito-calculus|Itô Calculus]] all require fluency with derivatives, partial derivatives, and the [[chain-rule|Chain Rule]]. [[taylor-series|Taylor Series]] expansions approximate nonlinear payoffs — the Greeks are literally Taylor coefficients of option prices.

## Key Equations

- Derivative: `f'(x) = lim_{h→0} [f(x+h) - f(x)] / h`
- Chain rule: `d/dx f(g(x)) = f'(g(x)) · g'(x)`
- Fundamental theorem: `∫_a^b f'(x) dx = f(b) - f(a)`
- Taylor expansion: `f(x+h) ≈ f(x) + f'(x)h + ½f''(x)h²`

## Resources

- [[3blue1brown-essence-of-calculus|3Blue1Brown — Essence of Calculus]] for intuition
- [[khan-academy-calculus|Khan Academy — Calculus]] for drill
- [[khan-academy-algebra-ii-and-precalculus|Khan Academy — Algebra II & Precalculus]] for prerequisite review

## Connections

- Extends into [[ito-calculus|Itô Calculus]] for stochastic settings
- [[derivatives|Derivatives]] and [[integrals|Integrals]] are the core operations
- [[taylor-series|Taylor Series]] used throughout options pricing and the [[avellaneda-stoikov|Avellaneda-Stoikov]] paper
