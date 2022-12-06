from dataclasses import dataclass

from aoc_2022.day_06.parser import Parser


@dataclass
class Day06PartBSolver:
    input: str

    @property
    def solution(self) -> int:
        n = 14
        for i in range(len(self.input) - (n - 1)):
            chunk = self.input[i : i + n]
            if len(set(chunk)) == n:
                return i + n
        assert False, "We shouldn't get here"


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day06PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_06/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
