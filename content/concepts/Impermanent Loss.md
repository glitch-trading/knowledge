---
type: concept
title: "Impermanent Loss"
tags:
  - concept
  - DeFi
  - AMM
  - risk
level: 1-4
prerequisites:
  - "[[Constant Product Formula]]"
  - "[[AMM]]"
---

## What It Is

Impermanent loss (IL) is the difference in value between holding tokens in an AMM liquidity pool versus simply holding them in your wallet. When the price of one token moves relative to the other, the AMM's invariant forces a rebalancing of reserves — effectively selling the appreciating token and buying the depreciating one. This mechanical rebalancing guarantees that an LP always underperforms a buy-and-hold portfolio when prices diverge.

It is called "impermanent" because if prices return to their original ratio, the loss disappears. But in practice, prices rarely return exactly, and the loss is very often permanent.

**The deep insight**: Providing liquidity to a constant product AMM is economically equivalent to **continuously selling straddles** — you are short gamma. You profit when prices stay stable (you collect fees), and you lose when prices move sharply in either direction. LPing is an options-like position, and IL is the premium you pay for being short volatility.

## Why It Matters

- **The core risk of LPing**: Fees earned must exceed IL for LPing to be profitable. This is the fundamental calculation for any LP strategy.
- **Adverse selection framing**: IL is caused by arbitrageurs trading against the pool whenever the AMM price diverges from the true market price. This is [[Adverse Selection]] — the informed traders (arbs) extract value from LPs (uninformed).
- **Short gamma analogy**: Understanding IL as a short volatility position connects DeFi liquidity provision to options theory. High realized volatility → high IL → LPs lose. This framing lets you apply options pricing intuition.
- **Strategy implication**: LP only in pairs where you expect low volatility (stablecoin pairs) or where fee income is high enough to compensate for expected price moves.

## Key Equations

**IL as a function of price change (constant product):**

If the price ratio changes by a factor $r = P_1 / P_0$:

$$IL(r) = \frac{2\sqrt{r}}{1 + r} - 1$$

This is always $\leq 0$ (a loss) for any $r \neq 1$.

**Example values:**
| Price change ($r$) | IL |
|---|---|
| 1.25 (25% up) | -0.6% |
| 1.50 (50% up) | -2.0% |
| 2.00 (2x) | -5.7% |
| 3.00 (3x) | -13.4% |
| 5.00 (5x) | -25.5% |
| 0.50 (50% down) | -5.7% |

**Derivation from first principles (constant product $x \cdot y = k$):**

1. Initial position: reserves $x_0, y_0$, price $P_0 = y_0/x_0$, pool value $V_0 = 2 x_0 P_0 = 2 y_0$
2. Price moves to $P_1 = r \cdot P_0$. Arbitrageurs rebalance: $x_1 = x_0 / \sqrt{r}$, $y_1 = y_0 \sqrt{r}$
3. LP value: $V_{LP} = x_1 P_1 + y_1 = 2 y_0 \sqrt{r}$
4. HODL value: $V_{HODL} = x_0 P_1 + y_0 = y_0(1 + r)$
5. IL: $\frac{V_{LP}}{V_{HODL}} = \frac{2\sqrt{r}}{1+r}$

**IL as short gamma (continuous time):**

$$\frac{dIL}{dt} \approx -\frac{1}{8} \sigma^2 \cdot V \cdot dt$$

Where $\sigma$ is the volatility of the price ratio. IL accumulates proportionally to realized variance — exactly like a short gamma position.

## Resources

- Pintail — "Uniswap: A Good Deal for Liquidity Providers?" (original IL analysis)
- Paradigm — "An Analysis of Uniswap Markets"
- Guillaume Lambert — "Uniswap v3 LP Tokens as Perpetual Put and Call Options"
- Dan Robinson — IL and options equivalence

## Connections

- [[AMM]] — IL is the defining risk of providing liquidity to AMMs
- [[Constant Product Formula]] — IL formula is derived directly from the $x \cdot y = k$ invariant
- [[Liquidity]] — LPs must weigh IL against fee income when deciding to provide liquidity
- [[Adverse Selection]] — IL is the LP's cost of being adversely selected by informed arbitrageurs
