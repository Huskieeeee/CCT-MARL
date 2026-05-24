# Experiment Matrix

This document summarizes the experiments used to address the reviewer concerns.

## E1 Main comparison
Methods: IQL, VDN, MAPPO, CCT-MARL.
Metrics: Return, Makespan, Waiting, Collision, Rework, Bits.

## E2 Shielded baseline and heuristic baselines
Methods: MAPPO+Shield, IQL+Shield diagnostics, Greedy, Greedy-Reservation, CCT-MARL.
Purpose: separate shield attribution from learned policy behavior.
Important interpretation: after shield correction, collision may be zero for all shielded methods; therefore the paper emphasizes makespan, variance, intervention rate when available, waiting, and communication cost.

## E3 Scalability
Settings: 8x8/5 dyads, 10x10/8 dyads, and optional 20x20/10 dyads.
Purpose: test whether the framework is limited to the 5x5 setting.

## E4 Communication aggregation
Completed: no aggregation vs. mean aggregation.
Specified future extension: attention aggregation inspired by TarMAC-style message weighting.

## E5 Reward sensitivity
Settings: full reward, without speed bonus, without waiting penalty, without collision penalty, and without invalid-action penalty.
Purpose: test whether the reported coordination behavior is explained only by a single shaping term.

## Remaining recommended experiments

1. Complete shield intervention-rate logging for all shielded methods.
2. Train attention aggregation only after implementing actual attention-based message weighting.
3. Train auxiliary experience loss only after adding the auxiliary prediction head and adding the loss to the optimizer objective.
4. Run 20x20 with more seeds if it is to be treated as a full benchmark rather than a sanity scale test.
