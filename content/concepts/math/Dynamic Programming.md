---
type: concept
title: "Dynamic Programming"
tags:
  - concept
  - optimization
  - control-theory
level: 2
prerequisites:
  - "[[Markov Property]]"
---

## What It Is
Dynamic programming is an optimization technique based on Bellman's *Principle of Optimality*: an optimal policy has the property that, regardless of how you arrived at the current state, the remaining decisions must constitute an optimal policy from that state onward.

This allows you to break a complex multi-period optimization into a sequence of simpler one-period problems, solved backwards from the terminal time. Instead of optimizing over all possible future action sequences, you only need to ask: "Given where I am now, what is the best action for this step?"

## Why It Matters
Dynamic programming is the algorithmic backbone of optimal trading strategies:
- **Market making**: Avellaneda-Stoikov's optimal quoting is a dynamic programming problem — at each instant, the market maker chooses quotes based on current inventory and time remaining
- **Optimal execution**: Almgren-Chriss and similar models use DP to split large orders over time
- **Reinforcement learning**: Modern RL (used in algorithmic trading) is essentially dynamic programming with function approximation
- The [[Bellman Equation]] is the discrete-time DP recursion; the [[HJB Equation]] is its continuous-time limit

## Key Equations

**Principle of Optimality** (Bellman, 1957):

$$V(s_t) = \max_{a_t} \left[ R(s_t, a_t) + \beta \, E[V(s_{t+1}) \mid s_t, a_t] \right]$$

Where:
- $V(s)$ is the value function (optimal future reward from state $s$)
- $a_t$ is the action (control) at time $t$
- $R$ is the immediate reward
- $\beta$ is the discount factor
- The expectation accounts for stochastic transitions

Solved by **backward induction**: start at terminal time $T$, set $V(s_T)$ = terminal reward, then work backwards.

## Resources
- Bellman, *Dynamic Programming* (1957)
- Bertsekas, *Dynamic Programming and Optimal Control*

## Connections
- [[Bellman Equation]] — the formal recursive equation that DP produces
- [[HJB Equation]] — the continuous-time version of the Bellman equation
- [[Markov Property]] — DP requires that the future depends only on the current state, not the history
