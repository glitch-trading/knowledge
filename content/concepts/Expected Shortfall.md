---
type: concept
title: "Expected Shortfall"
tags:
  - concept
  - risk
level: 3
prerequisites: []
---

## What It Is

Expected Shortfall (ES), also called Conditional Value at Risk (CVaR), measures the average loss in the worst X% of scenarios. Where [[Value at Risk]] tells you the threshold ("losses won't exceed $1M 95% of the time"), Expected Shortfall tells you what happens when they do ("in the worst 5% of cases, average loss is $2.3M").

Formally, ES at confidence level $\alpha$ is:
$$ES_\alpha = E[L \mid L > VaR_\alpha]$$

The expected loss, conditional on the loss exceeding the VaR threshold.

## Why It Matters

Expected Shortfall fixes the major problems with VaR:

1. **It captures tail risk.** ES looks at the entire tail distribution beyond the VaR threshold, not just the boundary point. This matters enormously for [[Fat Tails|fat-tailed]] distributions where extreme events are far worse than the threshold suggests.
2. **It is subadditive.** $ES(A + B) \leq ES(A) + ES(B)$. Diversification always helps (or at least doesn't hurt), which is the mathematically correct behavior for a risk measure.
3. **It is a coherent risk measure.** ES satisfies all four axioms of coherent risk measures (monotonicity, subadditivity, positive homogeneity, translation invariance). VaR fails subadditivity.
4. **Harder to game.** You can't hide tail risk from ES the way you can from VaR by selling deep OTM options.

**For crypto markets:** ES is far more appropriate than VaR. Crypto returns have heavy tails, meaning the worst outcomes are dramatically worse than Gaussian VaR would suggest. ES forces you to confront what those outcomes actually look like.

## Key Equations

**Continuous case:**
$$ES_\alpha = \frac{1}{1 - \alpha} \int_\alpha^1 VaR_u \, du$$

ES is the average of all VaR levels beyond the confidence threshold.

**For normally distributed returns:**
$$ES_\alpha = \mu + \sigma \cdot \frac{\phi(z_\alpha)}{1 - \alpha}$$

Where $\phi$ is the standard normal PDF and $z_\alpha$ is the corresponding quantile.

**Historical estimate:**
$$\widehat{ES}_\alpha = \frac{1}{|\{i : L_i > VaR_\alpha\}|} \sum_{L_i > VaR_\alpha} L_i$$

Simply the average of all losses exceeding VaR.

## Resources

- [[Quantitative Risk Management — McNeil, Frey & Embrechts]]
- Artzner et al. (1999) — "Coherent Measures of Risk" (foundational paper)

## Connections

- [[Value at Risk]] — The weaker risk measure that ES improves upon
- [[Fat Tails]] — The distributional reality that makes ES essential
