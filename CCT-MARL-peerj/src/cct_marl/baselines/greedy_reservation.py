from __future__ import annotations

from typing import Iterable, List, Tuple
from cct_marl.baselines.greedy import greedy_next_action
from cct_marl.shield.reservation_shield import ReservationShield

Position = Tuple[int, int]

def greedy_reservation_actions(positions: List[Position], unfinished_cells: Iterable[Position], grid_size: Tuple[int, int]) -> List[str]:
    actions = [greedy_next_action(p, unfinished_cells) for p in positions]
    return ReservationShield(grid_size).apply(positions, actions)["actions"]
