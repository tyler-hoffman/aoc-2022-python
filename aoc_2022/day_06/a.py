from aoc_2022.day_06.parser import Parser
from aoc_2022.day_06.shared import Day06Solver


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day06Solver(data, 4)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_06/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
