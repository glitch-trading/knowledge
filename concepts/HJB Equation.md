---
type: concept
title: "HJB Equation"
tags:
  - concept
  - optimization
  - control-theory
  - PDEs
level: 2
prerequisites:
  - "[[Bellman Equation]]"
  - "[[Stochastic Differential Equations]]"
  - "[[Itô's Lemma]]"
---

# HJB Equation

## What It Is
The Hamilton-Jacobi-Bellman (HJB) equation is the continuous-time analog of the [[Bellman Equation]]. It is a partial differential equation (PDE) that the optimal value function must satisfy. Where the Bellman equation uses discrete "max over actions," the HJB equation uses a supremum over continuous controls and replaces sums with derivatives.

The HJB equation arises when you have a system governed by a [[Stochastic Differential Equations|stochastic differential equation]] and want to find a control policy that maximizes (or minimizes) an expected objective over time.

## Why It Matters
The HJB equation is the mathematical core of Avellaneda-Stoikov's market-making model:
- **Section 3 of Avellaneda-Stoikov** derives the HJB equation for the market maker's value function
- The market maker's state variables are: current time $t$, midprice $s$, cash $x$, and inventory $q$
- The control variables are: bid and ask quote distances ($\delta^a$, $\delta^b$)
- Solving the HJB gives the optimal quoting policy — this is where the [[Reservation Price]] formula comes from
- The [[Feynman-Kac Theorem]] connects the HJB PDE back to the stochastic expected-utility problem

## Key Equations

For a stochastic control problem with state $X$ following $dX = \mu(X, u) \, dt + \sigma(X, u) \, dW$, the HJB equation is:

$$\frac{\partial V}{\partial t} + \sup_u \left[ \mu(X, u) \frac{\partial V}{\partial X} + \frac{1}{2} \sigma^2(X, u) \frac{\partial^2 V}{\partial X^2} + f(X, u) \right] = 0$$

With terminal condition $V(X, T) = g(X)$.

In Avellaneda-Stoikov, this becomes (after the exponential utility substitution and simplification):

$$\frac{\partial u}{\partial t} + \frac{\sigma^2}{2} \frac{\partial^2 u}{\partial s^2} + \max_{\delta^a, \delta^b} [\text{fill rate terms}] = 0$$

## Resources
- Avellaneda-Stoikov paper, Section 3 (derivation of the HJB for market making)
- Fleming & Soner, *Controlled Markov Processes and Viscosity Solutions*
- Bertsekas, *Dynamic Programming and Optimal Control*, Vol. II

## Connections
- [[Bellman Equation]] — the HJB is the continuous-time limit of the Bellman equation
- [[Dynamic Programming]] — HJB is the continuous-time dynamic programming principle
- [[Feynman-Kac Theorem]] — connects the HJB PDE to expected values of stochastic processes
- [[Avellaneda-Stoikov]] — the HJB equation is the core mathematical tool in the paper
