from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional, Sequence


@dataclass
class State(ABC):
    paths: Sequence[Path]
    known_path: list[Point] = field(default_factory=lambda: [Point(500, 0)], init=False)

    def drop_sand(self) -> Optional[Point]:
        """Drop a grain of sand.
        Returns the point the grain landed at if it
        didn't fall into the void. Otherwise returns
        None.
        """
        start = self.known_path.pop()
        while start in self.occupied:
            start = self.known_path.pop()

        x = start.x
        y = start.y

        while y <= self.max_depth + 10:
            self.known_path.append(Point(x, y))

            if self.floor_depth is not None and y + 1 == self.floor_depth:
                point = Point(x, y)
                self.occupied.add(point)
                return point

            elif Point(x, y + 1) in self.occupied:
                if Point(x - 1, y + 1) not in self.occupied:
                    x -= 1
                elif Point(x + 1, y + 1) not in self.occupied:
                    x += 1
                else:
                    point = Point(x, y)
                    self.occupied.add(point)
                    return point

            y += 1

        return None

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

    @property
    @abstractmethod
    def floor_depth(self) -> Optional[int]:
        ...


@dataclass
class Path:
    points: Sequence[Point]


@dataclass(frozen=True)
class Point:
    x: int
    y: int
