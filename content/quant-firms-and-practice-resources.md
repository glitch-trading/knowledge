---
title: "Quant Firms & Practice Resources"
type: index
tags:
  - MOC
  - resources
  - interview-prep
---

For interview prep, application targets, and skill-building outside the structured [[level-1-fundamentals|roadmap]].

## Quant Firms

Where MIT-pipeline quants typically apply, grouped by what they actually hire for. Role notes are abbreviated — every firm hires SWE in some form.

### Prop Trading & Market Making

| Firm | Roles | Notes |
|------|-------|-------|
| **Jane Street** | Quant Trading, QR, SWE | Heavy on probability brainteasers, expected value, conditional probability, iterative market-making sims. |
| **Citadel** | Trading (Global Fixed Income, etc.), QR, SWE | Brainteasers + applied finance. |
| **Citadel Securities** | Systematic Trading (more CS), Semi-Systematic Trading (more math), Fundamental Analyst | Mix of CS and math depending on track. |
| **Hudson River Trading** | Algo Developer, SWE | CS- and probability-heavy. Joint-distribution geometry, LeetCode-style coding rounds. |
| **Two Sigma** | QR, SWE | Data-science case studies (housing, opera-house pricing, CitiBikes); rarely asks brainteasers. |
| **D. E. Shaw** | Prop Trading, Quant Analyst, SWE / Quant Developer | Mixed style. |
| **Jump Trading** | Trading, SWE | Latency-sensitive HFT. |
| **SIG (Susquehanna)** | Trader, QR | Options/vol-heavy. Teaches directly from Natenberg. |
| **Optiver** | Trader, QR | Options market making. Fast mental math; teaches directly from [[option-volatility-and-pricing-sheldon-natenberg|Option Volatility and Pricing — Sheldon Natenberg]]. |
| **Akuna Capital** | Options trading, QR | Probability + options + light SWE. |
| **DRW** | Multi-strategy prop | Mixed. |
| **IMC Trading** | Options market making | Vol-focused. |
| **Five Rings** | Trader, QR | Combinatorial brainteasers, indicator-variable tricks, Kelly sizing. |
| **Virtu Financial** | Multi-asset MM/HFT | Probability + algorithm design. |
| **Tower Research** | HFT | Multi-strategy. |
| **Flow Traders** | ETF market making | Vol + microstructure. |
| **Belvedere / Group One / Old Mission / Wolverine / TransMarket** | Options MM, prop | Mostly Chicago-based options shops. |

### Hedge Funds & Asset Managers

| Firm | Roles | Notes |
|------|-------|-------|
| **Bridgewater** | Investment Associate, research | Macro + systematic. Less math-heavy than HFT firms; more economic reasoning. |
| **AQR** | QR, research | Factor investing. |
| **Point72 / Cubist** | QR | Multi-strategy. |
| **QuantCo** | Quant consulting | Data-science-heavy case studies (e.g. dynamic pricing). |
| **Seven Eight Capital** | Prop | — |

### Sell-Side / Bank

| Firm | Roles | Notes |
|------|-------|-------|
| **J.P. Morgan** | QR Extern/Intern | MIT-focused early-career programs. |

## Practice & Drills

- **[QuantGuide.io](https://quantguide.io)** — LeetCode for quants. The most quant-specific drill site.
- **[Brainstellar](https://brainstellar.com)** — Probability and logic puzzles.
- **[CMU Puzzle Toad](https://www.cs.cmu.edu/puzzle/)** — Long-running CMU puzzle archive; classic source for the harder Jane Street-style problems.
- **[LeetCode](https://leetcode.com)** — Required for HRT, Two Sigma, Akuna, Belvedere; useful for any quant SWE round.
- **[Kaggle](https://kaggle.com)** — Hands-on data-science problems; the easiest way to get fluent in numpy / pandas / scipy.

## Question Banks

- **MIT Quant Bible** (MIT Sloan Business Club, free PDF) — Probability, stats, regression, market making, plus a firm-by-firm question bank (Jane Street, Citadel, HRT, Two Sigma, Optiver, Akuna, Virtu, Five Rings, SIG). Referenced throughout the roadmap.
- **Zhou** — *A Practical Guide to Quantitative Finance Interviews* (the "Green Book"). 200+ problems with full solutions.
- **Crack** — *Heard on the Street*. 70+ math brainteasers — the classic.
- **Joshi** — *Quant Job Interview Questions and Answers*. Broader question set.
- **Mosteller** — *Fifty Challenging Problems in Probability with Solutions*. Older, still the bar.
- **McDowell** — *Cracking the Coding Interview*. For quant SWE rounds.
- **Art of Problem Solving** — *Intro to Counting and Probability* and *Intermediate Counting and Probability*. Built for high-school math competitions but the same patterns recur in phone screens.

## Community & Reference

- **[Glassdoor](https://glassdoor.com)** — Search by firm + role; recent interviewees post the actual questions they got. Cross-reference against question banks.
- **[Wall Street Oasis](https://www.wallstreetoasis.com)** — Quant-finance forum; recruiting threads, salary data, banker / trader discussions.
- **r/quant**, **r/quantfinance** — Active subreddits for industry discussion.
- **[MIT OpenCourseWare](https://ocw.mit.edu)** — Free MIT course materials. See [[mit-18-06-linear-algebra|MIT 18.06 — Linear Algebra]] and [[mit-18-s096-topics-in-mathematics-with-applications-in-finance|MIT 18.S096 — Topics in Mathematics with Applications in Finance]].

## MIT Course Track (reference)

The progression most MIT-pipeline quants take. Useful as a self-study syllabus even if you don't attend MIT — every course has free materials somewhere.

**Core**

- 18.600 — Probability and Random Variables
- 18.06 — Linear Algebra ([[mit-18-06-linear-algebra|MIT 18.06 — Linear Algebra]])
- 14.32 — Econometrics
- 6.042 — Discrete Math
- 6.006 / 6.046 — Algorithms
- 6.034 / 6.036 — Machine Learning
- 18.650 — Statistics

**Extra**

- 18.615 — Stochastic Processes (the main field of mathematical finance)
- 6.867 — Graduate-level Machine Learning
- 6.437 / 6.438 — Inference (advanced theory behind stats / ML)
- 18.211 — Combinatorics (advanced)

## Books

See [[essential-bookshelf|Essential Bookshelf]] for the curated roadmap reading list. Beyond what's there, the MIT Quant Bible specifically recommends:

- *Thinking Fast and Slow* by Daniel Kahneman — trader psychology and behavioral economics
- [[options-futures-and-other-derivatives-john-hull|Options, Futures, and Other Derivatives — John Hull]] — standard derivatives reference
- [[option-volatility-and-pricing-sheldon-natenberg|Option Volatility and Pricing — Sheldon Natenberg]] — the options interview text for Optiver / SIG
