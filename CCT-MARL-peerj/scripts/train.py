from __future__ import annotations

import argparse, json
from pathlib import Path
import yaml

from cct_marl.envs.construction_env import ConstructionCoordinationEnv, ConstructionEnvConfig
from cct_marl.shield.reservation_shield import ReservationShield
from cct_marl.experience.experience_manager import ExperienceManager
from cct_marl.communication.mean_broadcast import MeanBroadcastAggregator


def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--episodes", type=int, default=None)
    parser.add_argument("--eval-episodes", type=int, default=None)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    cfg = load_config(args.config)
    env_cfg = cfg.get("environment", {})
    exp_cfg = cfg.get("experiment", {})
    seed = args.seed if args.seed is not None else exp_cfg.get("seeds", [0])[0]
    grid_size = tuple(env_cfg.get("grid_size", [5, 5]))
    num_dyads = int(env_cfg.get("num_dyads", 3))
    max_steps = int(env_cfg.get("max_steps", 200))

    env = ConstructionCoordinationEnv(ConstructionEnvConfig(grid_size=grid_size, num_dyads=num_dyads, max_steps=max_steps, seed=seed))
    shield = ReservationShield(grid_size=grid_size)
    experience = ExperienceManager(num_dyads=num_dyads)
    aggregator = MeanBroadcastAggregator()

    obs = env.reset()
    total_return = 0.0
    totals = {"waiting": 0, "collision": 0, "rework": 0, "bits": 0.0}
    episodes = args.episodes or 1
    for _episode in range(episodes):
        obs = env.reset()
        done = False
        while not done:
            actions = ["Right" if i % 2 == 0 else "Down" for i in range(num_dyads)]
            protected = shield.apply(obs["positions"], actions)
            obs, reward, done, info = env.step(protected["actions"])
            total_return += reward
            totals["waiting"] += info.get("waiting", 0)
            totals["collision"] += info.get("collision", 0)
            totals["rework"] += info.get("rework", 0)
            totals["bits"] += len(aggregator.aggregate([[1.0, 0.0, 0.0] for _ in range(max(num_dyads - 1, 1))])) * num_dyads
            if info.get("rework", 0):
                experience.update(0, positive=1.0)
            if obs["t"] >= max_steps:
                break

    out_dir = Path(args.output or cfg.get("output", {}).get("save_dir", "results/runs/default"))
    out_dir.mkdir(parents=True, exist_ok=True)
    metrics = {
        "config": args.config,
        "seed": seed,
        "episodes": episodes,
        "return": total_return,
        "makespan": obs.get("t", 0),
        **totals,
        "experience_means": experience.means(),
    }
    (out_dir / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print(json.dumps(metrics, indent=2))

if __name__ == "__main__":
    main()
