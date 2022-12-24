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

    def dist(self, other: Point) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    @property
    def neighbors_without_diagonals(self) -> set[Point]:
        x = self.x
        y = self.y
        return {
            Point(x, y - 1),
            Point(x, y + 1),
            Point(x - 1, y),
            Point(x + 1, y),
        }
