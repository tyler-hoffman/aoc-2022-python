from aoc_2022.day_20.parser import Parser
from aoc_2022.day_20.shared import Day20Solver


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day20Solver(data, multiplier=811589153, rounds=10)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_20/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
