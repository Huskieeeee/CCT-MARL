from __future__ import annotations

from typing import Iterable, Tuple

Position = Tuple[int, int]

def greedy_next_action(position: Position, unfinished_cells: Iterable[Position]) -> str:
    cells = list(unfinished_cells)
    if not cells:
        return "Wait"
    target = min(cells, key=lambda c: abs(c[0] - position[0]) + abs(c[1] - position[1]))
    if target == position:
        return "Build"
    if target[0] < position[0]:
        return "Up"
    if target[0] > position[0]:
        return "Down"
    if target[1] < position[1]:
        return "Left"
    if target[1] > position[1]:
        return "Right"
    return "Wait"
