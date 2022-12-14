from dataclasses import dataclass

from aoc_2022.day_19.models import Blueprint
from aoc_2022.day_19.parser import Parser
from aoc_2022.day_19.shared import QualityChecker


@dataclass
class Day19PartASolver:
    blueprints: list[Blueprint]

    @property
    def solution(self) -> int:
        quality_checkers = [
            QualityChecker(blueprint, 24) for blueprint in self.blueprints
        ]
        quality_levels = [quality_checker.level for quality_checker in quality_checkers]
        return sum(quality_levels)


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
