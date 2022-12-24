from dataclasses import dataclass

from aoc_2022.day_24.parser import Map, Parser


@dataclass
class Day24PartASolver:
    starting_map: Map

    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day24PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_24/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
