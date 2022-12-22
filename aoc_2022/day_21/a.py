from dataclasses import dataclass

from aoc_2022.day_21.parser import Parser
from aoc_2022.day_21.shared import Day21Solver


@dataclass(frozen=True)
class Day21PartASolver(Day21Solver):
    @property
    def solution(self) -> int:
        self.monkey_dict["root"]
        return self.get_monkey_value("root")


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day21PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_21/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
