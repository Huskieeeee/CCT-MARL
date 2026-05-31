from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

Position = Tuple[int, int]
MOVE_DELTAS = {
    "Up": (-1, 0),
    "Down": (1, 0),
    "Left": (0, -1),
    "Right": (0, 1),
}
SAFE_ACTION_ORDER = ["Up", "Down", "Left", "Right", "Wait"]

@dataclass
class ReservationShield:
    grid_size: Tuple[int, int]

    def _in_bounds(self, pos: Position) -> bool:
        r, c = pos
        return 0 <= r < self.grid_size[0] and 0 <= c < self.grid_size[1]

    def target(self, pos: Position, action: str) -> Position:
        if action not in MOVE_DELTAS:
            return pos
        dr, dc = MOVE_DELTAS[action]
        cand = (pos[0] + dr, pos[1] + dc)
        return cand if self._in_bounds(cand) else pos

    def apply(self, positions: List[Position], actions: List[str]) -> Dict:
        """Apply local reservation logic to candidate actions.

        Detects same-target conflicts and swap conflicts. Unsafe movement actions
        are replaced by the first safe movement if available; otherwise by Wait.
        """
        adjusted = list(actions)
        targets = [self.target(p, a) for p, a in zip(positions, actions)]
        reserved: set[Position] = set()
        intervention = 0

        # Same-target conflict detection.
        target_counts: Dict[Position, int] = {}
        for t in targets:
            target_counts[t] = target_counts.get(t, 0) + 1

        for i, (pos, action, target) in enumerate(zip(positions, actions, targets)):
            risky = False
            if action in MOVE_DELTAS and target_counts.get(target, 0) > 1:
                risky = True
            for j, (other_pos, other_target) in enumerate(zip(positions, targets)):
                if i != j and target == other_pos and other_target == pos:
                    risky = True
                    break
            if risky:
                replacement = self._safe_alternative(pos, reserved)
                adjusted[i] = replacement
                targets[i] = self.target(pos, replacement)
                intervention += int(replacement != action)
            reserved.add(targets[i])

        return {"actions": adjusted, "targets": targets, "interventions": intervention}

    def _safe_alternative(self, pos: Position, reserved: set[Position]) -> str:
        for action in SAFE_ACTION_ORDER:
            cand = self.target(pos, action)
            if cand not in reserved:
                return action
        return "Wait"
