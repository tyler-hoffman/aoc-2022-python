from dataclasses import dataclass
from functools import cached_property
from typing import Mapping

from aoc_2022.day_08.parser import Parser
from aoc_2022.shared.models import Point


@dataclass
class Day08PartASolver:
    trees: Mapping[Point, int]

    @property
    def solution(self) -> int:
        return len([p for p in self.trees.keys() if self.is_visible(p)])

    def is_visible(self, point: Point) -> bool:
        return self.trees[point] > min(
            [
                self.tallest_tree_to_down_map[point],
                self.tallest_tree_to_up_map[point],
                self.tallest_tree_to_left_map[point],
                self.tallest_tree_to_right_map[point],
            ]
        )

    @cached_property
    def tallest_tree_to_left_map(self) -> Mapping[Point, int]:
        output: dict[Point, int] = {}
        for y in range(self.y_max + 1):
            tallest_so_far = -1
            for x in range(self.x_max + 1):
                output[Point(x, y)] = tallest_so_far
                tallest_so_far = max(tallest_so_far, self.trees[Point(x, y)])
        return output

    @cached_property
    def tallest_tree_to_right_map(self) -> Mapping[Point, int]:
        output: dict[Point, int] = {}
        for y in range(self.y_max + 1):
            tallest_so_far = -1
            for x in range(self.x_max, -1, -1):
                output[Point(x, y)] = tallest_so_far
                tallest_so_far = max(tallest_so_far, self.trees[Point(x, y)])
        return output

    @cached_property
    def tallest_tree_to_up_map(self) -> Mapping[Point, int]:
        output: dict[Point, int] = {}
        for x in range(self.x_max + 1):
            tallest_so_far = -1
            for y in range(self.y_max + 1):
                output[Point(x, y)] = tallest_so_far
                tallest_so_far = max(tallest_so_far, self.trees[Point(x, y)])
        return output

    @cached_property
    def tallest_tree_to_down_map(self) -> Mapping[Point, int]:
        output: dict[Point, int] = {}
        for x in range(self.x_max + 1):
            tallest_so_far = -1
            for y in range(self.y_max, -1, -1):
                output[Point(x, y)] = tallest_so_far
                tallest_so_far = max(tallest_so_far, self.trees[Point(x, y)])
        return output

    @cached_property
    def x_max(self) -> int:
        return max([p.x for p in self.trees.keys()])

    @cached_property
    def y_max(self) -> int:
        return max([p.y for p in self.trees.keys()])


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day08PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_08/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
