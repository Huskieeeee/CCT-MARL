#!/usr/bin/env bash
set -e
export PYTHONPATH="${PYTHONPATH:-}:$(pwd)/src"
python scripts/train.py --config configs/cct_marl_5x5.yaml --episodes 5 --eval-episodes 2 --seed 0 --output results/runs/smoke_test
python scripts/evaluate.py --config configs/cct_marl_5x5.yaml --output results/runs/smoke_test_eval
