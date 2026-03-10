---
type: concept
title: "Derivatives"
tags:
  - concept
  - math
  - calculus
level: 1
prerequisites: []
---

## What It Is

The **derivative** of a function $f(x)$ measures its instantaneous rate of change at a point. It is defined as the limit:

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

**Single-variable derivatives** give the slope of the tangent line. **Partial derivatives** extend this to functions of multiple variables — $\frac{\partial f}{\partial x}$ measures the rate of change of $f(x, y, \ldots)$ with respect to $x$ while holding all other variables constant.

Key rules:
- Power rule: $\frac{d}{dx} x^n = n x^{n-1}$
- Product rule: $(fg)' = f'g + fg'$
- Quotient rule: $(f/g)' = (f'g - fg') / g^2$
- Chain rule: $\frac{d}{dx} f(g(x)) = f'(g(x)) \cdot g'(x)$

## Why It Matters

Derivatives are the workhorse of quantitative finance:

- **Sensitivity analysis (Greeks)**: Option delta ($\Delta = \frac{\partial V}{\partial S}$), gamma ($\Gamma = \frac{\partial^2 V}{\partial S^2}$), theta ($\Theta = \frac{\partial V}{\partial t}$), and vega ($\nu = \frac{\partial V}{\partial \sigma}$) are all partial derivatives of option value with respect to different inputs.
- **Optimization**: Finding optimal portfolio weights, bid-ask spreads, or inventory levels requires setting derivatives to zero and solving first-order conditions.
- **PDE models**: The Black-Scholes equation and the Hamilton-Jacobi-Bellman equation are partial differential equations built from derivatives of value functions.
- **Taylor approximations**: Derivatives power the Taylor expansion used to approximate non-linear payoffs and in the derivation of Itô's Lemma.

## Key Equations

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

$$\frac{\partial f}{\partial x_i} = \lim_{h \to 0} \frac{f(x_1, \ldots, x_i + h, \ldots, x_n) - f(x_1, \ldots, x_n)}{h}$$

The gradient (vector of all partial derivatives):

$$\nabla f = \left(\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \ldots, \frac{\partial f}{\partial x_n}\right)$$

## Resources

- *Calculus* by James Stewart — standard reference
- 3Blue1Brown: *Essence of Calculus* (YouTube series)
- MIT OpenCourseWare: 18.01 Single Variable Calculus

## Connections

- [[Chain Rule]] — the most important derivative rule for composed functions
- [[Itô's Lemma]] — the stochastic calculus analog of the chain rule, requires second derivatives
- [[Taylor Series]] — derivatives define the coefficients of polynomial approximations
