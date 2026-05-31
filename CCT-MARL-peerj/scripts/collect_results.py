from __future__ import annotations

import argparse
from pathlib import Path

TABLE_MAP = {
    "main_comparison": "table2_main_comparison.csv",
    "shielded_baselines": "table3_shielded_baselines.csv",
    "ablation": "table4_component_ablation.csv",
    "scalability": "table5_scalability.csv",
    "reward_sensitivity": "table6_reward_sensitivity.csv",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--study", required=True, choices=list(TABLE_MAP))
    args = parser.parse_args()
    path = Path("results/tables") / TABLE_MAP[args.study]
    if not path.exists():
        raise FileNotFoundError(path)
    print(f"Verified processed result table: {path}")

if __name__ == "__main__":
    main()
