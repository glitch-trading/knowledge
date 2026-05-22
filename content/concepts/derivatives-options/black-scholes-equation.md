---
type: concept
title: "Black-Scholes Equation"
tags:
  - concept
  - derivatives
  - options
  - stochastic-calculus
level: 2
prerequisites:
  - "[[itos-lemma|Itô's Lemma]]"
  - "[[geometric-brownian-motion|Geometric Brownian Motion]]"
  - "[[partial-differential-equations|Partial Differential Equations]]"
---

## What It Is

The **Black-Scholes equation** is the PDE that the price $V(S, t)$ of any European-style derivative must satisfy when the underlying $S$ follows [[geometric-brownian-motion|Geometric Brownian Motion]] and continuous delta-hedging is possible:

$$\frac{\partial V}{\partial t} + \tfrac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - r V = 0$$

with the contract's payoff as a terminal condition. For a European call with strike $K$ and expiry $T$, the terminal condition is $V(S, T) = \max(S - K, 0)$, and the PDE has the closed-form solution

$$C(S, t) = S\, N(d_1) - K e^{-r(T-t)} N(d_2)$$

$$d_{1,2} = \frac{\log(S/K) + (r \pm \tfrac{1}{2}\sigma^2)(T-t)}{\sigma\sqrt{T-t}}$$

## Why It Matters

The PDE — not just the call formula — is the central object. Three reasons:

- **The drift $\mu$ of the underlying disappears.** The price depends on volatility $\sigma$ and the risk-free rate $r$, not on the expected return. This is the most counter-intuitive result in derivatives pricing and the heart of risk-neutral valuation.
- **It is universal.** Any derivative whose payoff is a function of $S$ at one terminal time — calls, puts, digitals, power options, barrier options (with adjusted boundary conditions) — satisfies this PDE. Different terminal/boundary conditions give different solutions; the equation does not change.
- **[[greeks|Greeks]] are its derivatives.** The Black-Scholes PDE relates $\Theta$, $\Gamma$, and $\Delta$ algebraically. A delta-neutral, gamma-positive book pays theta — this is the PDE rewritten.

## Derivation (the "no-arbitrage" argument)

Assume $dS = \mu S\, dt + \sigma S\, dW$. Form a portfolio $\Pi = V - \Delta\, S$ where $\Delta = \partial V/\partial S$. Apply [[itos-lemma|Itô's Lemma]] to $V$:

$$dV = \left(\frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \tfrac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right) dt + \sigma S \frac{\partial V}{\partial S}\, dW$$

The portfolio change becomes

$$d\Pi = dV - \Delta\, dS = \left(\frac{\partial V}{\partial t} + \tfrac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right) dt$$

The $dW$ terms cancel — the hedged portfolio is instantaneously riskless. By no-arbitrage it must earn the risk-free rate:

$$d\Pi = r\, \Pi\, dt = r(V - \Delta\, S)\, dt$$

Equating the two expressions gives the Black-Scholes PDE. The drift $\mu$ never appears because it canceled when $dV - \Delta\, dS$ was formed.

## Risk-Neutral Interpretation

The same equation falls out of [[feynman-kac-theorem|Feynman-Kac]] applied to the risk-neutral expectation

$$V(S, t) = e^{-r(T-t)} \mathbb{E}^{\mathbb{Q}}\!\left[ \text{payoff}(S_T) \mid S_t = S \right]$$

where under $\mathbb{Q}$ the drift of $S$ is the risk-free rate $r$, not $\mu$. The PDE and the expectation are two views of the same object — the price.

## Assumptions and When They Break

- Continuous trading — fails at gaps, suspensions, weekends.
- Constant volatility — empirically, $\sigma$ is itself stochastic and depends on strike; this is what produces the [[implied-volatility|Implied Volatility]] smile/skew.
- No transaction costs — every real delta hedge eats P&L; the [[optimal-execution-of-portfolio-transactions-almgren-and-chriss|optimal hedging frequency]] is a separate optimization.
- Lognormal $S$ with no jumps — equity returns have [[fat-tails|Fat Tails]] that GBM does not capture.

Practitioners use Black-Scholes anyway because (a) the *equation* is the language even when the *constant-$\sigma$ assumption* is wrong — you trade vol surface deviations — and (b) richer models (local vol, SABR, jump-diffusion) are built as corrections on top of it.

## Resources

- [[stochastic-calculus-for-finance-ii-steven-shreve|Stochastic Calculus for Finance II — Steven Shreve]] — Chapter on Black-Scholes from scratch
- [[options-futures-and-other-derivatives-john-hull|Options, Futures, and Other Derivatives — John Hull]] — Standard reference with worked examples
- [[ito-calculus|Itô Calculus]] — The machinery the derivation rests on

## Connections

- [[itos-lemma|Itô's Lemma]] — Used in the derivation
- [[greeks|Greeks]] — Partial derivatives of $V$; satisfy the relation $\Theta + \tfrac{1}{2}\sigma^2 S^2 \Gamma + rS\Delta - rV = 0$
- [[implied-volatility|Implied Volatility]] — The $\sigma$ that inverts the closed-form solution to match a market price
- [[geometric-brownian-motion|Geometric Brownian Motion]] — The assumed dynamics for $S$
- [[feynman-kac-theorem|Feynman-Kac Theorem]] — Gives the risk-neutral expectation form
- [[partial-differential-equations|Partial Differential Equations]] — Solution techniques
- [[put-call-parity|Put-Call Parity]] — Holds by no-arbitrage independent of the PDE; cross-checks the closed form
