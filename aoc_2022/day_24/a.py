from dataclasses import dataclass

from aoc_2022.day_24.parser import Parser
from aoc_2022.day_24.shared import Day24Solver, State


@dataclass
class Day24PartASolver(Day24Solver):
    @property
    def solution(self) -> int:
        start = State(self.starting_map.start, 0)
        return self.get_min_time_for_journey(start, self.starting_map.end)


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
