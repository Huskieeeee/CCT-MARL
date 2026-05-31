from __future__ import annotations

import argparse
from pathlib import Path

VALID = {"main_comparison", "ablation", "scalability", "reward_sensitivity"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--table", required=True)
    args = parser.parse_args()
    if args.table not in VALID:
        raise ValueError(f"Unknown table group: {args.table}")
    print(f"Table group '{args.table}' is available in results/tables/.")

if __name__ == "__main__":
    main()
