from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass
from functools import cached_property
from typing import Iterator, Mapping, Optional

from aoc_2022.day_12.models import Map, Point


@dataclass
class PointInfo:
    min_distance: int
    previous: Optional[Point]


@dataclass
class Day12Solver(ABC):
    data: Map

    @property
    @abstractmethod
    def solution(self) -> int:
        ...

    @property
    @abstractmethod
    def start(self) -> Point:
        ...

    @abstractmethod
    def can_move(self, from_height: int, to_height: int) -> bool:
        ...

    @cached_property
    def point_info(self) -> Mapping[Point, PointInfo]:
        output: dict[Point, PointInfo] = {self.start: PointInfo(0, None)}
        to_check = deque[Point]([self.start])

        while to_check:
            current = to_check.pop()
            current_info = output[current]
            for p in self.next_points(current):
                next_info = output.get(p)
                if (
                    not next_info
                    or next_info.min_distance > current_info.min_distance + 1
                ):
                    output[p] = PointInfo(current_info.min_distance + 1, current)
                    to_check.append(p)

        return output

    def next_points(self, current: Point) -> Iterator[Point]:
        for move in self.possible_moves:
            p = Point(current.x + move.x, current.y + move.y)
            if p in self.data.heightmap and self.can_move(
                self.data.heightmap[current], self.data.heightmap[p]
            ):
                yield p

    @cached_property
    def possible_moves(self) -> set[Point]:
        return {
            Point(-1, 0),
            Point(1, 0),
            Point(0, -1),
            Point(0, 1),
        }
