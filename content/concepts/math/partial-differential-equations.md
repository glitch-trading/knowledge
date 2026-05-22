---
type: concept
title: "Partial Differential Equations"
tags:
  - concept
  - math
level: 2
prerequisites:
  - "[[calculus|Calculus]]"
  - "[[differential-equations|Differential Equations]]"
---

## What It Is

Equations involving partial derivatives of a function with respect to multiple independent variables. In finance, the variables are typically price (S) and time (t). PDEs describe how a quantity evolves jointly across these dimensions.

## Why It Matters

The two most important equations in quantitative finance are PDEs:

1. **Black-Scholes PDE** — prices options by requiring a delta-hedged portfolio to earn the risk-free rate
2. **[[hjb-equation|HJB Equation]]** — solves stochastic optimal control problems, including the [[avellaneda-stoikov|Avellaneda-Stoikov]] market making model

The [[feynman-kac-theorem|Feynman-Kac Theorem]] connects PDEs to expected values of stochastic processes, bridging the probabilistic and analytical approaches.

## Key Equations

- Heat equation (financial analogue): `∂u/∂t = ½σ²∂²u/∂S²`
- Black-Scholes PDE: `∂V/∂t + ½σ²S²∂²V/∂S² + rS∂V/∂S - rV = 0`
- HJB general form: `∂u/∂t + sup_a[L^a u + f^a] = 0`

## Resources

- [[stochastic-calculus-for-finance-ii-steven-shreve|Stochastic Calculus for Finance II — Steven Shreve]] chapters 4-6
- [[options-futures-and-other-derivatives-john-hull|Options, Futures, and Other Derivatives — John Hull]] for Black-Scholes PDE derivation

## Connections

- Generalizes [[differential-equations|Differential Equations]] to multiple variables
- [[feynman-kac-theorem|Feynman-Kac Theorem]] links PDEs to stochastic expectations
- [[hjb-equation|HJB Equation]] is the PDE of optimal control
- [[ito-calculus|Itô Calculus]] produces the SDEs whose expectations satisfy PDEs
