from dataclasses import dataclass

from aoc_2022.day_06.parser import Parser


@dataclass
class Day06PartASolver:
    input: str

    @property
    def solution(self) -> int:
        for i in range(len(self.input) - 3):
            chunk = self.input[i : i + 4]
            if len(set(chunk)) == 4:
                return i + 4
        assert False, "We shouldn't get here"


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day06PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_06/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
