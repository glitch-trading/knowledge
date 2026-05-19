---
type: concept
title: "Put-Call Parity"
tags:
  - concept
  - derivatives
  - options
  - no-arbitrage
level: 2
prerequisites:
  - "[[Derivatives]]"
---

## What It Is

**Put-call parity** is a model-free no-arbitrage identity linking the prices of a European call and put on the same underlying $S$, strike $K$, and expiry $T$:

$$C - P = S - K e^{-r(T-t)}$$

where $r$ is the risk-free rate and the underlying pays no dividends over $[t, T]$. With continuous dividend yield $q$:

$$C - P = S e^{-q(T-t)} - K e^{-r(T-t)}$$

The relationship is an *identity*, not a model prediction. It holds for any pricing model that admits no arbitrage — Black-Scholes, local vol, stochastic vol, jump-diffusion — because the derivation only uses replication of payoffs at expiry, not any assumed dynamics for $S$.

## Why It Matters

Put-call parity is the most powerful sanity check available to an options trader.

- **Pricing consistency.** Any call-put pair that violates parity (after accounting for borrow, dividends, and discount rates) is an arbitrage opportunity. Real markets quote within a few basis points of parity at all times; persistent gaps appear only when one side is hard to short or has exercise frictions.
- **Synthetic positions.** Parity says any of $\{C, P, S, \text{cash}\}$ can be replicated from the other three: a synthetic long stock is $C - P + K e^{-r(T-t)}$. This is the entire foundation of risk reversals, collars, and box spreads.
- **Surface cleaning.** Before fitting an [[Implied Volatility]] surface, traders use parity to back out a clean implied forward and rate from the call-put pairs at each strike. Calls and puts at the same strike must yield the same IV — if they don't, the inputs are wrong, not the model.
- **Greek relations.** Parity implies $\Delta_C - \Delta_P = e^{-q(T-t)}$, $\Gamma_C = \Gamma_P$, $\mathcal{V}_C = \mathcal{V}_P$. Same vega and same gamma on calls and puts of the same strike is a consequence of parity — see [[Greeks]].

## Derivation (replication argument)

At expiry $T$:

$$C_T - P_T = \max(S_T - K, 0) - \max(K - S_T, 0) = S_T - K$$

Two portfolios with the same terminal value:

| Portfolio | Position at $t$ | Value at $T$ |
|---|---|---|
| A | Long call, short put | $S_T - K$ |
| B | Long stock, short $K$ in cash bonds | $S_T - K$ |

Both portfolios produce $S_T - K$ at $T$ with no path-dependent cash flows. By no-arbitrage they must have the same value at $t$:

$$C_t - P_t = S_t - K e^{-r(T-t)}$$

With dividends, the long-stock leg of portfolio B earns the dividend yield, modifying the formula to the form above.

## American Options

The identity above is for **European** options. For American options on non-dividend-paying stock the call should never be exercised early (so American = European for the call), but the put can be optimal to exercise early. This produces an **inequality**:

$$S - K \leq C - P \leq S - K e^{-r(T-t)}$$

Pricing American options requires numerical methods (binomial trees, finite differences, or LSM-style Monte Carlo).

## Common Real-World Frictions

- **Borrow cost.** When stock is hard to short, the "short stock" leg of the replication costs more than $0$; the parity relation widens by the borrow rate.
- **Discrete dividends.** Replace $e^{-q(T-t)}$ with $\sum_i D_i e^{-r(t_i - t)}$ for known dividend cash flows.
- **Exercise frictions.** Bid-ask, exchange fees, and assignment risk produce a band around parity rather than equality.
- **Interest rates.** For very short-dated options, the discount factor $e^{-r(T-t)} \approx 1$ and parity reduces to $C - P \approx S - K$, which is what trader screens display.

## Resources

- [[Options, Futures, and Other Derivatives — John Hull]] — Standard treatment with worked examples
- [[Option Volatility and Pricing — Sheldon Natenberg]] — Practical use in market-making

## Connections

- [[Black-Scholes Equation]] — Closed-form prices automatically satisfy parity
- [[Greeks]] — $\Gamma_C = \Gamma_P$, $\mathcal{V}_C = \mathcal{V}_P$, $\Delta_C - \Delta_P = e^{-q(T-t)}$ are parity consequences
- [[Implied Volatility]] — Used to clean inputs before fitting an IV surface
- [[Derivatives]] — Parity is the canonical no-arbitrage identity in derivatives
