---
type: course
title: "EE364A: Convex Optimization"
platform: Stanford
url: "https://web.stanford.edu/class/ee364a/"
status: not-started
tags:
  - course
  - optimization
level: 2
topics:
  - "[[Portfolio Optimization]]"
---

**Stephen Boyd's Stanford course. Companion to the textbook. Lectures, slides, and homework all free online.**

## What It Covers

The course tracks [[Convex Optimization — Boyd & Vandenberghe|Boyd & Vandenberghe]] chapter by chapter: convex sets and functions, the standard convex optimization problems (LP, QP, SOCP, SDP), Lagrange duality, unconstrained and constrained algorithms, and applications. The applications half covers exactly the problems quants meet — portfolio optimization, parameter estimation under constraints, robust regression, and signal processing.

Lecture videos, slides, and a full homework set with solutions are available at the course site.

## Key Takeaways

- Most problems quants face are either convex (and therefore solvable globally and reliably) or look convex if rewritten properly. Recognizing the convex form is the skill.
- Lagrange duality is the conceptual machinery behind risk-budgeting, shadow prices, and the dual interpretation of [[Portfolio Optimization|mean-variance optimization]].
- Convex problems do not need fancy solvers — interior-point methods solve them in polynomial time and are the engine behind `cvxpy`, `cvxopt`, and most production portfolio optimizers.
- The course's homework problems double as a quant exercise set: portfolio construction with constraints, risk parity, robust regression with outliers, factor model estimation.

## Connections

- [[Convex Optimization — Boyd & Vandenberghe]] — The textbook this course follows
- [[Portfolio Optimization]] — Most direct application
- [[Level 2 — Basic Probabilistic Arbitrage]] — Optimization section
