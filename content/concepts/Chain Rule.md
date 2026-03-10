---
type: concept
title: "Chain Rule"
tags:
  - concept
  - math
  - calculus
level: 1
prerequisites: []
---

## What It Is

The **chain rule** gives the derivative of a composition of functions. If $y = f(g(x))$, then:

$$\frac{dy}{dx} = f'(g(x)) \cdot g'(x)$$

Or equivalently, if $y = f(u)$ and $u = g(x)$:

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

The **multivariable chain rule** generalizes this. If $f$ depends on $u$ and $v$, which both depend on $t$:

$$\frac{df}{dt} = \frac{\partial f}{\partial u}\frac{du}{dt} + \frac{\partial f}{\partial v}\frac{dv}{dt}$$

## Why It Matters

The chain rule is arguably the single most important differentiation rule in quantitative finance:

- **Itô's Lemma**: The stochastic calculus version of the chain rule. When applying a smooth function $f(S, t)$ to a stochastic process $S$, Itô's Lemma tells you how $f$ evolves — but with an extra $\frac{1}{2}\frac{\partial^2 f}{\partial S^2}(dS)^2$ term that has no deterministic analog. Understanding the ordinary chain rule is a prerequisite for understanding why this correction term appears.
- **Greek computation**: Delta is $\frac{\partial V}{\partial S}$, but if you parameterize the model differently (e.g., in terms of log-price), you need the chain rule to convert between representations.
- **Backpropagation**: In machine learning for trading, backpropagation is just the chain rule applied systematically through a computational graph.
- **Change of variables**: Converting between return definitions (simple vs. log) or between price and log-price requires the chain rule.

## Key Equations

Single variable:

$$\frac{d}{dx} f(g(x)) = f'(g(x)) \cdot g'(x)$$

Multivariable:

$$\frac{df}{dt} = \sum_i \frac{\partial f}{\partial x_i} \frac{dx_i}{dt}$$

Example — derivative of $\ln(S)$ with respect to $S$:

$$\frac{d}{dS} \ln(S) = \frac{1}{S}$$

This simple application of the chain rule is why log returns appear everywhere.

## Resources

- *Calculus* by James Stewart — Section on the Chain Rule
- 3Blue1Brown: Chain rule intuition in *Essence of Calculus*
- *Stochastic Calculus for Finance II* by Shreve — to see the stochastic extension

## Connections

- [[Derivatives]] — the chain rule is the most important derivative rule
- [[Itô's Lemma]] — the stochastic generalization of the chain rule, with a correction term
