from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def move(self, x: int, y: int) -> Point:
        return Point(self.x + x, self.y + y)


@dataclass(frozen=True)
class Shape:
    points: set[Point]

    def move(self, x: int, y: int) -> Shape:
        return Shape({p.move(x, y) for p in self.points})

    def overlaps(self, points: set[Point]) -> bool:
        return any([p in points for p in self.points])
