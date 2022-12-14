from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from typing import Sequence


@dataclass
class State:
    paths: Sequence[Path]

    def drop_sand(self) -> bool:
        """Drop a grain of sand.
        Returns True if we are able to place
        the sand. Returns false if the sand falls
        into the void
        """
        x = 500
        y = 0
        while y <= self.max_depth:
            if Point(x, y + 1) in self.occupied:
                if Point(x - 1, y + 1) not in self.occupied:
                    x -= 1
                elif Point(x + 1, y + 1) not in self.occupied:
                    x += 1
                else:
                    self.occupied.add(Point(x, y))
                    return True
            y += 1
        return False

    @cached_property
    def occupied(self) -> set[Point]:
        return set(self.originally_occupied)

    @cached_property
    def max_depth(self) -> int:
        return max([p.y for p in self.originally_occupied])

    @cached_property
    def originally_occupied(self) -> set[Point]:
        output: set[Point] = set()
        for path in self.paths:
            current = path.points[0]
            for p in path.points[1:]:
                if p.x > current.x:
                    for x in range(current.x, p.x + 1):
                        output.add(Point(x, current.y))
                elif p.x < current.x:
                    for x in range(p.x, current.x + 1):
                        output.add(Point(x, current.y))
                elif p.y > current.y:
                    for y in range(current.y, p.y + 1):
                        output.add(Point(current.x, y))
                else:
                    for y in range(p.y, current.y + 1):
                        output.add(Point(current.x, y))
                current = p

        return output


@dataclass
class Path:
    points: Sequence[Point]


@dataclass(frozen=True)
class Point:
    x: int
    y: int
