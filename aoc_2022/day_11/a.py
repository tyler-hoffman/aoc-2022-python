from aoc_2022.day_11.parser import Parser
from aoc_2022.day_11.shared import Day11Solver


class Day11PartASolver(Day11Solver):
    def manager_worry_level(self, worry_level: int) -> int:
        return worry_level // 3


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day11PartASolver(data, 20)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_11/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
