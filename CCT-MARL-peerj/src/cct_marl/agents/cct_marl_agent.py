from __future__ import annotations

class CCTMARLAgent:
    """Lightweight agent interface for the PeerJ repository scaffold.

    Replace this class with the finalized learning implementation when running
    full experiments.
    """

    def __init__(self, action_space=None, seed: int = 0):
        self.action_space = action_space or ["Wait", "Up", "Down", "Left", "Right", "Build", "Inspect", "Rework", "MachineAssist"]
        self.seed = seed

    def act(self, observation):
        return self.action_space[0]

    def update(self, *args, **kwargs):
        return {"loss": 0.0}
