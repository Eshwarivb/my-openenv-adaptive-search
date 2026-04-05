---
title: Adaptive Search Environment
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: docker
app_file: inference.py
pinned: false
---

# Adaptive Search Environment (OpenEnv)

## Overview
A reinforcement learning environment that tests how efficiently agents can find a target value within a given range using directional feedback ("low", "high", "correct").

This environment models iterative search optimization problems such as parameter tuning, diagnostic testing, and decision refinement under uncertainty.

## Tasks
- Task 1: Range 1–10
- Task 2: Range 1–50
- Task 3: Range 1–100

## Action Space
- Integer guesses within range

## Observation Space
- "low", "high", "correct"

## Reward Function
- Based on distance to target (partial progress)
- Higher reward for efficient convergence

## Run
```bash
python inference.py
```
