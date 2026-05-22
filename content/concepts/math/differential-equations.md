---
type: concept
title: "Differential Equations"
tags:
  - concept
  - math
level: 1
prerequisites:
  - "[[calculus|Calculus]]"
---

## What It Is

Equations relating a function to its derivatives. Ordinary differential equations (ODEs) involve one independent variable; [[partial-differential-equations|Partial Differential Equations]] involve multiple. The solution is a function (or family of functions) that satisfies the relationship.

## Why It Matters

Financial models are expressed as differential equations. The [[black-scholes-equation|Black-Scholes]] PDE prices options, the [[hjb-equation|HJB Equation]] solves optimal control problems like the [[avellaneda-stoikov|Avellaneda-Stoikov]] market making model, and mean-reverting processes (Ornstein-Uhlenbeck) are solutions to linear SDEs. Understanding ODE structure is prerequisite to [[stochastic-differential-equations|Stochastic Differential Equations]].

## Key Equations

- First-order linear ODE: `dy/dt + p(t)y = q(t)`
- Separation of variables: `dy/g(y) = f(t)dt`
- Ornstein-Uhlenbeck (deterministic part): `dx/dt = θ(μ - x)`

## Resources

- [[khan-academy-calculus|Khan Academy — Calculus]] covers introductory ODEs
- [[stochastic-calculus-for-finance-ii-steven-shreve|Stochastic Calculus for Finance II — Steven Shreve]] for the stochastic extension

## Connections

- Extended by [[stochastic-differential-equations|Stochastic Differential Equations]] (add noise term `σdW`)
- [[partial-differential-equations|Partial Differential Equations]] are the multi-variable generalization
- The [[hjb-equation|HJB Equation]] and [[feynman-kac-theorem|Feynman-Kac Theorem]] connect SDEs back to PDEs
