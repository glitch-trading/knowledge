---
type: concept
title: "Utility Theory"
tags:
  - concept
  - optimization
  - economics
level: 2
prerequisites:
  - "[[Probability & Statistics MOC]]"
---

## What It Is
Utility theory provides a framework for making decisions under uncertainty. Instead of maximizing expected wealth directly, a rational agent maximizes expected *utility* — a concave function of wealth that encodes preferences about risk.

The key insight: a concave utility function means the pain of losing $100 is greater than the pleasure of gaining $100. This asymmetry is [[Risk Aversion]], and it is why rational agents don't just maximize expected value — they also care about variance and downside risk.

## Why It Matters
In quant trading, utility theory answers the question: "Why not just maximize expected profit?"
- A market maker who maximizes raw expected profit would quote infinitely tight spreads with no inventory limits — and eventually blow up
- [[Avellaneda-Stoikov]] maximizes expected utility (specifically [[Exponential Utility]]) rather than expected wealth. This naturally produces wider spreads when inventory is large and as time-to-close approaches
- The risk aversion parameter $\gamma$ in utility functions directly controls the aggressiveness of trading strategies
- [[Kelly Criterion]] is another example where utility (log utility) leads to better long-run outcomes than raw expected value maximization

## Key Equations

Expected utility maximization:

$$\max E[U(W)]$$

Where $U$ is a concave, increasing function. Common choices:
- **Exponential (CARA)**: $U(x) = -e^{-\gamma x}$ — used in [[Avellaneda-Stoikov]]
- **Log**: $U(x) = \ln(x)$ — used in [[Kelly Criterion]]
- **Power (CRRA)**: $U(x) = \frac{x^{1-\gamma}}{1-\gamma}$

Concavity ($U'' < 0$) is equivalent to risk aversion.

## Resources
- Von Neumann & Morgenstern, *Theory of Games and Economic Behavior*
- Avellaneda-Stoikov paper, Section 2 (choice of exponential utility)

## Connections
- [[Risk Aversion]] — the behavioral consequence of concave utility
- [[Exponential Utility]] — the specific utility function used in Avellaneda-Stoikov
- [[Reservation Price]] — derived from the indifference condition under utility maximization
