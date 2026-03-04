---
type: concept
title: "Itô Calculus"
tags:
  - concept
  - stochastic-calculus
level: 2
prerequisites:
  - "[[Brownian Motion]]"
  - "[[Calculus]]"
---

# Itô Calculus

## What It Is
Itô calculus is the mathematical framework for doing calculus with stochastic (random) processes, particularly those driven by Brownian Motion. It differs from ordinary calculus in one crucial way: second-order terms do not vanish.

In ordinary calculus, $(dx)^2$ is negligibly small and discarded. In Itô calculus, $(dW)^2 = dt$ — this is not negligible. This single fact is the source of every difference between stochastic and deterministic calculus, including the extra term in [[Itô's Lemma]] and the $\sigma^2/2$ correction in [[Geometric Brownian Motion]].

## Why It Matters
Itô calculus is the language of continuous-time quantitative finance. Every model that involves stochastic differential equations — from Black-Scholes to Avellaneda-Stoikov — relies on Itô calculus. Without it, you cannot:
- Apply the chain rule to functions of stochastic processes ([[Itô's Lemma]])
- Derive the Black-Scholes PDE
- Transform between the HJB equation and expected value formulations ([[Feynman-Kac Theorem]])

## Key Equations

The fundamental Itô calculus rules:

| Product   | Result |
|-----------|--------|
| $dt \cdot dt$   | 0      |
| $dt \cdot dW$   | 0      |
| $dW \cdot dW$   | $dt$   |

These rules come from the fact that Brownian Motion has quadratic variation equal to $t$.

## Resources
- Shreve, *Stochastic Calculus for Finance II*, Chapter 4
- Oksendal, *Stochastic Differential Equations*, Chapter 4

## Connections
- [[Itô's Lemma]] — the chain rule derived from Itô calculus
- [[Brownian Motion]] — the stochastic process that Itô calculus operates on
- [[Stochastic Differential Equations]] — equations written and solved using Itô calculus
