---
type: book
title: "Quantitative Risk Management: Concepts, Techniques and Tools"
author: "Alexander McNeil, Rüdiger Frey, Paul Embrechts"
status: unread
tags:
  - book
  - risk
level: 3, 6
topics:
  - "[[Value at Risk]]"
  - "[[Expected Shortfall]]"
  - "[[Fat Tails]]"
---

# Quantitative Risk Management — McNeil, Frey & Embrechts

**Proper risk modeling. Covers EVT, copulas, and tail risk.**

## Reading Plan
- **Chapters 1-4:** Core risk metrics, VaR, ES, correlation
- **Chapter 7:** Extreme value theory

## Key Takeaways

- **VaR is not enough.** Value at Risk tells you "the loss won't exceed X at confidence level Y" — but says nothing about *how bad* it gets beyond that threshold. For fat-tailed assets like crypto, VaR is dangerously misleading.
- **Expected Shortfall (CVaR) is the right metric.** Average loss in the tail, not just the threshold. It's coherent (VaR is not), sub-additive (diversification helps), and captures tail severity.
- **Extreme Value Theory.** Model the tails separately from the bulk of the distribution using EVT (Generalized Pareto Distribution for exceedances). This gives you realistic tail probabilities instead of Gaussian fantasy.
- **Copulas separate marginals from dependence.** Each asset can have its own marginal distribution while the copula models their joint dependence structure. In crises, correlations spike — Gaussian copulas underestimate joint tail risk.
- **Correlation is not dependence.** Two assets can have zero correlation but strong tail dependence. Stress testing must account for the non-linear ways assets move together in extremes.

