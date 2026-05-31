#!/usr/bin/env bash
set -e
export PYTHONPATH="${PYTHONPATH:-}:$(pwd)/src"
python scripts/collect_results.py --study scalability
python scripts/make_tables.py --table scalability
python scripts/make_figures.py --figure scalability
