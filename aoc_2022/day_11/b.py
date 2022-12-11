from functools import cached_property

from aoc_2022.day_11.parser import Parser
from aoc_2022.day_11.shared import Day11Solver


class Day11PartBSolver(Day11Solver):
    def manager_worry_level(self, worry_level: int) -> int:
        return worry_level % self.divisor

    @cached_property
    def divisor(self) -> int:
        output = 1
        for m in self.monkeys:
            output *= m.divisible_test
        return output


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day11PartBSolver(data, 10000)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_11/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
