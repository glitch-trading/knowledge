---
type: book
title: "Introduction to Probability Models"
author: Sheldon Ross
status: unread
tags:
  - book
  - probability
level: 1-2
topics:
  - "[[Poisson Process]]"
  - "[[Brownian Motion]]"
  - "[[Markov Property]]"
---

**Probability and stochastic processes. Read for understanding, not for solving every exercise.**

## Reading Plan
- **Chapter 5:** [[Poisson Process]] (essential for [[Avellaneda-Stoikov]])
- **Chapter 10:** [[Brownian Motion]] (conceptual foundation)

## Key Takeaways

- **Poisson processes model event arrivals.** Orders arriving at an exchange, liquidations triggering on a lending protocol, trades hitting a pool — all modeled as Poisson processes with intensity λ. The [[Avellaneda-Stoikov]] paper uses `λ(δ) = Ae^(-kδ)` for order arrival rates as a function of spread.
- **Exponential inter-arrival times.** If events arrive as a Poisson process with rate λ, the time between events is Exponential(λ). Memoryless property: the time until the next event doesn't depend on how long you've already waited.
- **Brownian motion is the continuous limit.** A random walk with smaller and smaller steps converges to Brownian motion. This is the foundation for continuous-time price models — `dS = σdW` means price evolves as a continuous random wiggle.
- **Markov property simplifies everything.** If the future depends only on the present state (not the history), the process is Markov. Most financial models assume this — it makes the math tractable via dynamic programming and HJB equations.

