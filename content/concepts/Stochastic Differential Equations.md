---
type: concept
title: "Stochastic Differential Equations"
tags:
  - concept
  - stochastic-calculus
level: 2
prerequisites:
  - "[[Itô Calculus]]"
  - "[[Brownian Motion]]"
  - "[[Differential Equations]]"
---

## What It Is
A Stochastic Differential Equation (SDE) is a differential equation that includes a random (stochastic) term driven by Brownian Motion. The general form separates into two components: a deterministic *drift* and a random *diffusion*.

Unlike ordinary differential equations, SDEs do not have a single solution trajectory. Instead, each realization of the Brownian Motion produces a different path. Solutions are described in terms of probability distributions rather than single curves.

## Why It Matters
SDEs are the language of continuous-time financial modeling:
- **Price models**: GBM is an SDE ($dS = \mu S \, dt + \sigma S \, dW$)
- **Optimal control**: Avellaneda-Stoikov's wealth process is an SDE, and finding optimal quotes requires solving the associated HJB equation
- **Risk modeling**: Interest rate models (Vasicek, CIR), volatility models (Heston) are all SDEs
- Understanding SDEs is essential for reading any quantitative finance paper that works in continuous time

## Key Equations

General form of an SDE:

$$dX_t = \mu(X_t, t) \, dt + \sigma(X_t, t) \, dW_t$$

Where:
- $\mu(X_t, t)$ is the **drift** coefficient (deterministic tendency)
- $\sigma(X_t, t)$ is the **diffusion** coefficient (randomness magnitude)
- $dW_t$ is the Brownian Motion increment

Common examples:
- **GBM**: $dS = \mu S \, dt + \sigma S \, dW$ (multiplicative noise)
- **Ornstein-Uhlenbeck**: $dX = \theta(\mu - X) \, dt + \sigma \, dW$ (mean-reverting)
- **Arithmetic BM**: $dX = \mu \, dt + \sigma \, dW$ (constant coefficients)

## Resources
- Oksendal, *Stochastic Differential Equations*, Chapters 5-7
- Shreve, *Stochastic Calculus for Finance II*, Chapter 4

## Connections
- [[Itô Calculus]] — the calculus framework for working with SDEs
- [[Brownian Motion]] — the source of randomness in SDEs
- [[HJB Equation]] — the PDE you solve when optimizing a system governed by an SDE
