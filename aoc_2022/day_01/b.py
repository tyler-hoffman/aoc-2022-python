from dataclasses import dataclass

from aoc_2022.day_01.parser import Parser


@dataclass
class Day01PartBSolver:
    calorie_sets: list[list[int]]

    @property
    def solution(self) -> int:
        sorted_totals = sorted(self.totals)
        return sum(sorted_totals[-3:])

    @property
    def totals(self) -> set[int]:
        return {sum(x) for x in self.calorie_sets}


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day01PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_01/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
