from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def move(self, x: int, y: int) -> Point:
        return Point(self.x + x, self.y + y)
