from aoc_2022.day_17.parser import Parser
from aoc_2022.day_17.shared import Day17Solver


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day17Solver(data, 1000000000000)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_17/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
