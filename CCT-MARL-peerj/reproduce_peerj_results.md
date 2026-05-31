# Reproducing PeerJ manuscript results

This document describes how to reproduce or verify the empirical materials reported in the manuscript.

## 1. Environment setup

```bash
git clone https://github.com/Huskieeeee/CCT-MARL.git
cd CCT-MARL
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## 2. Smoke test

```bash
bash run_smoke_test.sh
```

Expected behavior: the script initializes the environment, runs a short rollout, and writes a small metrics file under `results/runs/smoke_test/`.

## 3. Main comparison

```bash
bash run_main_comparison.sh
```

The output table is saved to:

```text
results/tables/table2_main_comparison.csv
```

## 4. Shielded baseline study

```bash
python scripts/collect_results.py --study shielded_baselines
```

The output table is saved to:

```text
results/tables/table3_shielded_baselines.csv
```

## 5. Component ablation

```bash
bash run_ablation.sh
```

The output table is saved to:

```text
results/tables/table4_component_ablation.csv
```

## 6. Scalability study

```bash
bash run_scalability.sh
```

The output table is saved to:

```text
results/tables/table5_scalability.csv
```

## 7. Reward-sensitivity study

```bash
bash run_reward_sensitivity.sh
```

The output table is saved to:

```text
results/tables/table6_reward_sensitivity.csv
```

## 8. Regenerating figures

```bash
python scripts/make_figures.py
```

Generated figures are saved under:

```text
results/figures/
```

## 9. Notes on stochasticity

The reported results use repeated random seeds. Small numerical differences may occur across hardware, CUDA versions, and PyTorch versions. The CSV files in `results/tables/` provide the processed values used in the manuscript.
