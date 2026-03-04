---
type: concept
title: "Risk Aversion"
tags:
  - concept
  - optimization
  - economics
level: 2
prerequisites:
  - "[[Utility Theory]]"
---

# Risk Aversion

## What It Is
Risk aversion is the preference for a certain outcome over a gamble with the same expected value. A risk-averse agent prefers receiving $50 for sure over a 50/50 chance of $0 or $100, even though both have the same expected value.

Mathematically, risk aversion corresponds to a *concave* utility function ($U'' < 0$). The degree of risk aversion is quantified by the Arrow-Pratt measure, which captures how curved the utility function is.

## Why It Matters
Risk aversion is the single parameter that controls the behavior of optimal market-making strategies:
- In [[Avellaneda-Stoikov]], the parameter $\gamma$ is the risk aversion coefficient. It directly appears in the [[Reservation Price]] formula: $r = s - q\gamma\sigma^2(T-t)$
- **Higher $\gamma$**: wider spreads, faster inventory reduction, lower risk, lower profit
- **Lower $\gamma$**: tighter spreads, willing to hold more inventory, higher risk, higher expected profit
- $\gamma = 0$ would mean risk-neutral (maximize expected wealth, no inventory penalty) — this leads to degenerate strategies
- Choosing $\gamma$ is one of the most important practical decisions when implementing Avellaneda-Stoikov

## Key Equations

**Arrow-Pratt absolute risk aversion (ARA)**:

$$A(x) = -\frac{U''(x)}{U'(x)}$$

For [[Exponential Utility]] $U(x) = -e^{-\gamma x}$:

$$A(x) = \gamma \quad \text{(constant — hence CARA)}$$

This constancy is why exponential utility is mathematically convenient: risk aversion doesn't depend on current wealth level.

## Resources
- Pratt, "Risk Aversion in the Small and in the Large" (1964)
- Avellaneda-Stoikov paper — $\gamma$ appears throughout Sections 3-4

## Connections
- [[Utility Theory]] — risk aversion is a property of the utility function
- [[Exponential Utility]] — the CARA utility function with constant risk aversion $\gamma$
- [[Kelly Criterion]] — log utility implies a specific level of risk aversion
