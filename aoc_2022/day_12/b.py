from collections import deque
from dataclasses import dataclass
from functools import cached_property
from typing import Iterator, Mapping, Optional

from aoc_2022.day_12.models import Map, Point
from aoc_2022.day_12.parser import CHARACTER_TO_HEIGHT_MAP, Parser


@dataclass
class PointInfo:
    min_distance: int
    previous: Optional[Point]


@dataclass
class Day12PartASolver:
    data: Map

    @property
    def solution(self) -> int:
        return min(
            [
                self.point_info[p].min_distance
                for p in self.possible_starts
                if p in self.point_info
            ]
        )

    @cached_property
    def possible_starts(self) -> set[Point]:
        return {
            p for p, height in self.data.heightmap.items() if height == self.min_height
        }

    @cached_property
    def min_height(self) -> int:
        return min(CHARACTER_TO_HEIGHT_MAP.values())

    @cached_property
    def point_info(self) -> Mapping[Point, PointInfo]:
        output: dict[Point, PointInfo] = {self.data.target: PointInfo(0, None)}
        to_check = deque[Point]([self.data.target])

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
            p_height = self.data.heightmap.get(p)
            if p_height is not None and p_height >= self.data.heightmap[current] - 1:
                yield p

    @cached_property
    def possible_moves(self) -> set[Point]:
        return {
            Point(-1, 0),
            Point(1, 0),
            Point(0, -1),
            Point(0, 1),
        }


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day12PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_12/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
