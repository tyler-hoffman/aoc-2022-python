from dataclasses import dataclass

from aoc_2022.day_01.parser import Parser


@dataclass
class Day01PartASolver:
    calorie_sets: list[list[int]]

    @property
    def solution(self) -> int:
        return max(self.totals)

    @property
    def totals(self) -> set[int]:
        return {sum(x) for x in self.calorie_sets}


def solve(s: str) -> int:
    data = Parser.parse(s)
    solver = Day01PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_01/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
