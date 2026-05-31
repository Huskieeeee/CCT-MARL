#!/usr/bin/env bash
set -e
export PYTHONPATH="${PYTHONPATH:-}:$(pwd)/src"
python scripts/collect_results.py --study reward_sensitivity
python scripts/make_tables.py --table reward_sensitivity
