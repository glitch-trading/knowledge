---
type: concept
title: "Feynman-Kac Theorem"
tags:
  - concept
  - stochastic-calculus
  - PDEs
level: 2
prerequisites:
  - "[[Stochastic Differential Equations]]"
  - "[[Partial Differential Equations]]"
  - "[[Itô's Lemma]]"
---

## What It Is
The Feynman-Kac Theorem is the bridge between stochastic processes and partial differential equations (PDEs). It says that the expected value of a function of a stochastic process can be computed by solving a deterministic PDE — and vice versa.

Concretely: if $X$ follows an SDE and you want $u(x,t) = E[g(X_T) \mid X_t = x]$, you don't need to simulate $X$ and average. Instead, $u$ satisfies a PDE that you can solve analytically or numerically.

## Why It Matters
Feynman-Kac is the theoretical engine behind several key results in quant finance:
- **Black-Scholes**: The option price as an expected discounted payoff is equivalent to the Black-Scholes PDE — this equivalence is Feynman-Kac
- **Avellaneda-Stoikov**: The optimal market-making problem is first formulated as maximizing expected utility (a stochastic problem). Via the HJB equation and Feynman-Kac-type reasoning, it becomes a PDE that can be solved. This is why Section 3 of the paper transitions from an expectation to a PDE
- It justifies switching between Monte Carlo simulation and PDE-solving as computational strategies

## Key Equations

If $dX_t = \mu(X_t, t) \, dt + \sigma(X_t, t) \, dW_t$ and $u(x, t) = E\left[e^{-r(T-t)} g(X_T) \mid X_t = x\right]$, then $u$ satisfies:

$$\frac{\partial u}{\partial t} + \mu(x,t) \frac{\partial u}{\partial x} + \frac{1}{2} \sigma^2(x,t) \frac{\partial^2 u}{\partial x^2} - r \, u = 0$$

with terminal condition $u(x, T) = g(x)$.

## Resources
- Shreve, *Stochastic Calculus for Finance II*, Theorem 6.4.1
- Oksendal, *Stochastic Differential Equations*, Theorem 8.2.1

## Connections
- [[Stochastic Differential Equations]] — the stochastic side of the Feynman-Kac correspondence
- [[HJB Equation]] — Feynman-Kac connects the HJB equation's PDE form to the stochastic optimization problem
- [[Avellaneda-Stoikov]] — uses this correspondence to turn expected utility maximization into a solvable PDE
