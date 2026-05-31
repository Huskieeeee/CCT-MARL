from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--figure", default="main_comparison")
    args = parser.parse_args()
    out_dir = Path("results/figures")
    out_dir.mkdir(parents=True, exist_ok=True)
    if args.figure == "main_comparison":
        df = pd.read_csv("results/tables/table2_main_comparison.csv")
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.bar(df["method"], df["makespan_mean"])
        ax.set_ylabel("Makespan")
        ax.set_title("Main comparison: makespan")
        ax.tick_params(axis="x", rotation=45)
        fig.tight_layout()
        fig.savefig(out_dir / "generated_main_comparison_makespan.png", dpi=300)
        plt.close(fig)
    elif args.figure == "scalability":
        df = pd.read_csv("results/tables/table5_scalability.csv")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(df["grid"].astype(str) + " / " + df["method"], df["makespan_mean"])
        ax.set_ylabel("Makespan")
        ax.set_title("Scalability")
        ax.tick_params(axis="x", rotation=45)
        fig.tight_layout()
        fig.savefig(out_dir / "generated_scalability_makespan.png", dpi=300)
        plt.close(fig)
    print(f"Generated figure group: {args.figure}")

if __name__ == "__main__":
    main()
