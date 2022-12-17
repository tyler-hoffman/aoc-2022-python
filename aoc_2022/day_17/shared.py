from dataclasses import dataclass
from functools import cached_property
from typing import Sequence

from aoc_2022.day_17.models import Point, Shape

SHAPES_STRING = """
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""


class ShapeParser:
    @staticmethod
    def parse_shapes(shapes_string: str) -> Sequence[Shape]:
        lines = shapes_string.strip().splitlines()
        output: list[Shape] = []

        shape_lines_so_far: list[str] = []
        for line in lines:
            if line == "":
                output.append(ShapeParser.parse_shape(shape_lines_so_far))
                shape_lines_so_far = []
            else:
                shape_lines_so_far.append(line)
        output.append(ShapeParser.parse_shape(shape_lines_so_far))

        return output

    @staticmethod
    def parse_shape(shape_string: list[str]) -> Shape:
        output: set[Point] = set()
        bottom = len(shape_string) - 1
        for y, line in enumerate(shape_string):
            for x, char in enumerate(line):
                if char == "#":
                    output.add(Point(x, bottom - y))

        return Shape(output)


SHAPES = ShapeParser.parse_shapes(SHAPES_STRING)


@dataclass
class Day17Solver:
    jets: Sequence[int]
    iterations: int
    shape_index: int = -1
    jet_index: int = -1
    highest_rock: int = -1

    @property
    def solution(self) -> int:
        for _ in range(self.iterations):
            self.drop_next_shape()
        return self.highest_rock + 1

    def drop_next_shape(self) -> None:
        self.shape_index += 1
        self.shape_index %= len(SHAPES)
        shape = SHAPES[self.shape_index]
        shape = shape.move(2, self.highest_rock + 4)
        shape = shape

        while True:
            self.jet_index += 1
            self.jet_index %= len(self.jets)

            jet = self.jets[self.jet_index]
            next_shape = shape.move(jet, 0)
            if self.is_valid_position(next_shape):
                shape = next_shape

            next_shape = shape.move(0, -1)
            if self.is_valid_position(next_shape):
                shape = next_shape
            else:
                for p in shape.points:
                    self.landed_rocks.add(p)
                self.highest_rock = max(
                    [self.highest_rock] + [p.y for p in shape.points]
                )
                break

    def is_valid_position(self, shape: Shape) -> bool:
        return all(
            [
                not shape.overlaps(self.landed_rocks),
                all(p.x >= 0 for p in shape.points),
                all(p.x < 7 for p in shape.points),
                all(p.y >= 0 for p in shape.points),
            ]
        )

    @cached_property
    def landed_rocks(self) -> set[Point]:
        return set()

    def __repr__(self) -> str:
        lines: list[str] = []
        max_y = self.highest_rock + 4
        for y in range(max_y, -1, -1):
            line = "|"
            for x in range(7):
                line += "#" if Point(x, y) in self.landed_rocks else "."
            line += "|"
            lines.append(line)
        lines.append("+-------+")
        return "\n".join(lines)
