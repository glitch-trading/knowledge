---
type: concept
title: "Greeks"
tags:
  - concept
  - derivatives
  - options
  - risk
level: 2
prerequisites:
  - "[[derivatives|Derivatives]]"
  - "[[itos-lemma|Itô's Lemma]]"
  - "[[taylor-series|Taylor Series]]"
---

## What It Is

The **Greeks** are the partial derivatives of an option's price $V(S, t; \sigma, r)$ with respect to the variables it depends on. Each Greek isolates exposure to one risk dimension and is the unit in which option traders quote, hedge, and risk-manage positions.

| Greek | Symbol | Sensitivity to | Order |
|---|---|---|---|
| Delta | $\Delta$ | underlying price $S$ | 1st |
| Gamma | $\Gamma$ | underlying price (second-order) | 2nd |
| Vega | $\mathcal{V}$ | volatility $\sigma$ | 1st |
| Theta | $\Theta$ | time $t$ | 1st |
| Rho | $\rho$ | interest rate $r$ | 1st |

For a vanilla European call under Black-Scholes:

$$\Delta = \frac{\partial V}{\partial S} = N(d_1), \qquad \Gamma = \frac{\partial^2 V}{\partial S^2} = \frac{N'(d_1)}{S\sigma\sqrt{T-t}}$$

$$\mathcal{V} = \frac{\partial V}{\partial \sigma} = S N'(d_1)\sqrt{T-t}, \qquad \Theta = \frac{\partial V}{\partial t}, \qquad \rho = \frac{\partial V}{\partial r}$$

The first-order Taylor expansion of an option's P&L is a sum of Greeks:

$$dV \approx \Delta\, dS + \tfrac{1}{2}\Gamma\, (dS)^2 + \mathcal{V}\, d\sigma + \Theta\, dt$$

This is the working equation every options market-maker uses to estimate P&L from market moves.

## Why It Matters

The Greeks are how options risk is *spoken about*. A trader does not say "I am long 100 calls" — they say "I am long $200{,}000 \Delta$, short $50{,}000 \Gamma$, long $80{,}000 \mathcal{V}$." Position sizing, hedging, and risk limits are all set in Greek units.

- **Delta hedging** turns a directional option position into a (locally) pure volatility position. The hedge that produces the [[black-scholes-equation|Black-Scholes Equation]] derivation is dynamic delta hedging.
- **Gamma** is convexity: when long gamma, your delta gets better as the market moves in your favor and worse against you. Long gamma pays for itself when realized vol > implied vol.
- **Vega** is the position's bet on [[implied-volatility|Implied Volatility]]. Long vega = long IV.
- **Theta** is the price of holding optionality — long-gamma/long-vega positions pay theta to the seller every day.
- **AMM liquidity provision is short gamma.** Providing liquidity on Uniswap v2/v3 is economically a sold straddle — see [[impermanent-loss|Impermanent Loss]].

## Greek Relationships

For European options without dividends, two identities are useful:

**Gamma-vega-theta link** (from the [[black-scholes-equation|Black-Scholes Equation]]):

$$\Theta + \tfrac{1}{2}\sigma^2 S^2 \Gamma + rS\Delta - rV = 0$$

A delta-neutral, gamma-positive book has $\Theta < 0$ — you pay for convexity in time decay.

**Put-call parity Greeks** (from [[put-call-parity|Put-Call Parity]]):

$$\Delta_{\text{call}} - \Delta_{\text{put}} = 1, \qquad \Gamma_{\text{call}} = \Gamma_{\text{put}}, \qquad \mathcal{V}_{\text{call}} = \mathcal{V}_{\text{put}}$$

## Resources

- [[options-futures-and-other-derivatives-john-hull|Options, Futures, and Other Derivatives — John Hull]] — Chapter on the Greeks is the standard reference
- [[option-volatility-and-pricing-sheldon-natenberg|Option Volatility and Pricing — Sheldon Natenberg]] — Trader-facing intuition, less math
- [[dynamic-replication-and-hedging-kolm-and-ritter|Dynamic Replication and Hedging — Kolm & Ritter]]

## Connections

- [[black-scholes-equation|Black-Scholes Equation]] — The PDE the Greeks satisfy as derivatives of its solution
- [[implied-volatility|Implied Volatility]] — Vega is the link between option prices and IV
- [[itos-lemma|Itô's Lemma]] — The Greek expansion above is Itô applied to $V(S, t)$
- [[impermanent-loss|Impermanent Loss]] — LP positions are short-gamma exposures
- [[put-call-parity|Put-Call Parity]] — Greek relations between calls and puts on the same strike
