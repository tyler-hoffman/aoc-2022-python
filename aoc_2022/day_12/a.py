from dataclasses import dataclass
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
        info = self.point_info
        return info[self.data.target].min_distance

    @property
    def start(self) -> Point:
        return self.data.start

    def can_move(self, from_height: int, to_height: int) -> bool:
        return to_height <= from_height + 1


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
