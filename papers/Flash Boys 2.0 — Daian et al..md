---
type: paper
title: "Flash Boys 2.0: Frontrunning, Transaction Reordering, and Consensus Instability in Decentralized Exchanges"
authors:
  - Philip Daian
  - Steven Goldfeder
  - Tyler Kell
  - Yunqi Li
  - Xueyuan Zhao
  - Iddo Bentov
  - Lorenz Breidenbach
  - Ari Juels
year: 2019
status: unread
tags:
  - paper
  - MEV
topics:
  - "[[MEV]]"
  - "[[Frontrunning]]"
  - "[[Sandwich Attack]]"
---

# Flash Boys 2.0 — Daian et al.

**"Flash Boys 2.0: Frontrunning, Transaction Reordering, and Consensus Instability in Decentralized Exchanges"**

The foundational MEV paper. This is the paper that named and formalized the concept of Miner Extractable Value (now Maximal Extractable Value) and demonstrated its consequences for DeFi.

## Summary

The authors studied DEX activity on Ethereum and discovered a sophisticated ecosystem of arbitrage bots engaging in priority gas auctions (PGAs) to frontrun, backrun, and sandwich ordinary users' trades. Key findings:

- **Frontrunning is pervasive.** Bots monitor the mempool for profitable pending transactions and submit competing transactions with higher gas prices to get executed first.
- **Priority gas auctions.** Bots engage in real-time bidding wars, incrementally raising gas prices to outcompete each other for transaction ordering priority. These auctions consume significant blockspace and raise gas prices for all users.
- **Consensus instability.** MEV creates incentives for miners/validators to reorganize blocks (time-bandit attacks). If the MEV in a block exceeds the block reward, rational miners would fork the chain to steal that MEV. This threatens the security assumptions of the blockchain itself.
- **Quantified MEV.** The paper measured millions of dollars in MEV extraction on Ethereum DEXs, establishing MEV as a first-order economic phenomenon rather than a curiosity.

## Key Results

- Identified and categorized MEV extraction strategies: pure revenue (arbitrage), frontrunning (copying a profitable transaction with higher gas), and sandwich attacks (wrapping a victim transaction with a buy-before and sell-after).
- Demonstrated that PGAs create negative externalities: network congestion, higher gas prices, worse execution for ordinary users.
- Argued that MEV is a systemic risk to blockchain consensus, not just a user experience problem.
- Proposed that MEV mitigation requires protocol-level solutions (later realized as Flashbots, MEV-Boost, PBS).

## Connections

- [[MEV]] — This paper defined the concept
- [[Frontrunning]] — Core MEV extraction technique documented here
- [[Sandwich Attack]] — Specific attack vector first rigorously analyzed in this paper
