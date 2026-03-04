---
type: book
title: "A First Course in Stochastic Calculus"
author: Louis-Pierre Arguin
status: unread
tags:
  - book
  - stochastic-calculus
  - math
level: 2
topics:
  - "[[Brownian Motion]]"
  - "[[Itô Calculus]]"
  - "[[Itô's Lemma]]"
  - "[[Stochastic Differential Equations]]"
---

# A First Course in Stochastic Calculus — Louis-Pierre Arguin

**A gentler alternative to Shreve for learning stochastic calculus.**

## Why Read This

Shreve's "Stochastic Calculus for Finance II" is the standard, but it can be dense for a first encounter. Arguin's book takes a more gradual path to the same destination — Brownian motion, Itô calculus, SDEs, and the connection to PDEs. If Shreve feels like hitting a wall, start here and then revisit Shreve with the foundations in place.

The key insight is the same either way: `(dW_t)² = dt` is the single most important fact in quantitative finance. This is why Itô's lemma has an extra term compared to ordinary calculus, and why the drift correction `−σ²/2` appears in GBM.

## Key Takeaways

- **Brownian motion is continuous but nowhere differentiable.** You can't take derivatives of it in the usual sense — this is why stochastic calculus exists.
- **Itô's lemma.** The chain rule for stochastic processes. The second-order term `½f''(dX)²` doesn't vanish because `(dW)² = dt`.
- **SDEs have solutions.** Geometric Brownian Motion, Ornstein-Uhlenbeck, and other standard processes — understand what it means for a process to "solve" an SDE.
- **Feynman-Kac.** Expected values of functions of stochastic processes satisfy PDEs. This connects probability to differential equations.


## Connections

- [[Stochastic Calculus for Finance II — Steven Shreve]] — More rigorous treatment
- [[Level 2 — Basic Probabilistic Arbitrage]] — Where this fits in the roadmap
- [[Geometric Brownian Motion]] — The core price model
