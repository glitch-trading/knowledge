---
type: course
title: "Neural Networks: Zero to Hero"
platform: YouTube
url: "https://karpathy.ai/zero-to-hero.html"
status: not-started
tags:
  - course
  - machine-learning
  - deep-learning
level: 6
topics: []
---

**Andrej Karpathy. Build a GPT from scratch, line by line, in PyTorch.**

## What It Covers

A self-contained series that walks from manually-implemented backpropagation (micrograd) through a character-level language model, makemore, a multi-layer perceptron with batchnorm, an autograd refresher, and finally a GPT trained on Shakespeare. Every step is implemented from scratch in PyTorch with the math derived live on screen.

Order of episodes:
- The spelled-out intro to neural networks and backpropagation: building micrograd
- The spelled-out intro to language modeling: building makemore (bigram → MLP → WaveNet)
- Building makemore Part 2-5: activations, batchnorm, manual backprop, deeper networks
- Let's build GPT: from scratch, in code, spelled out
- Let's build the GPT Tokenizer
- Let's reproduce GPT-2 (124M)

## Key Takeaways

- Backpropagation is not magic — once you implement it manually on a small expression DAG, the production version (PyTorch autograd) becomes legible rather than mysterious.
- Most "deep learning tricks" (batchnorm, residual connections, careful initialization, learning-rate schedules) exist to combat one of two enemies: vanishing/exploding gradients, or covariate shift between layers.
- Attention is a soft, differentiable dictionary lookup. The Q/K/V terminology obscures a simple averaging operation weighted by learned similarity.
- Tokenization is where many silent bugs in LLM applications live — including in financial-text pipelines.
- The same architecture that produces ChatGPT can be trained on financial text. Understanding it end-to-end is the prerequisite for trusting (or distrusting) [[Large Language Models in Quant Research|LLM-based research tools]].

## Connections

- [[The Elements of Statistical Learning — Hastie, Tibshirani & Friedman]] — Classical-ML counterpart
- [[Advances in Financial Machine Learning — López de Prado]] — Applies ML methods to finance
- [[Large Language Models in Quant Research]] — Why understanding LLMs end-to-end matters for quant work
- [[Level 6 — Advanced Topics]] — Machine learning section
