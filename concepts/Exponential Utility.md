---
type: concept
title: "Exponential Utility"
tags:
  - concept
  - optimization
level: 2
prerequisites:
  - "[[Utility Theory]]"
  - "[[Risk Aversion]]"
---

# Exponential Utility

## What It Is
Exponential utility is the utility function $U(x) = -e^{-\gamma x}$, where $\gamma > 0$ is the risk aversion parameter. It belongs to the CARA (Constant Absolute Risk Aversion) family, meaning the degree of risk aversion is the same regardless of wealth level.

Key properties:
- Always negative, approaching 0 from below as wealth increases
- Concave (risk-averse) for $\gamma > 0$
- The Arrow-Pratt risk aversion measure equals $\gamma$ everywhere
- Wealth-independent risk aversion: a billionaire and a pauper would make the same bet

## Why It Matters
Exponential utility is the specific utility function used in [[Avellaneda-Stoikov]], and it is chosen for a precise mathematical reason: **separability**. When you maximize $E[-e^{-\gamma W_T}]$ where wealth depends on both cash and inventory, the CARA property allows the value function to factor into a product of terms depending on different state variables. This makes the HJB equation solvable.

Without CARA utility, the Avellaneda-Stoikov model would not have a closed-form (or near-closed-form) solution. The choice of utility function is not arbitrary — it is what makes the math tractable.

## Key Equations

$$U(x) = -e^{-\gamma x}$$

Properties:
- $U'(x) = \gamma e^{-\gamma x} > 0$ (increasing)
- $U''(x) = -\gamma^2 e^{-\gamma x} < 0$ (concave)
- Arrow-Pratt ARA: $A(x) = -U''/U' = \gamma$

Key identity used in Avellaneda-Stoikov — if $W = X + qS$ (cash plus inventory value):

$$E[-e^{-\gamma W}] = -e^{-\gamma X} \cdot E[e^{-\gamma q S}]$$

This factoring is why CARA utility makes the optimization tractable.

## Resources
- Avellaneda-Stoikov paper, Section 2 (motivation for CARA)
- Pratt, "Risk Aversion in the Small and in the Large" (1964)

## Connections
- [[Utility Theory]] — exponential utility is a specific utility function
- [[Risk Aversion]] — $\gamma$ is the constant absolute risk aversion parameter
- [[Avellaneda-Stoikov]] — uses exponential utility to derive optimal quotes
