---
type: concept
title: "Itô's Lemma"
tags:
  - concept
  - stochastic-calculus
level: 2
prerequisites:
  - "[[Itô Calculus]]"
  - "[[Chain Rule]]"
---

## What It Is
Itô's Lemma is the chain rule for stochastic calculus. Given a smooth function $f(t, X)$ where $X$ follows a stochastic process, Itô's Lemma tells you how $f$ evolves. The critical difference from the ordinary chain rule is an extra second-order term that arises because $(dW)^2 = dt$.

In ordinary calculus, the chain rule for $f(t, x)$ gives $df = f_t \, dt + f_x \, dx$. In stochastic calculus, you must keep the second-order term: $\frac{1}{2} f_{xx} (dX)^2$. This term survives because the quadratic variation of Brownian Motion is non-zero.

## Why It Matters
Itô's Lemma is used constantly in quantitative finance:
- Deriving the Black-Scholes PDE from GBM
- Solving the GBM SDE to get the explicit stock price formula (and the $\sigma^2/2$ correction)
- Transforming value functions in the HJB equation (as done in Avellaneda-Stoikov Section 3)
- Converting between different representations of stochastic processes

## Key Equations

If $dX = \mu \, dt + \sigma \, dW$ and $f = f(t, X)$, then:

$$df = \frac{\partial f}{\partial t} dt + \frac{\partial f}{\partial X} dX + \frac{1}{2} \frac{\partial^2 f}{\partial X^2} (dX)^2$$

Expanding $(dX)^2 = \sigma^2 \, dt$:

$$df = \left(\frac{\partial f}{\partial t} + \mu \frac{\partial f}{\partial X} + \frac{1}{2} \sigma^2 \frac{\partial^2 f}{\partial X^2}\right) dt + \sigma \frac{\partial f}{\partial X} dW$$

The $\frac{1}{2} \sigma^2 f_{XX}$ term is the Itô correction — absent in ordinary calculus.

## Resources
- Shreve, *Stochastic Calculus for Finance II*, Chapter 4.4
- Oksendal, *Stochastic Differential Equations*, Theorem 4.1.2

## Connections
- [[Itô Calculus]] — the framework from which Itô's Lemma is derived
- [[Chain Rule]] — the ordinary calculus analog that Itô's Lemma generalizes
- [[Stochastic Differential Equations]] — Itô's Lemma is the primary tool for manipulating SDEs
