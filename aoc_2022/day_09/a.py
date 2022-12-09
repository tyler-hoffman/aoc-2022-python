from dataclasses import dataclass
from typing import Iterator

from aoc_2022.day_09.models import Movement, Point
from aoc_2022.day_09.parser import Parser
from aoc_2022.day_09.shared import move_knot_direction, move_knot_to_other_knot


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
                head = move_knot_direction(head, movement.direction)
                tail = move_knot_to_other_knot(head, tail)
                yield tail


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
