---
type: concept
title: "Partial Differential Equations"
tags:
  - concept
  - math
level: 2
prerequisites:
  - "[[Calculus]]"
  - "[[Differential Equations]]"
---

# Partial Differential Equations

## What It Is

Equations involving partial derivatives of a function with respect to multiple independent variables. In finance, the variables are typically price (S) and time (t). PDEs describe how a quantity evolves jointly across these dimensions.

## Why It Matters

The two most important equations in quantitative finance are PDEs:

1. **Black-Scholes PDE** — prices options by requiring a delta-hedged portfolio to earn the risk-free rate
2. **[[HJB Equation]]** — solves stochastic optimal control problems, including the [[Avellaneda-Stoikov]] market making model

The [[Feynman-Kac Theorem]] connects PDEs to expected values of stochastic processes, bridging the probabilistic and analytical approaches.

## Key Equations

- Heat equation (financial analogue): `∂u/∂t = ½σ²∂²u/∂S²`
- Black-Scholes PDE: `∂V/∂t + ½σ²S²∂²V/∂S² + rS∂V/∂S - rV = 0`
- HJB general form: `∂u/∂t + sup_a[L^a u + f^a] = 0`

## Resources

- [[Stochastic Calculus for Finance II — Steven Shreve]] chapters 4-6
- [[Options, Futures, and Other Derivatives — John Hull]] for Black-Scholes PDE derivation

## Connections

- Generalizes [[Differential Equations]] to multiple variables
- [[Feynman-Kac Theorem]] links PDEs to stochastic expectations
- [[HJB Equation]] is the PDE of optimal control
- [[Itô Calculus]] produces the SDEs whose expectations satisfy PDEs
