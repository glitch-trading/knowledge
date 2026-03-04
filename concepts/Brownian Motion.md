---
type: concept
title: "Brownian Motion"
tags:
  - concept
  - stochastic-calculus
  - stochastic-processes
level: 1-2
prerequisites: []
---

# Brownian Motion

## What It Is

**Brownian motion** (or **Wiener process**) $\{W_t, t \ge 0\}$ is the fundamental continuous-time stochastic process. It is defined by:

1. $W_0 = 0$
2. **Independent increments**: For $0 \le s < t \le u < v$, the increments $W_t - W_s$ and $W_v - W_u$ are independent
3. **Normal increments**: $W_t - W_s \sim \mathcal{N}(0, t - s)$
4. **Continuous paths**: $t \mapsto W_t$ is continuous (with probability 1)

Key properties:
- $E[W_t] = 0$ and $\text{Var}(W_t) = t$
- **Self-similarity**: $W_{ct} \overset{d}{=} \sqrt{c}\, W_t$ — Brownian motion at different time scales looks statistically identical (up to rescaling)
- **Nowhere differentiable**: Although the path is continuous, it is so jagged that the derivative $dW/dt$ does not exist at any point. This is why ordinary calculus fails and Itô calculus is needed.
- **Quadratic variation**: $\sum_{i} (W_{t_i} - W_{t_{i-1}})^2 \to t$ as the partition gets finer. In differential notation: $(dW)^2 = dt$. This is the key technical fact that makes Itô calculus different from ordinary calculus.
- **Markov property**: $W_t$ given $W_s$ (for $s < t$) depends only on $W_s$, not on the path before $s$
- **Martingale**: $E[W_t \mid W_s] = W_s$ for $s < t$

## Why It Matters

Brownian motion is the building block of continuous-time finance:

- **Price dynamics**: The standard model for asset prices is $dS = \mu S\,dt + \sigma S\,dW$, where $W$ is a Brownian motion. The $dW$ term provides the randomness. This is [[Geometric Brownian Motion]], and it is the assumption behind Black-Scholes.
- **Avellaneda-Stoikov**: The A-S model assumes the mid-price follows arithmetic Brownian motion: $dS = \sigma\,dW$. The variance parameter $\sigma^2$ directly determines optimal spread width. Higher $\sigma$ means more inventory risk, so the market maker quotes wider.
- **Itô calculus**: Since Brownian motion is nowhere differentiable, you cannot use ordinary calculus on functions of $W_t$. [[Itô Calculus]] provides the tools — Itô's integral, Itô's lemma — all built on properties of Brownian motion.
- **The $(dW)^2 = dt$ rule**: This is the single most important fact in stochastic calculus. In ordinary calculus, $(dx)^2 = 0$ (second-order terms vanish). But Brownian motion is so rough that $(dW)^2 = dt$ does not vanish — it contributes a first-order term. This gives rise to the $\frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial S^2}$ correction in Itô's Lemma and the entire machinery of stochastic calculus.
- **Simulation**: Brownian motion is easy to simulate: $W_{t+\Delta t} = W_t + \sqrt{\Delta t}\, Z$ where $Z \sim \mathcal{N}(0,1)$. This is the basis of Monte Carlo methods in finance.
- **Limitations**: Real asset prices are not Brownian — they exhibit jumps, volatility clustering, and [[Fat Tails]]. Extensions include jump-diffusion processes, stochastic volatility, and fractional Brownian motion.

## Key Equations

$$W_t - W_s \sim \mathcal{N}(0, t-s)$$

$$(dW)^2 = dt, \quad dW \cdot dt = 0, \quad (dt)^2 = 0$$

Arithmetic Brownian motion (used in A-S):

$$dS = \sigma\, dW$$

Geometric Brownian motion (used in Black-Scholes):

$$dS = \mu S\, dt + \sigma S\, dW$$

Simulation:

$$W_{t+\Delta t} = W_t + \sqrt{\Delta t}\, Z, \quad Z \sim \mathcal{N}(0, 1)$$

## Resources

- *Stochastic Calculus for Finance II* by Shreve — rigorous construction and properties
- *Paul Wilmott Introduces Quantitative Finance* — intuitive treatment
- *Probability and Random Processes* by Grimmett & Stirzaker — Chapter 13
- 3Blue1Brown / Mathemaniac: visual introductions to Brownian motion

## Connections

- [[Random Walk]] — Brownian motion is the continuous-time limit of the random walk
- [[Geometric Brownian Motion]] — the multiplicative version used for asset prices
- [[Itô Calculus]] — the calculus framework built on Brownian motion
- [[Avellaneda-Stoikov]] — assumes arithmetic Brownian motion for the mid-price
