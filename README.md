# Adaptive Search Environment (OpenEnv)

## Overview
This project implements a reinforcement learning environment where an agent iteratively searches for a target value using feedback signals.

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
