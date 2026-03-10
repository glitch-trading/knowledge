---
type: paper
title: "Power-Law Distributions in Empirical Data"
authors:
  - Aaron Clauset
  - Cosma Rohilla Shalizi
  - M.E.J. Newman
year: 2009
status: unread
tags:
  - paper
  - statistics
  - distributions
topics:
  - "[[Power Law Distribution]]"
  - "[[Fat Tails]]"
---

**How to properly fit and test for power laws. The definitive methodology paper.**

## Summary

Power laws are claimed everywhere — city sizes, earthquake magnitudes, word frequencies, wealth distributions, and critically, financial market variables like order sizes, returns, and trading volumes. But most of these claims are poorly supported. This paper provides a rigorous statistical framework for fitting power-law distributions and testing whether a power law is actually a good fit.

The authors demonstrate that many "power laws" in the literature are artifacts of bad methodology: log-log plots look linear for many distributions, simple least-squares fits on log-log plots are statistically invalid, and researchers rarely test alternative hypotheses.

## Key Results

**Power-law distribution:**
$$p(x) \propto x^{-\alpha}$$

Where $\alpha$ is the scaling exponent (typically $2 < \alpha < 3$ for financial data).

**Proper fitting procedure:**
1. **Estimate $x_{\min}$**: The lower bound above which the power law holds. Use KS-statistic minimization, not eyeballing.
2. **Estimate $\alpha$**: Use maximum likelihood estimation (MLE), not linear regression on log-log plots.
   $$\hat{\alpha} = 1 + n \left[ \sum_{i=1}^{n} \ln \frac{x_i}{x_{\min}} \right]^{-1}$$
3. **Goodness-of-fit test**: Use KS statistic with bootstrapped p-values. A power law is plausible only if $p > 0.1$.
4. **Compare alternatives**: Test power law against lognormal, exponential, stretched exponential, and power law with cutoff using likelihood ratio tests. Many claimed power laws are better fit by lognormals.

**Relevance to finance:**
- Market order sizes follow approximate power laws with $\alpha \approx 1.5$
- Return distributions have power-law tails with $\alpha \approx 3$ (the "inverse cubic law")
- These [[Fat Tails]] mean extreme events are far more likely than Gaussian models predict
- Proper power-law analysis is essential for calibrating risk models like [[Value at Risk]] and [[Expected Shortfall]]

**The paper's warning:** Do not claim a power law without following this methodology. Most claimed power laws in published literature do not survive rigorous testing.

## Resources

- Python `powerlaw` package implements the full methodology
- Companion code available from the authors

## Connections

- [[Power Law Distribution]] — The distribution this paper teaches you to properly identify
- [[Fat Tails]] — Power-law tails are the mechanism behind fat tails in financial data
