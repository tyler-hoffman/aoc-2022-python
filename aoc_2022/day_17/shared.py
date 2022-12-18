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

Row = tuple[bool, bool, bool, bool, bool, bool, bool]


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
        time = 0
        skipped_height = 0
        skipped_cycles = False
        while time < self.iterations:
            resting_place = self.drop_next_shape()
            self.land_shape(resting_place, time)
            if not skipped_cycles:
                top = self.get_top(min({p.y for p in resting_place.points}))
                key = (self.shape_index, self.jet_index, top)
                if key in self.cached_tops:
                    previous_time, previous_highest = self.cached_tops[key]
                    cycle_length = time - previous_time
                    height_per_cycle = self.highest_rock - previous_highest
                    remaining_cycles = (self.iterations - 1 - time) // cycle_length
                    time += remaining_cycles * cycle_length
                    skipped_height = remaining_cycles * height_per_cycle
                    skipped_cycles = True
                else:
                    self.cached_tops[key] = (time, self.highest_rock)
            time += 1
        return self.highest_rock + 1 + skipped_height

    @cached_property
    def cached_tops(self) -> dict[tuple[int, int, tuple[Row, ...]], tuple[int, int]]:
        return {}

    def get_top(self, lowest_y: int) -> tuple[Row, ...]:
        if self.highest_rock - lowest_y > 100:
            assert False
        rows = [self.get_row(y) for y in range(lowest_y, self.highest_rock + 1)]
        return tuple(rows)

    def land_shape(self, shape: Shape, time: int) -> None:
        ys = {p.y for p in shape.points}

        for p in shape.points:
            self.landed_rocks.add(p)

        self.highest_rock = max([self.highest_rock] + list(ys))

    def drop_next_shape(self) -> Shape:
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
                return shape

    def get_row(self, y: int) -> Row:
        return tuple([Point(x, y) in self.landed_rocks for x in range(7)])

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
