---
type: concept
title: "Survivorship Bias"
tags:
  - concept
  - backtesting
  - data-quality
  - risk
level: 3
prerequisites: []
---

## What It Is

**Survivorship bias** is the systematic distortion that arises when a dataset includes only entities that survived to the end of a window and excludes those that disappeared (delisted, went bankrupt, merged, were closed). Statistics computed on the survivors-only sample are not representative of the population that existed at the start of the window.

In quant finance the most common manifestations are:

- **Stock universes** that contain only companies currently listed. Backtesting on today's S&P 500 over the last 20 years implicitly removes every company that went bankrupt or was delisted — exactly the losses your strategy would have taken.
- **Fund databases** that drop funds when they close. Average returns across "surviving" funds overstate the average fund's actual returns by 1-2% per year.
- **Strategy backtests** that quietly filter out periods when an exchange was down, a market halted, or a position couldn't be liquidated.

## Why It Matters

Survivorship bias is one of the two canonical paths to a backtest that looks great and bleeds money live — the other is [[Look-Ahead Bias]]. Unlike look-ahead bias (a logic bug), survivorship bias is a *data sourcing* bug, which makes it harder to spot because the code is correct.

Concrete examples:

- A 2002-launched momentum strategy backtested on the *2024* S&P 500 has implicitly bet against every dot-com that survived and avoided every name that didn't — because the failures are absent from the universe entirely.
- A "long the cheapest decile, short the most expensive decile" value strategy looks great when the cheapest decile excludes the deep-value names that went to zero. Realistic value backtests *must* use point-in-time index constituents and include delisted stocks at their delisting price.
- In crypto, survivorship bias is severe: most tokens that existed in 2018 are no longer traded. A "buy the top 100 by market cap and hold" backtest on today's top 100 is closer to a backtest of "buy the winners" than of a real strategy.

## How To Avoid It

- **Use point-in-time index membership.** CRSP and Compustat provide historical constituent lists. For free data, scrape historical S&P 500 changes from Wikipedia and reconstruct membership.
- **Include delisted securities.** Use a survivorship-bias-free dataset (CRSP includes delisted prices; some free providers explicitly drop them). When a security delists, model its final return as the actual delisting price minus prior close.
- **Test on a fixed-at-start universe.** Rather than today's top-100 by market cap, take the top-100 *as of the backtest start date* and hold that fixed cohort. Compare against the dynamically rebalanced version — the gap is the survivorship effect.
- **Cross-check magnitude.** If a backtest on "today's S&P 500" returns 15% per year and a backtest on point-in-time S&P 500 with delisted names returns 9%, the 6% gap is survivorship bias, not edge.

## Related Distortions

- **Selection bias more broadly** — survivorship is one form of a broader pattern where the observable sample is non-random.
- **Reporting bias in fund databases** — funds self-select into reporting and self-select out before bad months.
- **Backfill bias** — when a fund joins a database, its prior history is often backfilled only if it is favorable.
- **Multiple testing** — running enough strategies guarantees survivor-strategies appear (see [[Hypothesis Testing]] and [[Overfitting]]).

## Resources

- [[Advances in Financial Machine Learning — López de Prado]] — Chapter on backtest pitfalls
- [[Fooled by Randomness — Nassim Taleb]] — The non-technical articulation
- Brown, Goetzmann, Ibbotson & Ross (1992), "Survivorship Bias in Performance Studies" — The original quantification

## Connections

- [[Look-Ahead Bias]] — The other canonical backtest-killer
- [[Overfitting]] — Survivorship-biased data makes overfitting easier and harder to detect
- [[Statistical Arbitrage]] — Cross-sectional strategies are especially sensitive
- [[Hypothesis Testing]] — Tests on survivorship-biased data have inflated false-discovery rates
