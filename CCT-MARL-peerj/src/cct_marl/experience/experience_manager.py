from __future__ import annotations

from dataclasses import dataclass

@dataclass
class ExperienceState:
    alpha: float = 1.0
    beta: float = 1.0

    @property
    def mean(self) -> float:
        eps = 1e-8
        return self.alpha / (self.alpha + self.beta + eps)

class ExperienceManager:
    """Beta-style dyad-level experience updater."""

    def __init__(self, num_dyads: int, eta_pos: float = 1.0, eta_neg: float = 1.0):
        self.num_dyads = num_dyads
        self.eta_pos = eta_pos
        self.eta_neg = eta_neg
        self.states = [ExperienceState() for _ in range(num_dyads)]

    def update(self, dyad_id: int, positive: float = 0.0, negative: float = 0.0) -> ExperienceState:
        state = self.states[dyad_id]
        state.alpha += self.eta_pos * max(0.0, positive)
        state.beta += self.eta_neg * max(0.0, negative)
        return state

    def means(self):
        return [s.mean for s in self.states]
