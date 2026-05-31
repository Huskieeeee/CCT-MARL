from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Tuple
import random

Position = Tuple[int, int]

ACTIONS = ["Wait", "Up", "Down", "Left", "Right", "Build", "Inspect", "Rework", "MachineAssist"]
MOVE_DELTAS = {
    "Up": (-1, 0),
    "Down": (1, 0),
    "Left": (0, -1),
    "Right": (0, 1),
}

@dataclass
class ConstructionEnvConfig:
    grid_size: Tuple[int, int] = (5, 5)
    num_dyads: int = 3
    max_steps: int = 200
    seed: int = 0

@dataclass
class ConstructionState:
    completed: set[Position] = field(default_factory=set)
    rework_required: set[Position] = field(default_factory=set)
    positions: List[Position] = field(default_factory=list)
    t: int = 0

class ConstructionCoordinationEnv:
    """Minimal grid-based construction coordination environment.

    The class is intentionally lightweight so that reviewers can inspect the
    build-inspect-rework lifecycle and safety interface. Replace or extend it
    with the finalized training environment if the full implementation differs.
    """

    def __init__(self, config: ConstructionEnvConfig | None = None):
        self.config = config or ConstructionEnvConfig()
        self.rng = random.Random(self.config.seed)
        self.cells = [(r, c) for r in range(self.config.grid_size[0]) for c in range(self.config.grid_size[1])]
        self.state = ConstructionState()

    def reset(self) -> Dict:
        rows, cols = self.config.grid_size
        starts = [(0, 0), (0, cols - 1), (rows - 1, 0), (rows - 1, cols - 1)]
        positions = [starts[i % len(starts)] for i in range(self.config.num_dyads)]
        self.state = ConstructionState(completed=set(), rework_required=set(), positions=positions, t=0)
        return self._observe()

    def _in_bounds(self, pos: Position) -> bool:
        r, c = pos
        rows, cols = self.config.grid_size
        return 0 <= r < rows and 0 <= c < cols

    def _move(self, pos: Position, action: str) -> Position:
        if action not in MOVE_DELTAS:
            return pos
        dr, dc = MOVE_DELTAS[action]
        cand = (pos[0] + dr, pos[1] + dc)
        return cand if self._in_bounds(cand) else pos

    def step(self, actions: List[str]) -> Tuple[Dict, float, bool, Dict]:
        assert len(actions) == self.config.num_dyads
        self.state.t += 1
        reward = 0.0
        waiting = 0
        invalid = 0
        rework = 0

        proposed = [self._move(p, a) for p, a in zip(self.state.positions, actions)]
        collisions = len(proposed) - len(set(proposed))
        self.state.positions = proposed

        for i, action in enumerate(actions):
            pos = self.state.positions[i]
            if action == "Wait":
                waiting += 1
            elif action in {"Build", "MachineAssist"}:
                if pos not in self.state.completed:
                    self.state.completed.add(pos)
                    reward += 6.0
                else:
                    invalid += 1
            elif action == "Inspect":
                if pos in self.state.completed and self.rng.random() < 0.15:
                    self.state.rework_required.add(pos)
                    reward -= 1.0
            elif action == "Rework":
                if pos in self.state.rework_required:
                    self.state.rework_required.remove(pos)
                    rework += 1
                    reward += 3.0
                else:
                    invalid += 1

        reward -= 1.25 * collisions
        reward -= 0.50 * invalid
        reward -= 0.05 * waiting
        done = len(self.state.completed) >= len(self.cells) or self.state.t >= self.config.max_steps
        if len(self.state.completed) >= len(self.cells):
            reward += 20.0
        info = {"waiting": waiting, "collision": collisions, "invalid": invalid, "rework": rework}
        return self._observe(), reward, done, info

    def _observe(self) -> Dict:
        return {
            "t": self.state.t,
            "positions": list(self.state.positions),
            "completed": sorted(self.state.completed),
            "rework_required": sorted(self.state.rework_required),
            "remaining": len(self.cells) - len(self.state.completed),
        }
