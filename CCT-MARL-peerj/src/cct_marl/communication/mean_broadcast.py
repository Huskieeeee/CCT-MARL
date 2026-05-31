from __future__ import annotations

from typing import Iterable
import numpy as np

class MeanBroadcastAggregator:
    """Structured mean aggregation for peer messages."""

    def aggregate(self, messages: Iterable[Iterable[float]]) -> np.ndarray:
        arr = np.asarray(list(messages), dtype=float)
        if arr.size == 0:
            return np.zeros(0, dtype=float)
        if arr.ndim == 1:
            arr = arr.reshape(1, -1)
        return arr.mean(axis=0)
