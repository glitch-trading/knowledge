---
type: book
title: "Introduction to Linear Algebra"
author: Gilbert Strang
status: unread
tags:
  - book
  - linear-algebra
  - math
level: 1-2
topics:
  - "[[Portfolio Optimization]]"
  - "[[Regression]]"
---

**The definitive linear algebra textbook. Pair with MIT 18.06 lectures.**

## Why Read This

Linear algebra is the machinery behind portfolio optimization, PCA, covariance estimation, and every ML model. Strang's book builds intuition through geometric reasoning — you'll understand *why* eigenvalues matter, not just how to compute them. The problems are excellent and directly applicable to quantitative finance.

The covariance matrix Σ encodes all pairwise asset relationships. Portfolio variance is a quadratic form: `w^T Σ w`. The first few eigenvectors of stock returns explain most of the variance — this is the basis of factor investing and dimensionality reduction.

## Key Takeaways

- **Think in transformations, not numbers.** Matrices are linear transformations. Eigenvalues tell you how much a transformation stretches along each eigenvector.
- **Eigenvalue decomposition.** Diagonalize covariance matrices to find principal components — the dominant risk factors in a portfolio.
- **Quadratic forms.** Portfolio variance `w^T Σ w` is a quadratic form. Positive definiteness of Σ guarantees a unique minimum-variance portfolio.
- **SVD.** Singular value decomposition generalizes eigendecomposition and is the backbone of PCA, regression, and low-rank approximations.


## Connections

- [[MIT 18.06 — Linear Algebra]] — Companion lectures
- [[Portfolio Optimization]] — Mean-variance optimization uses Σ
- [[Level 1 — Fundamentals]] — Core mathematical foundation
