---
type: book
title: "Convex Optimization"
author: Stephen Boyd & Lieven Vandenberghe
status: unread
tags:
  - book
  - optimization
  - math
level: 2
topics:
  - "[[Portfolio Optimization]]"
  - "[[Dynamic Programming]]"
---

**Free Stanford PDF. The standard reference for optimization theory. Focus on chapters 1-5.**

## Why Read This

Optimization is everywhere in quant finance: portfolio construction, execution algorithms, parameter estimation, and risk management. This book establishes when a problem is "easy" (convex) vs "hard" (non-convex), and provides the tools to solve convex problems efficiently. The first 5 chapters cover enough theory to understand and formulate most problems you'll encounter.

The book pairs with `cvxpy` in Python, which lets you solve convex optimization problems with a few lines of code once you understand the formulation.

## Key Takeaways

- **Convex problems have global optima.** If your problem is convex, any local minimum is the global minimum — no need to worry about getting stuck.
- **Formulation matters more than algorithms.** Recognizing that a problem is convex (or can be reformulated as convex) is the hard part. The solver handles the rest.
- **Duality.** Every convex problem has a dual problem. KKT conditions connect the two and give optimality conditions.
- **Common problem types.** LP, QP, SOCP, SDP — know which category your problem falls into.


## Connections

- [[Level 2 — Basic Probabilistic Arbitrage]] — Optimization foundations for control theory
- [[Portfolio Optimization]] — Mean-variance is a QP
- [[HJB Equation]] — Continuous-time optimal control
