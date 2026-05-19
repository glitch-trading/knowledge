---
type: concept
title: "Implied Volatility"
tags:
  - concept
  - derivatives
  - options
  - volatility
level: 2
prerequisites:
  - "[[Greeks]]"
  - "[[Black-Scholes Equation]]"
  - "[[Normal Distribution]]"
---

## What It Is

**Implied volatility** is the value of $\sigma$ that, when plugged into the [[Black-Scholes Equation|Black-Scholes formula]], reproduces the observed market price of an option. It is not a forecast — it is the market's collective number for how volatile the underlying is expected to be over the option's remaining life, expressed in the units of the model.

Formally, given a market price $V^{\text{mkt}}$ and the Black-Scholes pricing function $V^{\text{BS}}(S, K, T, r, \sigma)$:

$$\sigma^{\text{IV}} = \{\sigma : V^{\text{BS}}(S, K, T, r, \sigma) = V^{\text{mkt}}\}$$

The function $V^{\text{BS}}$ is strictly increasing in $\sigma$ for vanilla options, so the IV is unique and recoverable by 1D root-finding (Newton's method using $\mathcal{V}$ as the derivative).

## Why It Matters

IV is the unit in which the entire options industry communicates and trades.

- **Quotes are in vol, not in price.** A trader saying "26 bid at 27" means 26% IV bid / 27% IV offer, not $26-$27. The price is mechanical once you fix the vol.
- **Vol surface** = IV as a function of strike $K$ and expiry $T$. A liquid option market produces a 2D surface that updates in real time and is the primary input to every derivatives book.
- **Vol smile / skew.** Black-Scholes assumes a flat vol — empirically, IV depends on strike. Equity index options exhibit a **skew** (puts have higher IV than calls — crash insurance is expensive). FX options exhibit a **smile** (both tails priced high). The shape encodes the market's tail-risk view.
- **Trading IV is trading vega.** Going long [[Greeks|vega]] in a delta-neutral way isolates a bet on whether realized future vol will exceed current IV.

## Realized vs. Implied

Realized volatility is the actual standard deviation of returns over a window:

$$\sigma_{\text{realized}} = \sqrt{\frac{252}{n-1} \sum_{t=1}^{n} \left(r_t - \bar r\right)^2}$$

Implied vol is forward-looking from the market's pricing. The difference is the **volatility risk premium**: on average, $\sigma^{\text{IV}} > \sigma_{\text{realized}}$ for equity indices because option sellers demand compensation for crash risk. Selling vol systematically captures this premium but has fat-tailed P&L — see [[Fat Tails]].

## Vol Surface Construction

Steps a trader executes daily:

1. Pull mid prices for every liquid option on the underlying.
2. Strip out put-call parity arbitrage (see [[Put-Call Parity]]) to get a clean implied forward and rate.
3. Invert each price to an IV via Newton's method on $V^{\text{BS}}$.
4. Smooth/interpolate the resulting $(K, T) \to \sigma^{\text{IV}}$ surface, typically in moneyness $\log(K/F)$ rather than raw $K$.
5. Use the surface to price illiquid strikes, compute [[Greeks]], and risk-manage the book.

## Numerical Recovery

```python
import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq

def bs_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def implied_vol(price, S, K, T, r):
    f = lambda s: bs_call(S, K, T, r, s) - price
    return brentq(f, 1e-6, 5.0)
```

Production systems use Newton with vega as the analytical derivative for speed.

## Resources

- [[Options, Futures, and Other Derivatives — John Hull]] — Chapters on volatility and the smile
- [[Option Volatility and Pricing — Sheldon Natenberg]] — The trader-side treatment, surface intuition
- Gatheral, *The Volatility Surface* — Quant-side modeling (SVI, SABR, local vol)

## Connections

- [[Black-Scholes Equation]] — The model IV is inverted from
- [[Greeks]] — Vega is the IV sensitivity; gamma scaled by vol is the "carry" of long-gamma positions
- [[Put-Call Parity]] — Used to clean inputs before fitting a surface
- [[Fat Tails]] — Why the skew exists and why short-vol is a tail-risk strategy
- [[Geometric Brownian Motion]] — The constant-$\sigma$ assumption IV violates in practice
