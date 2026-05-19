---
type: concept
title: "Fundamental Law of Active Management"
tags:
  - concept
  - signals
  - performance
level: 3
prerequisites:
  - "[[Information Coefficient]]"
  - "[[Information Ratio]]"
---

## What It Is

A result due to Grinold (1989) decomposing the [[Information Ratio]] of an active strategy into the per-forecast skill (the [[Information Coefficient]]) and the number of independent forecasts made per period (breadth):

$$\mathrm{IR} \approx \mathrm{IC} \cdot \sqrt{\mathrm{BR}}$$

- $\mathrm{IR}$ — system-level information ratio
- $\mathrm{IC}$ — average per-forecast information coefficient
- $\mathrm{BR}$ — *breadth*, the number of **independent** forecasts per period

The relationship is approximate; it is exact only under simplifying assumptions (uncorrelated forecasts, mean-variance-optimal weighting, no constraints). Clarke, de Silva & Thorley (2002) refine it with a *transfer coefficient* $\mathrm{TC}$ to account for constraint-induced loss of efficiency:

$$\mathrm{IR} = \mathrm{TC} \cdot \mathrm{IC} \cdot \sqrt{\mathrm{BR}}$$

with $\mathrm{TC} \in [0, 1]$ reflecting how well the implemented portfolio expresses the underlying forecasts (a long-only constraint, turnover cap, or risk budget can each drag $\mathrm{TC}$ well below 1).

## Why It Matters

This is the single most important framing result in active management. It says: **system performance scales with $\sqrt{\mathrm{BR}}$**, not with $\mathrm{BR}$. The arithmetic consequences are stark:

- A single signal with $\mathrm{IC} = 0.10$ run alone gives $\mathrm{IR} = 0.10$.
- Fifty independent signals each with $\mathrm{IC} = 0.05$ give $\mathrm{IR} = 0.05 \cdot \sqrt{50} \approx 0.354$.

The 50-signal portfolio at *half* the per-signal skill produces over three times the system-level IR. This is why institutional alpha desks employ researchers searching for many weak edges rather than the one strong edge. Strong individual edges either don't exist or have been arbitraged to nothing; weak ones survive precisely because they are weak enough to be unattractive in isolation.

**The breadth trap.** $\mathrm{BR}$ in the Fundamental Law is the count of **independent** forecasts, not the count of signals you happen to compute. Signals with overlapping data, shared factor exposures, or common construction logic count as fractional contributions. Running 50 correlated signals can give the effective breadth of 5–10, in which case the realized IR is a fraction of the naive calculation. The fix is structural: see [[Alpha Combination]] for the standard procedure that removes shared variance before weighting.

**Practical implications:**

- **Build redundant data sources.** Two implementations of the same idea on the same data add no breadth.
- **Refresh forecasts.** Breadth counts *independent forecasts per period*. A signal that updates daily contributes more breadth than the same signal updating monthly — provided the daily updates are genuinely new information, not noise around a slow underlying signal.
- **Diversify across horizons.** Short-horizon microstructure signals are nearly independent of long-horizon factor signals; combining horizons multiplies breadth cheaply.
- **Be honest about IC.** Backtest IC inflated by feature search is the canonical input to a Fundamental Law calculation that fails out of sample. Apply multiple-testing corrections, see [[The Deflated Sharpe Ratio — Bailey & López de Prado]].

## Key Equations

**Basic form (Grinold, 1989):**
$$\mathrm{IR} \approx \mathrm{IC} \cdot \sqrt{\mathrm{BR}}$$

**With transfer coefficient (Clarke et al., 2002):**
$$\mathrm{IR} = \mathrm{TC} \cdot \mathrm{IC} \cdot \sqrt{\mathrm{BR}}$$

## Resources

- Grinold, R. (1989) — "The Fundamental Law of Active Management"
- Grinold & Kahn — *Active Portfolio Management*, Ch. 6
- Clarke, de Silva & Thorley (2002) — "Portfolio Constraints and the Fundamental Law of Active Management"

## Connections

- [[Information Coefficient]] — per-signal skill input
- [[Information Ratio]] — system-level output
- [[Alpha Combination]] — the procedure for actually achieving the breadth the law promises
- [[Sharpe Ratio]] — IR is a benchmark-relative cousin
- [[Overfitting]] — the most common reason out-of-sample IR misses the Fundamental Law prediction
