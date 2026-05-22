---
type: concept
title: "Markov Chain"
tags:
  - concept
  - probability
  - stochastic-processes
level: 1
prerequisites:
  - "[[markov-property|Markov Property]]"
  - "[[conditional-probability|Conditional Probability]]"
---

## What It Is

A **Markov Chain** is a discrete-time stochastic process over a discrete state space that satisfies the [[markov-property|Markov Property]]: the next state depends only on the current state, not the full history. It is the simplest non-trivial stochastic process and the building block for most regime-aware models in finance.

A chain over $n$ states is fully specified by a **transition matrix** $\mathbf{P}$ where

$$P_{ij} = P(X_{t+1} = j \mid X_t = i), \qquad \sum_{j=1}^{n} P_{ij} = 1 \;\; \forall i$$

Each row is a probability distribution. From any state $i$, the chain must transition somewhere — including back to $i$ itself.

Key concepts:
- **State space**: must be **mutually exclusive and collectively exhaustive**. Every observation belongs to exactly one state, no gaps, no overlaps.
- **Time-homogeneity**: $\mathbf{P}$ is assumed constant over time. Often violated in practice (see [[regime-switching|Regime Switching]]).
- **Irreducible**: every state can be reached from every other state in some number of steps.
- **Aperiodic**: the chain does not get trapped in a cycle of fixed length.
- **Ergodic** (irreducible + aperiodic + positive recurrent): the chain has a unique stationary distribution and converges to it from any starting state.
- **Absorbing state**: $P_{ii} = 1$. Once entered, never left. Useful for modeling defaults, liquidations, terminal events.

## Why It Matters

Markov chains turn vague "what regime are we in?" intuition into a quantitative, testable object:

- **Multi-step forecasts collapse to matrix powers.** The $n$-step transition probability from $i$ to $j$ is the $(i,j)$ entry of $\mathbf{P}^n$ (Chapman-Kolmogorov). All the complexity of paths through state space reduces to repeated matrix multiplication.
- **Long-run behavior has a closed form.** The stationary distribution $\boldsymbol\pi$ solving $\boldsymbol\pi \mathbf{P} = \boldsymbol\pi$ tells you the long-run proportion of time spent in each state. Any strategy that bets heavily on a state the stationary distribution says is rare is taking on tail risk.
- **Estimation is cheap and intuitive.** The MLE is "count transitions, normalize rows" — no optimizer, no gradient.
- **Naive independence violates reality.** A loan-portfolio model that draws each month's state independently will produce loans jumping from *current* to *90+ days late* in one step. The Markov structure forbids that by construction. The same issue applies to market regimes: yesterday's state is not irrelevant to today's.
- **Foundation for richer models.** [[hidden-markov-models|Hidden Markov Models]], regime-switching GARCH, and dynamic-programming control problems (Bellman, HJB) all assume a Markov chain over some latent state.

## Key Equations

**Markov property:**

$$P(X_{t+1} = j \mid X_t = i, X_{t-1}, \ldots, X_0) = P(X_{t+1} = j \mid X_t = i)$$

**Row sums to one:**

$$\sum_{j} P_{ij} = 1$$

**Chapman-Kolmogorov ($n$-step transitions):**

$$P^{(n)}_{ij} = [\mathbf{P}^n]_{ij} = \sum_k P^{(m)}_{ik} P^{(n-m)}_{kj}$$

**Maximum-likelihood estimator** for entry $P_{ij}$ given an observed trajectory:

$$\hat P_{ij} = \frac{N_{ij}}{\sum_k N_{ik}}$$

where $N_{ij}$ counts observed $i \to j$ transitions. This is both the intuitive answer ("how often did we go from $i$ to $j$ out of all times we left $i$?") and the formal MLE under multinomial row likelihoods.

**Stationary distribution** $\boldsymbol\pi$:

$$\boldsymbol\pi \mathbf{P} = \boldsymbol\pi, \qquad \sum_i \pi_i = 1$$

Equivalently, $\boldsymbol\pi$ is the left eigenvector of $\mathbf{P}$ with eigenvalue $1$.

## Estimation in Code

Transition matrix from a sequence of integer state labels:

```python
import numpy as np

def estimate_transition_matrix(states: np.ndarray, n_states: int) -> np.ndarray:
    counts = np.zeros((n_states, n_states))
    for i in range(len(states) - 1):
        counts[states[i], states[i + 1]] += 1
    row_sums = counts.sum(axis=1, keepdims=True)
    return np.divide(counts, row_sums, where=row_sums > 0)
```

The $n$-step forecast is just a matrix power:

```python
P_n = np.linalg.matrix_power(P, n)            # n-step transition matrix
forecast = P_n[current_state]                 # distribution over states after n steps
```

The stationary distribution as a linear-system solve (replace one row of $\mathbf{P}^\top - \mathbf{I}$ with the normalization constraint):

```python
def stationary_distribution(P: np.ndarray) -> np.ndarray:
    n = P.shape[0]
    A = P.T - np.eye(n)
    A[-1] = 1.0                               # replace last equation with sum-to-one
    b = np.zeros(n); b[-1] = 1.0
    return np.linalg.solve(A, b)
```

## Sample-Size Discipline

The MLE is unbiased but noisy for rare transitions. Rule of thumb: every cell of $\mathbf{P}$ should be estimated from **at least 20–30 observed transitions**, or the off-diagonal probabilities will be dominated by sampling noise. If a cell is sparse, options are:

- Merge states (e.g., collapse "30–59 days late" and "60–89 days late" into one bucket)
- Extend the sample history
- Apply a Dirichlet prior (add pseudo-counts) to regularize the estimate

## Resources

- *Introduction to Probability Models* by Sheldon Ross — Ch. 4 on Markov chains
- *Markov Chains and Mixing Times* by Levin, Peres & Wilmer — deeper theory, mixing and convergence
- *Finite Markov Chains and Algorithmic Applications* by Häggström — concise modern intro

## Connections

- [[markov-property|Markov Property]] — the abstract property this concrete object satisfies
- [[regime-switching|Regime Switching]] — Markov chains applied to model market regimes
- [[hidden-markov-models|Hidden Markov Models]] — Markov chain over a *latent* state, observed through noisy emissions
- [[dynamic-programming|Dynamic Programming]] — Bellman recursion assumes a Markov state
- [[random-walk|Random Walk]] — the simplest Markov chain
- [[stationarity|Stationarity]] — related-but-different notion (statistical properties constant over time, vs. distribution of the chain converging)
