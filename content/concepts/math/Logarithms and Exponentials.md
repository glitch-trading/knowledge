---
type: concept
title: "Logarithms and Exponentials"
tags:
  - concept
  - math
level: 1
prerequisites: []
---

## What It Is

The **natural logarithm** $\ln(x)$ is the inverse of the **exponential function** $e^x$, where $e \approx 2.71828$ is Euler's number. Together they form the most fundamental pair of functions in quantitative finance.

Key properties:
- $\ln(ab) = \ln(a) + \ln(b)$ — products become sums
- $\ln(a/b) = \ln(a) - \ln(b)$ — ratios become differences
- $\ln(a^k) = k \ln(a)$ — powers become products
- $e^{a+b} = e^a \cdot e^b$ — sums become products
- $\frac{d}{dx} e^x = e^x$ and $\frac{d}{dx} \ln(x) = \frac{1}{x}$

## Why It Matters

Logarithms and exponentials are ubiquitous in quant trading:

- **Log returns**: The continuously compounded return is $r = \ln(P_t / P_{t-1})$. Log returns are additive across time, which makes them far more convenient than simple returns for multi-period analysis.
- **Compound growth**: Continuous compounding follows $P_t = P_0 e^{rt}$. This is the foundation of discounted cash flow and option pricing.
- **Utility functions**: Logarithmic utility $U(W) = \ln(W)$ is the utility function implied by the Kelly criterion — it penalizes losses more than it rewards gains.
- **Geometric Brownian Motion**: The standard model for asset prices uses $dS = \mu S\,dt + \sigma S\,dW$, whose solution involves $e^{(\mu - \sigma^2/2)t + \sigma W_t}$.
- **Order of magnitude reasoning**: Log scales let you compare assets with vastly different price levels and volatilities on equal footing.

## Key Equations

$$r_{\text{log}} = \ln\!\left(\frac{P_t}{P_{t-1}}\right) = \ln(P_t) - \ln(P_{t-1})$$

$$P_t = P_0 \, e^{r \cdot t}$$

$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2} + \cdots$$

## Resources

- *Mathematics for Finance* by Capinski & Zastawniak — Chapter 1 on compounding
- Khan Academy: Logarithms and Exponentials
- *Paul's Online Math Notes*: Exponential and Logarithm Functions

## Connections

- [[Exponential Utility]] — logarithmic utility as a special case
- [[Taylor Series]] — the exponential function has the cleanest Taylor expansion
- [[Geometric Brownian Motion]] — solution involves exponentials
- [[Normal Distribution]] — the PDF is built on $e^{-x^2}$
