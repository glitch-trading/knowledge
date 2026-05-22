---
type: concept
title: "Information Ratio"
tags:
  - concept
  - metrics
  - performance
level: 3
prerequisites:
  - "[[Sharpe Ratio]]"
---

## What It Is

The Information Ratio (IR) is risk-adjusted return measured **relative to a benchmark**: the active return per unit of active risk (tracking error).

$$\mathrm{IR} = \frac{R_p - R_b}{\sigma_{p-b}}$$

where $R_p$ is portfolio return, $R_b$ is benchmark return, and $\sigma_{p-b}$ is the standard deviation of the active-return series $R_p - R_b$ (the *tracking error*).

**Relation to [[Sharpe Ratio]]:**

- Sharpe uses excess return over the risk-free rate and total volatility — it measures absolute risk-adjusted performance.
- IR uses excess return over a chosen benchmark and tracking error — it measures the *skill* added relative to a passive alternative.
- For an absolute-return strategy with no benchmark, IR collapses to Sharpe.

## Why It Matters

IR is the operational performance metric for active management because it isolates manager / strategy skill from passive market exposure. A long-only equity manager who returns 12% in a year the index returned 10% with a 4% tracking error has $\mathrm{IR} = 0.5$ — useful, but not a star.

**Benchmark scale:**

- $\mathrm{IR} > 0.5$ — competent active manager.
- $\mathrm{IR} > 0.75$ — top quartile, sustainable.
- $\mathrm{IR} > 1.0$ — elite; rare on long horizons after fees.
- $\mathrm{IR} > 2.0$ — almost always a data, sample, or fee artifact.

**Fundamental Law connection.** IR is the left-hand side of the [[Fundamental Law of Active Management]]:

$$\mathrm{IR} \approx \mathrm{IC} \cdot \sqrt{\mathrm{BR}}$$

so improving IR requires either raising per-signal [[Information Coefficient]] or increasing the breadth $\mathrm{BR}$ — the number of *independent* forecasts per period. This decomposition is the entire basis of multi-signal alpha programs: it is mathematically easier to find many weakly-predictive independent signals than one strongly-predictive one.

**Caveats:**

- **Benchmark choice is load-bearing.** A skilled small-cap manager benchmarked against the S&P 500 has inflated IR; the tracking error mostly reflects style drift, not skill.
- **Inherits all Sharpe failure modes** — fat tails, non-normality, multiple-testing inflation. See [[The Deflated Sharpe Ratio — Bailey & López de Prado]].
- **Active vs. residual return distinction matters.** Some references compute IR using residual return from a factor regression rather than raw active return; the two coincide only if benchmark beta is exactly 1.

## Key Equations

**Standard form:**
$$\mathrm{IR} = \frac{R_p - R_b}{\sigma_{p-b}}$$

**Fundamental Law approximation:**
$$\mathrm{IR} \approx \mathrm{IC} \cdot \sqrt{\mathrm{BR}}$$

**Annualization** (same caveats as Sharpe):
$$\mathrm{IR}_{\text{annual}} = \mathrm{IR}_{\text{periodic}} \cdot \sqrt{f}$$

where $f$ is periods per year.

## Resources

- Grinold & Kahn — *Active Portfolio Management* (defines IR and derives the Fundamental Law)
- [[The Deflated Sharpe Ratio — Bailey & López de Prado]] — multiple-testing corrections apply to IR identically

## Connections

- [[Sharpe Ratio]] — IR generalizes Sharpe to benchmark-relative performance
- [[Fundamental Law of Active Management]] — decomposes IR into [[Information Coefficient]] × $\sqrt{\text{breadth}}$
- [[Information Coefficient]] — per-signal input
- [[Alpha Combination]] — the engineering of high-IR systems from many low-IC signals
