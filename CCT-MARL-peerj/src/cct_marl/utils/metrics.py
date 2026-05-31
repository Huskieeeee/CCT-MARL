from __future__ import annotations

from dataclasses import dataclass

@dataclass
class EpisodeMetrics:
    episode_return: float = 0.0
    makespan: int = 0
    waiting: int = 0
    collision: int = 0
    rework: int = 0
    bits: float = 0.0

    def as_dict(self):
        return {
            "return": self.episode_return,
            "makespan": self.makespan,
            "waiting": self.waiting,
            "collision": self.collision,
            "rework": self.rework,
            "bits": self.bits,
        }
