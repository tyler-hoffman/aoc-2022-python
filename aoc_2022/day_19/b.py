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
            QualityChecker(blueprint, 32) for blueprint in self.blueprints[:3]
        ]
        max_geode_counts = [
            quality_checker.max_geodes for quality_checker in quality_checkers
        ]

        output = 1
        for max_geode_count in max_geode_counts:
            output *= max_geode_count
        return output


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
