# Algorithm notes

CCT-MARL combines four mechanism blocks:

1. **Experience-conditioned policy input**: each dyad maintains a Beta-style experience state `(alpha, beta)` updated from build, inspect, and rework feedback.
2. **Structured broadcast communication**: each dyad broadcasts compact progress and risk features; received messages are aggregated using mean aggregation.
3. **Task-progress reservation shield**: candidate actions are corrected through same-target, swap-conflict, occupied-cell, and progress-preserving reservation rules.
4. **Centralized-training/decentralized-execution interface**: policy outputs candidate actions; the shield performs executable action correction before environment transition.

This repository contains modular code for these blocks so that reviewers can inspect their logic independently.
