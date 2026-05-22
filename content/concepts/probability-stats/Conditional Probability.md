---
type: concept
title: "Conditional Probability"
tags:
  - concept
  - probability
level: 1
prerequisites: []
---

## What It Is

**Conditional probability** is the probability of event $A$ occurring given that event $B$ has already occurred:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

This formula says: to find the probability of $A$ given $B$, take the probability of both happening and normalize by the probability of $B$.

Key concepts:
- **Independence**: $A$ and $B$ are independent if $P(A \mid B) = P(A)$, equivalently $P(A \cap B) = P(A)P(B)$. Knowing $B$ tells you nothing about $A$.
- **Law of total probability**: $P(A) = \sum_i P(A \mid B_i)P(B_i)$ — decompose $A$ across a partition of the sample space.
- **Conditional expectation**: $E[X \mid Y = y]$ is the expected value of $X$ given that $Y$ takes value $y$. This is a function of $y$.
- **Multiplication rule**: $P(A \cap B) = P(A \mid B) \cdot P(B)$

## Why It Matters

Conditional probability is the foundation of information-driven trading:

- **Updating on market data**: When new information arrives (earnings, order flow, price moves), you update your beliefs. $P(\text{fair price} \mid \text{observed trade})$ is a conditional probability.
- **Adverse selection**: A market maker must estimate $P(\text{informed trader} \mid \text{large order})$. Informed traders adversely select against the market maker's quotes.
- **Filtrations in stochastic calculus**: The conditional expectation $E[X_T \mid \mathcal{F}_t]$ — what you expect the future value to be given all information up to time $t$ — is the basis of martingale theory and no-arbitrage pricing.
- **Signal processing**: Alpha signals are useful precisely when $E[\text{return} \mid \text{signal}] \ne E[\text{return}]$ — the signal provides conditional information that shifts expected returns.
- **Markov property**: The assumption that $P(X_{t+1} \mid X_t, X_{t-1}, \ldots) = P(X_{t+1} \mid X_t)$ — the future depends only on the present — is a conditional probability statement.

## Key Equations

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

$$P(A) = \sum_i P(A \mid B_i) P(B_i) \quad \text{(Law of Total Probability)}$$

$$P(A \cap B) = P(A \mid B) P(B) = P(B \mid A) P(A)$$

## Resources

- *Introduction to Probability* by Bertsekas & Tsitsiklis — Chapter 1
- *All of Statistics* by Larry Wasserman — Chapter 2
- Khan Academy: Conditional probability

## Connections

- [[Bayes' Theorem]] — uses conditional probability to invert the direction of conditioning
- [[Markov Property]] — a conditional independence assumption that simplifies stochastic models
