from dataclasses import dataclass
from typing import Mapping

from aoc_2022.day_19.models import Blueprint
from aoc_2022.day_19.parser import Parser


@dataclass
class Day19PartASolver:
    blueprints: Mapping[int, Blueprint]

    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day19PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_19/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
