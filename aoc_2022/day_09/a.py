from aoc_2022.day_09.parser import Parser
from aoc_2022.day_09.shared import Day09Solver


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day09Solver(data, 2)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_09/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
