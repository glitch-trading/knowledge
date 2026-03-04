---
type: book
title: "Stochastic Calculus for Finance II: Continuous-Time Models"
author: Steven Shreve
status: unread
tags:
  - book
  - stochastic-calculus
level: 2
topics:
  - "[[Brownian Motion]]"
  - "[[Itô Calculus]]"
  - "[[Stochastic Differential Equations]]"
  - "[[Feynman-Kac Theorem]]"
---

# Stochastic Calculus for Finance II — Steven Shreve

**The mathematical backbone. Standard textbook, written for finance people.**

## Why Read This
Provides all the stochastic calculus needed for the [[Avellaneda-Stoikov]] paper and beyond. Chapters 1-4 are essential.

## Reading Plan
- **Chapter 1:** General probability theory
- **Chapter 2:** Information and conditioning
- **Chapter 3:** [[Brownian Motion]]
- **Chapter 4:** [[Itô Calculus]] — the core chapter

## Key Takeaways

- **`(dW)² = dt` is the key fact.** Brownian motion is rough enough that quadratic variation doesn't vanish. This single fact drives the entire theory — Itô's lemma, the drift correction, Black-Scholes, everything.
- **Itô's lemma is the chain rule for stochastic calculus.** For `f(S,t)` where S follows an SDE: `df = f_t dt + f_S dS + ½ f_SS (dS)²`. The extra `½ f_SS` term is what makes stochastic calculus different from ordinary calculus.
- **The drift correction `−σ²/2`.** Apply Itô's lemma to `ln(S)` where S follows GBM → the log return has drift `μ − σ²/2`, not `μ`. This is why geometric mean < arithmetic mean for volatile assets.
- **Martingales and risk-neutral pricing.** Under the risk-neutral measure, discounted asset prices are martingales. This change of measure (Girsanov's theorem) is the theoretical foundation for derivative pricing.
- **Feynman-Kac connects expectations to PDEs.** Expected values of functions of diffusion processes satisfy PDEs. This is why the [[Avellaneda-Stoikov]] optimization (maximize expected utility) becomes an [[HJB Equation]].


## Connections
- Enables reading [[Avellaneda-Stoikov]]
- Supplements with MIT OCW 18.S096 lectures 17-21
