# CCT-MARL

This repository contains the source code scaffold, experimental scripts, configuration files, result tables, and reproducibility materials for the manuscript:

**CCT-MARL: A construction-oriented hybrid multi-agent reinforcement learning framework for human–machine coordination**

The study proposes CCT-MARL, a construction-oriented hybrid multi-agent reinforcement learning framework for human–machine dyad coordination. The framework combines experience-conditioned policy learning, structured broadcast communication, and a task-progress reservation shield for construction coordination tasks involving spatial movement, build–inspect–rework feedback, waiting, collision avoidance, and communication cost.

> **Repository note for PeerJ submission:** this package is designed as a GitHub-ready repository layout for transparent review. If your final training code differs from the lightweight modules provided here, replace the corresponding files in `src/` and `scripts/` with the finalized implementation before creating the PeerJ submission release.

## Repository contents

- `src/cct_marl/`: implementation modules for the construction coordination environment, communication operator, experience manager, task-progress reservation shield, heuristic baselines, and agent interfaces.
- `scripts/`: training, evaluation, result aggregation, table-generation, and figure-generation entry points.
- `configs/`: experiment configuration files for the default 5×5 setting, shielded baselines, ablation studies, scalability studies, and reward-sensitivity experiments.
- `results/`: processed tables, figures, and example logs corresponding to the manuscript.
- `docs/`: metric definitions, algorithm notes, data dictionary, and PeerJ submission notes.
- `tests/`: smoke tests for the environment, communication module, and reservation shield.

## Installation

Python 3.10 or later is recommended.

```bash
git clone https://github.com/Huskieeeee/CCT-MARL.git
cd CCT-MARL

python -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

Alternatively, a Conda environment can be created using:

```bash
conda env create -f environment.yml
conda activate cct-marl
pip install -e .
```

## Quick reproducibility check

Run a short smoke test:

```bash
bash run_smoke_test.sh
```

The smoke test verifies that the construction coordination environment, reservation shield, communication module, and result-writing pipeline can be initialized and executed.

## Reproducing manuscript result tables

### Main comparison

```bash
bash run_main_comparison.sh
```

### Component ablation

```bash
bash run_ablation.sh
```

### Scalability experiments

```bash
bash run_scalability.sh
```

### Reward-sensitivity experiments

```bash
bash run_reward_sensitivity.sh
```

The processed result tables are provided in `results/tables/`.

## Result files

Processed result tables correspond to the manuscript tables:

- `table2_main_comparison.csv`
- `table3_shielded_baselines.csv`
- `table4_component_ablation.csv`
- `table5_scalability.csv`
- `table6_reward_sensitivity.csv`

Figures used for manuscript visualization are provided in `results/figures/` when available.

## Random seeds

Unless otherwise specified, the reported experiments use five random seeds. Seed values and configuration details are recorded in the corresponding YAML files under `configs/`.

## Hardware and runtime

Smoke tests can be run on CPU. Full multi-seed training should be run on a CUDA-capable GPU if the finalized learning implementation is used. Runtime depends on the number of seeds, grid size, and training horizon.

## Code availability statement

The source code, experimental scripts, configuration files, processed result tables, and reproduction instructions are available in this repository.

## License

The code in this repository is released under the MIT License. See `LICENSE` for details.

## Citation

If you use this repository, please cite the associated manuscript and this software repository. Citation metadata are provided in `CITATION.cff`.
