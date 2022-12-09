from dataclasses import dataclass
from typing import Iterator

from aoc_2022.day_09.models import Movement, Point


@dataclass
class Day09Solver:
    movements: list[Movement]
    knot_count: int

    @property
    def solution(self) -> int:
        return len(set(self.get_tail_positions()))

    def get_tail_positions(self) -> Iterator[Point]:
        knots = [Point() for _ in range(self.knot_count)]

        yield knots[-1]

        for movement in self.movements:
            for _ in range(movement.amount):
                knots[0] = self.move_knot_direction(knots[0], movement.direction)
                for i in range(1, self.knot_count):
                    knots[i] = self.move_knot_to_other_knot(knots[i - 1], knots[i])
                yield knots[-1]

    def move_knot_direction(self, current: Point, direction: str) -> Point:
        match direction:
            case "R":
                return Point(current.x + 1, current.y)
            case "L":
                return Point(current.x - 1, current.y)
            case "U":
                return Point(current.x, current.y + 1)
            case "D":
                return Point(current.x, current.y - 1)
            case _:
                assert False, "Invalid direction"

    def move_knot_to_other_knot(self, head: Point, tail: Point) -> Point:
        x = tail.x
        y = tail.y

        y_diff = tail.y - head.y
        x_diff = tail.x - head.x

        if max(abs(x_diff), abs(y_diff)) < 2:
            return tail
        if x_diff == 0 and y_diff < 1:
            return Point(x, y + 1)
        elif x_diff == 0 and y_diff > 1:
            return Point(x, y - 1)
        elif y_diff == 0 and x_diff < 1:
            return Point(x + 1, y)
        elif y_diff == 0 and x_diff > 1:
            return Point(x - 1, y)
        elif x_diff < 0 and y_diff < 0:
            return Point(x + 1, y + 1)
        elif x_diff > 0 and y_diff > 0:
            return Point(x - 1, y - 1)
        elif x_diff < 0 and y_diff > 0:
            return Point(x + 1, y - 1)
        elif x_diff > 0 and y_diff < 0:
            return Point(x - 1, y + 1)
        else:
            assert False, "we shouldn't get here"
