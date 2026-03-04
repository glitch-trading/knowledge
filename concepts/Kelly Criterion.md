---
type: concept
title: "Kelly Criterion"
tags:
  - concept
  - risk
  - position-sizing
level: 3
prerequisites: []
---

# Kelly Criterion

## What It Is

The Kelly Criterion determines the optimal fraction of your bankroll to bet on a favorable wager. It maximizes the expected logarithmic growth rate of wealth — i.e., the geometric compounding rate over time.

For a simple binary bet with probability $p$ of winning and odds of $b$ to 1:

$$f^* = \frac{bp - q}{b}$$

Where:
- $f^*$ = optimal fraction of bankroll to wager
- $b$ = net odds (win $b$ for every $1$ wagered)
- $p$ = probability of winning
- $q = 1 - p$ = probability of losing

**For even-money bets** ($b = 1$): $f^* = 2p - 1$. You need $p > 0.5$ (an edge) for a positive Kelly fraction.

**For continuous distributions** (e.g., trading): Kelly generalizes to maximizing $E[\ln(1 + f \cdot R)]$ where $R$ is the return distribution of the bet.

## Why It Matters

Kelly is the bridge between "having an edge" and "sizing your bets to exploit it." Without Kelly thinking:

- **Bet too large**: You risk ruin. Even with a positive edge, overbetting eventually blows up your account through variance. Betting 2x Kelly cuts your long-run growth rate to zero.
- **Bet too small**: You leave money on the table. Growth is suboptimal.
- **Full Kelly is aggressive**: In practice, full Kelly is rarely used because it produces large drawdowns (~50% drawdowns are common). Parameter estimation errors also mean your perceived edge may be wrong.

**Fractional Kelly** is the standard practice:
- **Half Kelly** ($f^*/2$): ~75% of the growth rate, dramatically lower drawdowns
- **Quarter Kelly** ($f^*/4$): Even more conservative, suitable when edge estimates are uncertain

The key insight: **the optimal bet size depends on both your edge AND your uncertainty about that edge.** When you're unsure of your edge (you always are), size down.

## Key Equations

**Binary Kelly:**
$$f^* = \frac{bp - q}{b}$$

**Continuous Kelly (Gaussian returns):**
$$f^* = \frac{\mu}{\sigma^2}$$

Where $\mu$ = expected excess return, $\sigma^2$ = variance of returns. This says: bet more when edge is high, less when variance is high.

**Growth rate at Kelly fraction $f$:**
$$g(f) = p \ln(1 + bf) + q \ln(1 - f)$$

Maximum at $f = f^*$.

## Resources

- [[A Man for All Markets — Ed Thorp]] — Thorp popularized Kelly for gambling and investing
- Kelly, J.L. (1956) — "A New Interpretation of Information Rate"
- Thorp, E.O. — "The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market"

## Connections

- [[Position Sizing]] — Kelly is the foundational framework for position sizing
- [[Risk Aversion]] — Fractional Kelly maps to different levels of risk aversion
- [[A Man for All Markets — Ed Thorp]] — Thorp applied Kelly from blackjack to Wall Street
- [[Maximum Drawdown]] — Full Kelly produces ~50% expected max drawdown; fractional Kelly reduces this
