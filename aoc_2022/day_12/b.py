from dataclasses import dataclass
from functools import cached_property
from typing import Optional

from aoc_2022.day_12.models import Point
from aoc_2022.day_12.parser import Parser
from aoc_2022.day_12.shared import Day12Solver


@dataclass
class PointInfo:
    min_distance: int
    previous: Optional[Point]


class Day12PartASolver(Day12Solver):
    @property
    def solution(self) -> int:
        return min(
            [
                self.point_info[p].min_distance
                for p in self.possible_starts
                if p in self.point_info
            ]
        )

    @property
    def start(self) -> Point:
        return self.data.target

    def can_move(self, from_height: int, to_height: int) -> bool:
        return to_height >= from_height - 1

    @cached_property
    def possible_starts(self) -> set[Point]:
        return {
            p for p, height in self.data.heightmap.items() if height == self.min_height
        }

    @cached_property
    def min_height(self) -> int:
        return min(self.data.heightmap.values())


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
