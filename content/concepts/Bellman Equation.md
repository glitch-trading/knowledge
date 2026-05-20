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

## Value Iteration in Code

Value iteration repeatedly applies the Bellman operator until $V$ stops changing — the fixed-point view in action. Toy MDP with $n$ states, $m$ actions, reward tensor $R[s, a]$ and transition tensor $P[s, a, s']$:

```python
import numpy as np

def value_iteration(P: np.ndarray, R: np.ndarray, gamma: float = 0.95,
                    tol: float = 1e-8, max_iter: int = 10_000) -> tuple[np.ndarray, np.ndarray]:
    n_states, n_actions = R.shape
    V = np.zeros(n_states)
    for _ in range(max_iter):
        Q = R + gamma * np.einsum("sat,t->sa", P, V)  # one-step lookahead
        V_new = Q.max(axis=1)
        if np.max(np.abs(V_new - V)) < tol:
            V = V_new
            break
        V = V_new
    policy = Q.argmax(axis=1)
    return V, policy
```

Each iteration is exactly the Bellman update: compute $Q(s, a) = R(s, a) + \gamma \sum_{s'} P(s' \mid s, a) V(s')$, then take the max over $a$. Convergence is geometric at rate $\gamma$ because the operator is a $\gamma$-contraction in the sup-norm — that contraction is why a unique fixed point exists.

For continuous state/action spaces, this same loop becomes the [[HJB Equation]] in the $\Delta t \to 0$ limit, with the `max` replaced by a `sup` over a control set.

## Resources
- Bellman, *Dynamic Programming* (1957)
- Sutton & Barto, *Reinforcement Learning: An Introduction*, Chapter 3

## Connections
- [[Dynamic Programming]] — the Bellman equation is the core equation of dynamic programming
- [[HJB Equation]] — the continuous-time generalization of the Bellman equation
