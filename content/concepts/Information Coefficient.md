---
type: concept
title: "Information Coefficient"
tags:
  - concept
  - metrics
  - signals
level: 3
prerequisites:
  - "[[Correlation]]"
  - "[[Regression]]"
---

## What It Is

The Information Coefficient (IC) is the cross-sectional correlation between a signal's forecasted values and the realized values that the signal is trying to predict (returns, residual returns, probabilities, etc.). At time $t$:

$$\mathrm{IC}_t = \mathrm{corr}\!\left(\hat{r}_{i,t},\, r_{i,t+h}\right)$$

where $\hat{r}_{i,t}$ is the signal's forecast for asset $i$ over horizon $h$, and $r_{i,t+h}$ is the realized value. Reported IC is usually the time-series mean of $\mathrm{IC}_t$ over many cross-sections; the standard deviation of $\mathrm{IC}_t$ gives the **IC information ratio** $\mathrm{IC}/\sigma_{\mathrm{IC}}$ (sometimes called the "IC-IR").

**Variants:**

- **Pearson IC** — vanilla linear correlation; sensitive to outliers.
- **Rank IC (Spearman)** — correlation of ranks; the operational default at most desks because it is robust and the natural object when signals drive cross-sectional long/short portfolios.
- **Conditional IC** — IC measured within a regime (volatility bucket, sector, market condition).

## Why It Matters

IC is the **standard unit of signal quality** in systematic equity / multi-asset research. It feeds directly into the [[Fundamental Law of Active Management]]:

$$\mathrm{IR} = \mathrm{IC} \cdot \sqrt{N}$$

so the design problem is to either raise IC, raise the effective breadth $N$, or both.

**Calibration:**

- Real institutional signals on liquid markets typically have IC in the 0.02–0.10 range. Reported numbers above ~0.15 on broad equity universes are almost always overfit, look-ahead-biased, or measured on tiny samples.
- IC's standard error scales like $1/\sqrt{\text{universe size}}$ per period; statistical significance is achieved through long histories and wide cross-sections, not strong single-period IC.

**What IC does not say:**

- **Direction of P&L**: IC measures predictive correlation, not P&L. A signal with positive IC can still lose money after costs, capacity constraints, or sizing errors.
- **Independence**: two signals can each have IC of 0.05 and be nearly perfectly correlated with each other. Their effective contribution to a combined system depends on residual independence — see [[Alpha Combination]].
- **Stationarity**: IC measured on a 10-year backtest is the average across regimes. Real IC walks around, drifts, and decays. Tracking $\mathrm{IC}_t$ over time is often more informative than the long-run average.

## Key Equations

**Time-$t$ cross-sectional IC:**
$$\mathrm{IC}_t = \mathrm{corr}\!\left(\hat{r}_{i,t},\, r_{i,t+h}\right)$$

**Reported IC (time-series average):**
$$\overline{\mathrm{IC}} = \frac{1}{T}\sum_{t=1}^{T}\mathrm{IC}_t$$

**IC information ratio (signal-level Sharpe analogue):**
$$\mathrm{IC\text{-}IR} = \frac{\overline{\mathrm{IC}}}{\sigma(\mathrm{IC}_t)}$$

## Resources

- Grinold & Kahn — *Active Portfolio Management*, Ch. 6 (IC, breadth, fundamental law)
- [[Advances in Financial Machine Learning — López de Prado]] — multiple-testing corrections relevant to reported IC

## Connections

- [[Fundamental Law of Active Management]] — IC is the per-signal input to $\mathrm{IR} = \mathrm{IC} \cdot \sqrt{N}$
- [[Information Ratio]] — system-level outcome that IC and breadth combine to produce
- [[Alpha Combination]] — translating IC across many signals into a single weighted forecast
- [[Correlation]] — IC is a correlation under the hood
- [[Sharpe Ratio]] — IC-IR is the signal-level analogue
- [[Overfitting]] — reported IC inflated by feature search / parameter tuning is the canonical failure mode
