---
type: concept
title: "VWAP"
tags:
  - concept
  - execution
level: 4
prerequisites:
  - "[[Market Impact]]"
  - "[[TWAP]]"
---

## What It Is

VWAP is both a price benchmark and an execution algorithm. As a benchmark, it is the average price of an asset weighted by volume over a given period. As an algorithm, it aims to execute a large order by matching the market's volume profile — trading more when the market is active and less when it is quiet.

**As a benchmark:**
$$VWAP = \frac{\sum_{i} P_i \times V_i}{\sum_{i} V_i}$$

**As an algorithm:**
- Predict the intraday volume profile (e.g., U-shaped: high at open, low midday, high at close).
- Allocate your order proportionally to expected volume in each time bucket.
- Execute more shares during high-volume periods (where your impact is diluted) and fewer during low-volume periods.

VWAP is the most widely used execution benchmark in institutional trading. "Getting VWAP" means your average fill price matches the market's VWAP — you traded at the average price, no better, no worse.

## Why It Matters

- **Better than TWAP when volume is predictable**: Volume profiles in TradFi are relatively stable and predictable (U-shaped in equities). VWAP exploits this structure to reduce impact compared to equal-slice TWAP.
- **Industry standard benchmark**: Institutional investors judge execution quality against VWAP. Beating VWAP = good execution. Missing VWAP = you impacted the market or timed poorly.
- **Impact minimization**: By concentrating execution in high-volume periods, each slice represents a smaller fraction of market activity, reducing per-slice impact.
- **Crypto considerations**: Volume profiles in crypto are less predictable (24/7 markets, event-driven spikes), making VWAP execution harder to optimize but still valuable for large orders.

## Key Equations

**VWAP benchmark:**
$$VWAP = \frac{\sum_{i=1}^{N} P_i \times V_i}{\sum_{i=1}^{N} V_i}$$

**VWAP execution schedule:**

Target quantity in time bucket $i$:
$$q_i = Q \times \frac{\hat{V}_i}{\sum_j \hat{V}_j}$$

Where $\hat{V}_i$ is the predicted volume in bucket $i$ and $Q$ is total order size.

**Volume prediction (simple historical):**
$$\hat{V}_i = \frac{1}{D} \sum_{d=1}^{D} V_{i,d}$$

Average volume in bucket $i$ over the past $D$ days.

**VWAP tracking error:**
$$\text{Error} = P_{\text{exec}} - VWAP$$

Where $P_{\text{exec}}$ is your volume-weighted average execution price.

## Resources

- Berkowitz, Logue & Noser — "The Total Cost of Transactions on the NYSE"
- Robert Kissell — *The Science of Algorithmic Trading and Portfolio Management*
- Konishi — "Optimal Slice of a VWAP Trade"

## Connections

- [[TWAP]] — TWAP uses equal time slices; VWAP weights by volume profile
- [[Market Impact]] — VWAP minimizes impact by trading proportionally to market activity
- [[Liquidity]] — VWAP execution works best when volume/liquidity patterns are predictable
