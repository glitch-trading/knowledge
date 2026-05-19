---
type: concept
title: "Frank-Wolfe Algorithm"
tags:
  - concept
  - optimization
level: 5
prerequisites:
  - "[[Convex Optimization — Boyd & Vandenberghe]]"
---

## What It Is

The Frank-Wolfe algorithm (also "conditional gradient method", 1956) minimizes a smooth convex function $f$ over a compact convex set $C$ using only a **linear-optimization oracle** over $C$. At iteration $k$:

1. Compute gradient $\nabla f(\mathbf{x}_k)$.
2. Solve the **linear** subproblem: $\mathbf{s}_k = \arg\min_{\mathbf{s} \in C} \langle \nabla f(\mathbf{x}_k),\, \mathbf{s} \rangle$.
3. Step: $\mathbf{x}_{k+1} = (1 - \gamma_k)\mathbf{x}_k + \gamma_k \mathbf{s}_k$ with $\gamma_k \in [0,1]$ (e.g. $\gamma_k = 2/(k+2)$ or line search).

**Convergence:** $O(1/k)$ for smooth convex $f$; matches projected gradient descent rates without ever performing a projection. Affine-invariant analyses (Jaggi 2013) give the cleanest modern treatment.

**Why it scales to combinatorial polytopes.** Most convex algorithms require a Euclidean (or Bregman) projection onto $C$ each step — intractable when $C$ has exponentially many facets or vertices. Frank-Wolfe replaces projection with **one linear optimization over $C$**, which is often easy even when $C$ is huge: an LP solver, a shortest-path computation, a min-cut, or a domain-specific oracle. After $k$ iterations the iterate $\mathbf{x}_k$ is a convex combination of at most $k$ vertices — automatically sparse.

**Key variants:**

- **Line-search / fully corrective** Frank-Wolfe — pick the optimal $\gamma_k$ per step; often much faster in practice.
- **Away-step / pairwise Frank-Wolfe** — adds the ability to *reduce* weight on previously selected vertices, achieving linear convergence on polytopes (Lacoste-Julien & Jaggi 2015).
- **Barrier / proximal Frank-Wolfe** — for objectives with log-barrier terms that blow up near the boundary (e.g. LMSR cost $C(\mathbf{q}) = b\log\sum_i e^{q_i/b}$, or any objective with $\log$ singularities at 0 and 1). The barrier variant keeps step sizes stable and prevents iterates from approaching the boundary too fast.
- **Stochastic Frank-Wolfe** — uses noisy gradient estimates; standard in large-scale ML.

## Why It Matters

**The natural optimizer over exponential polytopes.** This is the property that matters in trading and prediction-market applications:

- **[[Combinatorial Prediction Markets|Combinatorial arbitrage]].** The arbitrage-free projection onto the marginal polytope $M$ is a [[Bregman Divergence|Bregman]] (KL) projection — a convex optimization over a polytope with up to $2^n$ vertices. Frank-Wolfe needs only a linear oracle over $M$, which is a single IP / MAP-inference call. Typical implementations converge in 50–150 iterations on real markets even when the nominal outcome space has trillions of joint states.
- **Structured prediction in ML.** Training structural SVMs is an optimization over the marginal polytope of a graphical model. Block-coordinate Frank-Wolfe (Lacoste-Julien et al., 2013) is one of the standard training algorithms.
- **Sparse approximation.** Iterates are convex combinations of few vertices — useful when the solution is meant to be sparse (e.g., portfolio over a large universe with a cardinality preference).
- **Online learning with linear oracles.** Online Frank-Wolfe handles regret minimization over the same combinatorial sets, useful in adaptive market-making.

**Practical pitfalls.**

- **Zig-zagging near the optimum** on polytopes. Vanilla Frank-Wolfe slows to sublinear progress near the solution because the chosen vertex keeps oscillating between corners. Away-step / pairwise variants are the fix.
- **Sensitivity to gradient explosions near boundary.** With log-barrier objectives (LMSR, log-utility), gradients diverge near 0/1. Use the barrier variant or shrink the feasible set with a small interior tolerance.
- **Linear oracle is the bottleneck.** Frank-Wolfe is only as fast as the LP / MAP / shortest-path call inside each iteration. In hard combinatorial settings, the oracle may itself be approximate; convergence guarantees degrade accordingly.

## Key Equations

**Update:**
$$\mathbf{s}_k = \arg\min_{\mathbf{s} \in C} \langle \nabla f(\mathbf{x}_k),\, \mathbf{s} \rangle, \qquad \mathbf{x}_{k+1} = (1 - \gamma_k)\mathbf{x}_k + \gamma_k \mathbf{s}_k$$

**Standard step size:** $\gamma_k = \dfrac{2}{k+2}$.

**Convergence (smooth convex, $L$-Lipschitz gradient):**
$$f(\mathbf{x}_k) - f(\mathbf{x}^*) \le \frac{2 L \, D^2}{k+2}$$

where $D$ is the diameter of $C$.

**Frank-Wolfe duality gap** (computable certificate of suboptimality):
$$g(\mathbf{x}_k) = \langle \nabla f(\mathbf{x}_k),\, \mathbf{x}_k - \mathbf{s}_k \rangle \ge f(\mathbf{x}_k) - f(\mathbf{x}^*)$$

## Resources

- Frank & Wolfe (1956) — original paper
- Jaggi (2013) — "Revisiting Frank-Wolfe: Projection-Free Sparse Convex Optimization"
- Lacoste-Julien & Jaggi (2015) — "On the Global Linear Convergence of Frank-Wolfe Optimization Variants"
- Dudík, Lahaie, Pennock (2012) — applies Frank-Wolfe-style constraint generation to combinatorial market making

## Connections

- [[Combinatorial Prediction Markets]] — primary trading application: KL-projection onto the marginal polytope
- [[Bregman Divergence]] — the natural objective family Frank-Wolfe minimizes in prediction-market settings
- [[Logarithmic Market Scoring Rule]] — log-sum-exp cost requires the barrier variant near boundaries
- [[KL Divergence]] — the LMSR-induced divergence Frank-Wolfe is optimizing in practice
- [[Convex Optimization — Boyd & Vandenberghe]] — background reference
