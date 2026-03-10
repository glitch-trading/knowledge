---
type: course
title: "MIT 18.06 — Linear Algebra"
platform: MIT OpenCourseWare / YouTube
url: "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
status: not-started
tags:
  - course
  - linear-algebra
  - math
level: 1
topics:
  - "[[Portfolio Optimization]]"
  - "[[Regression]]"
---

**Gilbert Strang. The definitive linear algebra course. Free on MIT OCW and YouTube.**

## What It Covers

Full linear algebra: vector spaces, matrix operations, determinants, eigenvalues and eigenvectors, SVD, positive definiteness. Strang's geometric intuition makes abstract concepts concrete — you'll understand what eigenvalues *mean*, not just how to calculate them.

## Why It Matters for Quant

- Covariance matrices and their eigendecomposition → PCA, factor models
- Quadratic forms → portfolio variance `w^T Σ w`
- SVD → dimensionality reduction, regression
- Positive definiteness → valid covariance matrices, convex optimization

## Key Takeaways

- The four fundamental subspaces (column space, null space, row space, left null space) give the complete picture of what a matrix does
- Positive definite matrices guarantee convexity — critical for portfolio optimization and valid covariance matrices
- SVD is the most important factorization — it works for any matrix and reveals rank, range, and null space simultaneously
- Least squares regression is just projection onto a column space — linear algebra makes statistics geometric

## Companion Text

[[Introduction to Linear Algebra — Gilbert Strang]]

## Connections

- [[3Blue1Brown — Essence of Linear Algebra]] — Watch first for intuition
- [[Level 1 — Fundamentals]] — Linear algebra section
- [[Convex Optimization — Boyd & Vandenberghe]] — Builds on positive definiteness and quadratic forms

