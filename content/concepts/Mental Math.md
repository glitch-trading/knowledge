---
type: concept
title: "Mental Math"
tags:
  - concept
  - interview-prep
  - trader-skills
level: 1
prerequisites: []
---

## What It Is

**Mental math** in the quant trader context is the ability to perform arithmetic at speed and under pressure — typically 2-3 digit multiplication, division, percentage calculations, fraction-to-decimal conversion, and simple expected-value evaluations done in seconds without a calculator.

This is a *skill* in the literal sense: separately drilled and separately measured from the math that underpins [[Probability Distributions|probability]] or [[Stochastic Differential Equations|stochastic calculus]]. A strong mathematician can fail trader interviews on the speed-arithmetic round; a weak mathematician with drilled mental math will not pass either.

## Why It Matters

Trader interviews at firms like Optiver, IMC, Jane Street, Five Rings, and SIG include a dedicated speed-arithmetic test. The bar is consistent across firms:

- **Zetamac** at the standard configuration (2-digit × 2-digit multiplication, 2-digit additions, simple divisions): **target 50+ correct in 2 minutes**.
- Some firms run the test live during the interview, others as an online assessment beforehand. Failing it ends the process regardless of how strong the rest of the candidate is.

The reason the test exists, on the firm side, is that market making is genuinely a job where you compute fair value, hedge ratios, and P&L impact in your head while a market moves around you. The selection signal is not a tradition — it is empirically predictive of trader performance.

## How To Drill

The standard regimen:

- **[Zetamac](https://arithmetic.zetamac.com/) daily.** 5-10 minutes, every day. Track scores in a spreadsheet. Plateau at a number for a week, then push through.
- **Default configuration first** (addition 2-100, subtraction 2-100, multiplication 2-12, division). Once you clear 50/2 minutes consistently, expand to 2-digit × 2-digit multiplication.
- **Card decks for valuation drills.** Variant: draw two cards, multiply or divide quickly. Used internally at several trader firms.
- **Working with fractions.** Convert /3, /6, /7, /8, /9, /11 to decimal in under 3 seconds. These appear in mental Black-Scholes approximations, percentage-of-portfolio calculations, and price-to-fair comparisons.

## Techniques Worth Memorizing

- **Squares to 25.** $13^2 = 169$, $14^2 = 196$, ..., $25^2 = 625$. Pattern: $(10+a)^2 = 100 + 20a + a^2$.
- **Two-digit multiplication via (a+b)(a-b) when one number is a round number.** $98 \times 102 = 100^2 - 2^2 = 9996$.
- **Percentages as fractions.** 12.5% = 1/8, 16.67% = 1/6, 14.29% = 1/7, 11.11% = 1/9.
- **Approximate doubling time** (rule of 72): years to double = 72 / annual %.
- **Approximate Black-Scholes ATM call price.** $C \approx 0.4 \cdot S \cdot \sigma \sqrt{T}$ — useful for sanity-checking option quotes in your head.
- **Half a basis point** of \$10M = \$500. Internalize basis-point translations until they are instinctive.

## Beyond Interviews

Mental math stays relevant past the interview:

- **Quoting markets** — translating fair-value calculations to bid/ask in real time.
- **Hedging on the fly** — computing the share delta-equivalent of an option position while watching the market.
- **P&L tracking** — knowing where your book stands mid-day without pulling up a screen.
- **Sanity-checking model output** — catching obvious sign errors and order-of-magnitude bugs in code review.

The skill compounds with everything else in the trader's tool kit. Without it, the rest is harder to use under pressure.

## Resources

- [Zetamac](https://arithmetic.zetamac.com/) — The standard practice tool
- [Brainstellar](https://brainstellar.com/) — Probability puzzles that exercise mental math alongside reasoning
- [[A Practical Guide to Quantitative Finance Interviews — Xinfeng Zhou]] — Many problems implicitly require speed arithmetic

## Connections

- [[A Practical Guide to Quantitative Finance Interviews — Xinfeng Zhou]] — Many problems require fast arithmetic alongside reasoning
- [[Heard on the Street — Timothy Crack]] — Brainteasers often have a mental-math component
- [[Market Making]] — Real-time market-making requires this skill under load
