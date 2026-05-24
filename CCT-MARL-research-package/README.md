# CCT-MARL: Construction-oriented Communication and Coordination with Task-progress Shielding

This repository package documents the CCT-MARL study for intelligent construction coordination. The work formulates a process-level human-machine construction coordination environment and evaluates a hybrid MARL framework that couples:

1. experience-conditioned policy inputs;
2. structured broadcast communication with explicit mean aggregation;
3. a task-progress reservation shield for pre-execution action correction;
4. build-inspect-rework feedback from machine-assisted construction operations.

The current manuscript follows a reviewer-resolved positioning: CCT-MARL is not presented as an unconditional scalar-dominant MARL algorithm. Instead, it is evaluated as a construction-oriented hybrid learning-and-coordination framework under a safety-efficiency-communication trade-off.

Code availability: https://github.com/Huskieeeee/CCT-MARL

## Repository layout

```text
docs/
  paper/          LaTeX draft and compiled PDF
  figures/        Clean figure assets without embedded Figure 2/3/5 labels
  results/        CSV summaries used by the manuscript
  supplementary/  Additional notes and checklists
configs/          Example experiment matrix definitions
scripts/          Helper scripts for checking result completeness
src/              Placeholder for implementation files in the public code repository
```

## Main experimental claims addressed

### 1. Shield attribution
The shielded-baseline study adds MAPPO+Shield and IQL+Shield diagnostics. Since applying the same shield makes collisions zero, the revised claim is not that CCT-MARL alone can remove collisions. The intended evidence is that CCT-MARL remains competitive in makespan, stability, and process-level coordination while using the same safety layer.

### 2. Scalability
The draft includes scale-up evidence on 8x8 with 5 dyads and 10x10 with 8 dyads, with a 20x20/10-dyad sanity setting treated as proof-of-scale rather than a fully tuned benchmark.

### 3. Heuristic baselines
The study includes Greedy and Greedy-Reservation/Prioritized-Planning style baselines. This addresses whether a small construction grid can be solved by simple hand-written rules.

### 4. Communication aggregation
The implemented aggregation operator is explicitly defined as mean aggregation. The no-aggregation ablation tests whether peer messages matter. Attention aggregation is specified as an extensible future variant; it should not be claimed as completed unless implemented and trained.

### 5. Experience manager and reward shaping
The current experience manager is a deterministic feedback updater used as policy and communication input. Misleading auxiliary losses have been removed from the reported objective. Reward sensitivity experiments test whether the result depends on a single shaping term.

## How to cite the artifacts

Use the PDF under `docs/paper/` as the current manuscript snapshot and the CSV files under `docs/results/` as the numerical source tables.

## Authors

Lingcheng Liu, Yichao Zhang, Jihong Guan, Wengen Li, Zhiwei Cao, and Shuigeng Zhou.

Shuigeng Zhou is affiliated with the School of Computer Science, Fudan University, Shanghai, China.
