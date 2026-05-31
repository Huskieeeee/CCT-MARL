#!/usr/bin/env bash
set -e
export PYTHONPATH="${PYTHONPATH:-}:$(pwd)/src"
python scripts/collect_results.py --study ablation
python scripts/make_tables.py --table ablation
