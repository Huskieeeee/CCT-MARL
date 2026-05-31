#!/usr/bin/env bash
set -e
export PYTHONPATH="${PYTHONPATH:-}:$(pwd)/src"
python scripts/collect_results.py --study main_comparison
python scripts/make_tables.py --table main_comparison
python scripts/make_figures.py --figure main_comparison
