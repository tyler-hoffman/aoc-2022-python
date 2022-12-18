from dataclasses import dataclass
from functools import cached_property
from typing import Mapping

from aoc_2022.day_08.parser import Parser
from aoc_2022.shared.models import Point


@dataclass
class Day08PartBSolver:
    trees: Mapping[Point, int]

    @property
    def solution(self) -> int:
        return max([self.scenic_score(p) for p in self.trees.keys()])

    def scenic_score(self, p: Point) -> int:
        height = self.trees[p]
        left = 0
        right = 0
        up = 0
        down = 0

        for x in range(p.x - 1, -1, -1):
            left += 1
            if self.trees[Point(x, p.y)] >= height:
                break
        for x in range(p.x + 1, self.x_max + 1):
            right += 1
            if self.trees[Point(x, p.y)] >= height:
                break
        for y in range(p.y - 1, -1, -1):
            up += 1
            if self.trees[Point(p.x, y)] >= height:
                break
        for y in range(p.y + 1, self.y_max + 1):
            down += 1
            if self.trees[Point(p.x, y)] >= height:
                break

        return left * right * up * down

    @cached_property
    def x_max(self) -> int:
        return max([p.x for p in self.trees.keys()])

    @cached_property
    def y_max(self) -> int:
        return max([p.y for p in self.trees.keys()])


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day08PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_08/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
