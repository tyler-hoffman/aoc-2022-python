from dataclasses import dataclass

from aoc_2022.day_14.models import State
from aoc_2022.day_14.parser import Parser


class PartAState(State):
    @property
    def floor_depth(self) -> None:
        return None


@dataclass
class Day14PartASolver:
    state: State

    @property
    def solution(self) -> int:
        grains_added = 0

        while True:
            landed = self.state.drop_sand()
            if landed:
                grains_added += 1
            else:
                break
        return grains_added


def solve(input: str) -> int:
    paths = Parser.parse(input)
    solver = Day14PartASolver(PartAState(paths))

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_14/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
