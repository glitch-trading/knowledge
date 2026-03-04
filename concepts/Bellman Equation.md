---
type: concept
title: "Bellman Equation"
tags:
  - concept
  - optimization
  - control-theory
level: 2
prerequisites:
  - "[[Dynamic Programming]]"
  - "[[Markov Property]]"
---

# Bellman Equation

## What It Is
The Bellman equation is the fundamental recursive equation of dynamic programming. It expresses the value of being in a state as the best immediate reward you can get plus the (discounted) value of the state you transition to. It encodes the insight that optimal decisions can be made one step at a time.

The equation is a *fixed-point* condition: the value function $V$ is the unique function satisfying this recursive relationship. Solving the Bellman equation means finding $V$ and the associated optimal policy.

## Why It Matters
The Bellman equation is the discrete-time foundation for:
- **Reinforcement learning**: Q-learning, SARSA, and policy gradient methods all aim to approximately solve Bellman equations
- **Optimal trading in discrete time**: If you model trading decisions at discrete intervals, the optimal strategy satisfies a Bellman equation
- **Understanding the HJB equation**: The [[HJB Equation]] is the continuous-time limit of the Bellman equation. Understanding the discrete version first makes the continuous version intuitive — the "max over actions" and "expected future value" structure carry over directly

## Key Equations

**Deterministic case**:

$$V(s) = \max_a \left[ R(s, a) + \gamma \, V(s') \right]$$

**Stochastic case** (with transition probabilities):

$$V(s) = \max_a \left[ R(s, a) + \gamma \sum_{s'} P(s' \mid s, a) \, V(s') \right]$$

Where:
- $V(s)$ = value of state $s$ under optimal policy
- $R(s, a)$ = immediate reward for action $a$ in state $s$
- $\gamma$ = discount factor ($0 < \gamma \leq 1$)
- $P(s' \mid s, a)$ = probability of transitioning to $s'$

## Resources
- Bellman, *Dynamic Programming* (1957)
- Sutton & Barto, *Reinforcement Learning: An Introduction*, Chapter 3

## Connections
- [[Dynamic Programming]] — the Bellman equation is the core equation of dynamic programming
- [[HJB Equation]] — the continuous-time generalization of the Bellman equation
