from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def move(self, x: int, y: int) -> Point:
        return Point(self.x + x, self.y + y)
