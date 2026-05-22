---
type: concept
title: "Principal Component Analysis"
tags:
  - concept
  - linear-algebra
  - dimensionality-reduction
  - factor-models
level: 1
prerequisites: []
---

## What It Is

**Principal Component Analysis (PCA)** finds the orthogonal directions in a dataset that capture the most variance. Given a centered data matrix $X \in \mathbb{R}^{n \times p}$ with rows as observations and columns as features, PCA decomposes the sample covariance matrix

$$\Sigma = \tfrac{1}{n-1} X^\top X$$

via its eigendecomposition $\Sigma = V \Lambda V^\top$, where the columns of $V$ are eigenvectors (principal directions) and $\Lambda$ is the diagonal matrix of eigenvalues sorted descending. The $k$-th **principal component** of an observation $x$ is its projection $x^\top v_k$.

Equivalently, PCA is the SVD of $X$: if $X = U S V^\top$, the right singular vectors $V$ are the principal directions and the singular values $s_i$ relate to eigenvalues by $\lambda_i = s_i^2 / (n-1)$.

## Why It Matters

PCA is the workhorse for extracting structure from high-dimensional financial data. Three uses dominate:

- **Factor discovery.** Apply PCA to a panel of stock or asset returns. The first principal component is almost always "the market" — every asset loads on it positively. PC2-PC5 capture sector / style / regional factors. For 500 stocks, the first 5 components typically explain ~70% of variance — the rest is asset-specific noise. This is the empirical foundation of factor investing, which models like [[CAPM]] and [[Fama-French Factor Model]] then formalize.
- **Covariance regularization.** The sample covariance matrix on 500 stocks needs ~$500 \times 500 / 2 \approx 125{,}000$ pairwise estimates from a few hundred observations — wildly underdetermined. Reconstructing $\Sigma$ from the top-$k$ eigenvectors plus a noise floor is a standard fix and stabilizes [[Portfolio Optimization]].
- **Dimensionality reduction for ML.** Replace 500 correlated price-derived features with 10 orthogonal components before fitting a model. Reduces collinearity, speeds training, often helps generalization.

PCA does **not** know about returns or risk — it only looks at variance. A component with high variance can still be uninformative for forecasting, and a low-variance direction can carry the signal. This is the central trap.

## Key Equations

**Variance explained** by the first $k$ components:

$$\text{ratio}_k = \frac{\sum_{i=1}^{k} \lambda_i}{\sum_{i=1}^{p} \lambda_i}$$

**Reconstruction** from top-$k$ components:

$$\hat X = U_k S_k V_k^\top \quad \text{(rank-}k\text{ approximation, minimizes } \|X - \hat X\|_F\text{)}$$

**Loadings vs. scores.** $V$ (loadings) is fixed structure of the data; $U S$ (scores) is the projection of observations into the new basis.

## Estimation in Code

```python
import numpy as np

def pca(X: np.ndarray, k: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    X_centered = X - X.mean(axis=0)
    U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)
    eigenvalues = S**2 / (X.shape[0] - 1)
    components = Vt[:k].T
    scores = X_centered @ components
    explained = eigenvalues[:k] / eigenvalues.sum()
    return components, scores, explained
```

On daily returns for an S&P 500 panel, the first eigenvalue usually carries 40-60% of variance, and the eigenvector is roughly uniform — the market factor.

## Practical Notes

- **Always center** the data first. Skipping mean-centering puts the first PC through the centroid rather than along the direction of maximum variance.
- **Scale matters.** If features are on different units (returns vs. volumes), standardize first or PCA will be dominated by the highest-variance feature.
- **Eigenvalue noise.** With $n$ observations and $p$ features, eigenvalues of pure-noise correlation matrices follow the Marchenko-Pastur distribution. Components inside the MP bulk are statistical noise; only eigenvalues clearly above the upper edge are real structure.
- **Sign indeterminacy.** Eigenvectors are defined up to a sign. Two PCA runs on the same data can return opposite-signed components — handle this when comparing across runs.

## Resources

- [[Introduction to Linear Algebra — Gilbert Strang]] — Eigendecomposition and SVD
- [[The Elements of Statistical Learning — Hastie, Tibshirani & Friedman]] — Chapter 14 covers PCA, kernel PCA, sparse PCA
- [[Quantitative Risk Management — McNeil, Frey & Embrechts]] — PCA in risk modeling

## Connections

- [[Portfolio Optimization]] — Top-$k$ PCA stabilizes the covariance matrix used in mean-variance
- [[CAPM]] — Single-factor model whose empirical analogue is PC1 of stock returns
- [[Fama-French Factor Model]] — Pre-specified factors that loosely correspond to top PCs in equity returns
- [[Regression]] — Principal component regression replaces collinear predictors with their PCs
- [[Statistical Arbitrage]] — Residuals after removing top PCs are the canonical "alpha" candidates
