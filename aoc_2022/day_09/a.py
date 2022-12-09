from dataclasses import dataclass
from typing import Iterator

from aoc_2022.day_09.models import Movement, Point
from aoc_2022.day_09.parser import Parser


@dataclass
class Day09PartASolver:
    movements: list[Movement]

    @property
    def solution(self) -> int:
        return len(set(self.get_tail_positions()))

    def get_tail_positions(self) -> Iterator[Point]:
        head = Point()
        tail = Point()

        yield tail

        for movement in self.movements:
            for _ in range(movement.amount):
                head = self.next_head(head, movement.direction)
                tail = self.next_tail(head, tail)
                yield tail

    def next_head(self, current: Point, direction: str) -> Point:
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

    def next_tail(self, head: Point, tail: Point) -> Point:
        x = tail.x
        y = tail.y

        x_min = head.x - 1
        x_max = head.x + 1
        y_min = head.y - 1
        y_max = head.y + 1

        if max(abs(x - head.x), abs(y - head.y)) < 2:
            return tail
        elif x == head.x:
            if y < y_min:
                return Point(x, y + 1)
            elif y > y_max:
                return Point(x, y - 1)
            else:
                return tail
        elif y == head.y:
            if x < x_min:
                return Point(x + 1, y)
            elif x > x_max:
                return Point(x - 1, y)
            else:
                return tail

        elif x < head.x and y < head.y:
            return Point(x + 1, y + 1)
        elif x > head.x and y > head.y:
            return Point(x - 1, y - 1)
        elif x < head.x and y > head.y:
            return Point(x + 1, y - 1)
        elif x > head.x and y < head.y:
            return Point(x - 1, y + 1)
        else:
            return tail


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day09PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_09/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
