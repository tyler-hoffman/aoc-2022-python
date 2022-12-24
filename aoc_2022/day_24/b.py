from dataclasses import dataclass

from aoc_2022.day_24.parser import Parser
from aoc_2022.day_24.shared import Day24Solver, State
from aoc_2022.shared.models import Point


@dataclass
class Day24PartBSolver(Day24Solver):
    @property
    def solution(self) -> int:
        time_a = self.get_min_time_for_journey(State(self.start, 0), self.end)
        time_b = self.get_min_time_for_journey(State(self.end, time_a), self.start)
        return self.get_min_time_for_journey(State(self.start, time_b), self.end)

    @property
    def start(self) -> Point:
        return self.starting_map.start

    @property
    def end(self) -> Point:
        return self.starting_map.end


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day24PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_24/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
