---
type: concept
title: "Leg Risk"
tags:
  - concept
  - execution
  - risk
level: 4
prerequisites:
  - "[[Order Book]]"
---

## What It Is

The risk in a multi-leg trade that some legs fill and others do not, converting a structure intended to be market-neutral or arbitrage-free into a directional position. The "leg" terminology comes from spread, basis, and triangular trades, where each component is a *leg* of the overall position.

**Where it shows up:**

- **Cross-venue arbitrage** — buying on venue A, selling on venue B. If venue B's order moves away (or the matching engine rejects) before the second leg fills, you are stuck long the asset on A.
- **[[Triangular Arbitrage]]** — three sequential trades in a cycle. A partial fill on leg 2 leaves you holding the intermediate currency at a possibly-now-worse rate.
- **[[CEX-DEX Arbitrage]]** — the CEX leg fills synchronously; the DEX leg sits in the mempool. Reorgs, gas spikes, or front-runs break the hedge.
- **[[Combinatorial Prediction Markets|Combinatorial prediction-market arbitrage]]** — the arbitrage portfolio touches several conditional markets that cannot be filled atomically.
- **[[Funding Rate Arbitrage]]** — perp leg fills; spot leg slips against you mid-fill.
- **Basis trades / cash-and-carry** — same mechanics on a longer time horizon.

**Atomicity spectrum:**

| Setting | Atomicity | Leg risk |
| --- | --- | --- |
| Single-venue spread order | Native atomic | None |
| Single CLOB, multiple IOC orders | Per-order atomic, portfolio-non-atomic | Low |
| Cross-venue same-asset arb | Non-atomic | Moderate |
| On-chain bundle (flashbots / atomic smart contract) | Atomic-within-bundle | None (within bundle); inclusion risk remains |
| Cross-chain arb | Non-atomic, with confirmation lag | High |
| Multi-leg on non-atomic prediction venue | Non-atomic | High |

## Why It Matters

**Leg risk is what makes a "guaranteed" arbitrage not guaranteed.** Two arbitrages with identical headline edge can have wildly different realized P&L distributions purely because of execution structure. A combinatorial mispricing of $0.05 per dollar means nothing if filling the second leg moves the second market by $0.06.

**Common practical defenses:**

- **Atomic execution where available.** On-chain bundles (flashbots), smart-contract routers, and exchange-native spread/IOC-combo order types eliminate leg risk entirely. Always prefer atomic constructions when they exist.
- **Edge thresholds.** Only trigger when the headline edge clears a buffer covering expected leg-slippage plus fees plus gas (e.g. only trade arbitrages with $> 5\%$ gross gap). Smaller "free money" gaps are typically negative-EV after leg risk.
- **Parallel submission with cancel-on-partial.** Submit all legs simultaneously rather than sequentially; cancel surviving legs if any one fails to fill within a deadline. Reduces but does not eliminate the exposure window.
- **Capacity-aware sizing.** Realized profit is bounded by the **minimum** liquidity across all legs, not the average. Sizing to the weakest leg is the conservative default:
$$\mathrm{Profit}_{\mathrm{realized}} \le \Delta p \cdot \min_{i \in \mathrm{legs}} V_i$$
- **Pre-hedge with the slowest leg.** When one leg has materially higher latency or fill-failure probability (e.g. the on-chain leg in CEX-DEX), submit it first and only fire the fast leg if the slow one confirms.
- **Leg-failure inventory account.** Treat stuck positions as a tracked book with its own risk budget; arbitrage strategies leak P&L through this account constantly and need to be measured there, not just at the level of "successful" arbs.

**Adjacent failure modes that look like leg risk:**

- **"Becoming exit liquidity."** Copy-trading a fast arbitrageur from one block later means buying the price *after* their fill corrected it — you are filling the second leg of *their* trade against them. The mechanic is the same as classic leg risk, but the counterparty is informed.
- **Front-running of the second leg.** On public mempools, the first leg telegraphs the intent; opportunistic traders fill the second leg ahead of you. Private RPC / sealed-bid auctions mitigate.
- **Latency-induced fills.** Even with no failed legs, sequential filling at different timestamps captures different sides of intra-trade price moves — the arbitrage decays before it is fully assembled.

## Key Equations

**Capacity bound (multi-leg):**
$$\mathrm{Profit}_{\mathrm{adj}} = \Delta p \cdot \min_{i \in \mathrm{legs}} V_i$$

**Minimum-edge trigger (single-leg slippage budget $\sigma_i$ per leg):**
$$\mathrm{Trigger} \iff \Delta p > \sum_i \sigma_i + \text{fees} + \text{gas}$$

## Resources

- Harris, *Trading and Exchanges*, Ch. 14 (execution)
- [[Flash Boys 2.0 — Daian et al.]] — leg risk in the on-chain setting

## Connections

- [[Spatial Arbitrage]] / [[Triangular Arbitrage]] / [[CEX-DEX Arbitrage]] / [[Cross-Chain Arbitrage]] — concrete multi-leg strategies where leg risk dominates execution P&L
- [[Combinatorial Prediction Markets]] — many-leg arbitrages on non-atomic venues
- [[Funding Rate Arbitrage]] — multi-leg basis trade
- [[Slippage]] / [[Market Impact]] — the per-leg execution cost that leg risk amplifies
- [[MEV]] / [[Frontrunning]] — adversarial leg-risk amplification on public mempools
- [[Liquidity]] — the constraint that bounds capacity-adjusted profit
