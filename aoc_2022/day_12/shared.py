from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property, total_ordering
from queue import PriorityQueue
from typing import Any, Iterator, Mapping, Optional

from aoc_2022.day_12.models import Map, Point


@total_ordering
@dataclass(frozen=True)
class PointInfo:
    min_distance: int
    previous: Optional[PointInfo]
    point: Point

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, PointInfo):
            return self.min_distance < other.min_distance
        else:
            return False

    def total_distance(self) -> int:
        if self.previous:
            return 1 + self.previous.total_distance()
        else:
            return 0


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
        output: dict[Point, PointInfo] = {self.start: PointInfo(0, None, self.start)}
        to_check: PriorityQueue[PointInfo] = PriorityQueue()
        to_check.put(output[self.start])

        while not to_check.empty():
            current = to_check.get()
            current_info = output[current.point]
            for p in self.next_points(current.point):
                next_info = output.get(p)
                if (
                    not next_info
                    or next_info.min_distance > current_info.min_distance + 1
                ):
                    output[p] = PointInfo(
                        current_info.min_distance + 1, current_info, p
                    )
                    to_check.put(output[p])

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
