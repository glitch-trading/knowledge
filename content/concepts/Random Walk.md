---
type: concept
title: "Random Walk"
tags:
  - concept
  - probability
  - stochastic-processes
level: 1
prerequisites: []
---

## What It Is

A **random walk** is a stochastic process where an entity takes successive steps in random directions. The simplest version is the **symmetric random walk** on integers:

$$S_n = S_0 + \sum_{i=1}^{n} X_i$$

where each step $X_i = +1$ or $-1$ with equal probability $1/2$.

Key properties:
- **Mean**: $E[S_n] = S_0$ — the expected position stays at the starting point
- **Variance**: $\text{Var}(S_n) = n$ — uncertainty grows linearly with time
- **Standard deviation**: $\sigma_{S_n} = \sqrt{n}$ — the "square root of time" rule
- **Martingale**: $E[S_n \mid S_0, S_1, \ldots, S_{n-1}] = S_{n-1}$ — the best prediction of tomorrow's value is today's value
- **Recurrence** (1D): A symmetric random walk on integers returns to the origin infinitely often (with probability 1), but the expected time to return is infinite

Generalizations:
- **Random walk with drift**: $S_n = S_0 + \mu n + \sum X_i$ — adds a deterministic trend
- **Scaled random walk**: Shrink step size and time step; in the limit, this becomes [[Brownian Motion]]

## Why It Matters

The random walk is the discrete foundation of virtually all financial modeling:

- **Efficient Market Hypothesis (EMH)**: If markets are informationally efficient, prices should follow a random walk (or close to it). Any predictable pattern would be arbitraged away. The random walk hypothesis is the null model that every alpha signal must beat.
- **Testing for alpha**: To determine if a trading strategy has genuine predictive power, you compare its performance against a random walk benchmark. Can your strategy predict better than "tomorrow's price = today's price"?
- **Square root of time**: The $\sqrt{n}$ scaling of volatility is fundamental. Daily vol scales to annual vol by $\sigma_{\text{annual}} = \sigma_{\text{daily}} \sqrt{252}$. Holding period risk grows with the square root of time, not linearly.
- **Path to continuous models**: The random walk is the discrete precursor to Brownian motion. As step size $\to 0$ and number of steps $\to \infty$ (appropriately scaled), the random walk converges to continuous Brownian motion — the foundation of Black-Scholes, Itô calculus, and Avellaneda-Stoikov.
- **Gambler's ruin**: A random walk with absorbing barriers models a trader's capital hitting zero. Even with zero edge, a finite-capital trader facing an infinite-capital market will eventually go bust.

## Key Equations

$$S_n = S_0 + \sum_{i=1}^{n} X_i, \quad X_i \in \{+1, -1\} \text{ with } p = 1/2$$

$$E[S_n] = S_0, \quad \text{Var}(S_n) = n$$

$$\sigma_T = \sigma_1 \sqrt{T} \quad \text{(square root of time rule)}$$

Scaling to Brownian motion: Let $W^{(n)}(t) = \frac{1}{\sqrt{n}} S_{\lfloor nt \rfloor}$. Then $W^{(n)} \xrightarrow{d} W(t)$ as $n \to \infty$ (Donsker's theorem).

## Resources

- *A Random Walk Down Wall Street* by Burton Malkiel — the popular classic
- *Stochastic Calculus for Finance I* by Shreve — random walks as the foundation
- *Probability and Random Processes* by Grimmett & Stirzaker — rigorous treatment

## Connections

- [[Brownian Motion]] — the continuous-time limit of the random walk
- [[Markov Property]] — random walks are Markov: the future depends only on the current position
