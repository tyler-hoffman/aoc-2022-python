from dataclasses import dataclass

from aoc_2022.day_14.models import Point, State, StateWithFloor
from aoc_2022.day_14.parser import Parser


@dataclass
class Day14PartBSolver:
    state: State

    @property
    def solution(self) -> int:
        grains_added = 0
        while True:
            position = self.state.drop_sand()
            grains_added += 1
            if position and position.y < 1:
                print("foo")
            if position == Point(500, 0):
                break
        return grains_added


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day14PartBSolver(StateWithFloor(data))

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_14/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
