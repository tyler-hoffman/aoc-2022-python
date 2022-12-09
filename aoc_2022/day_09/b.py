from dataclasses import dataclass
from typing import Iterator

from aoc_2022.day_09.models import Movement, Point
from aoc_2022.day_09.parser import Parser
from aoc_2022.day_09.shared import move_knot_direction, move_knot_to_other_knot


@dataclass
class Day09PartBSolver:
    movements: list[Movement]

    @property
    def solution(self) -> int:
        return len(set(self.get_tail_positions()))

    def get_tail_positions(self) -> Iterator[Point]:
        knots = [Point() for _ in range(10)]

        yield knots[-1]

        for movement in self.movements:
            for _ in range(movement.amount):
                knots[0] = move_knot_direction(knots[0], movement.direction)
                for i in range(1, 10):
                    knots[i] = move_knot_to_other_knot(knots[i - 1], knots[i])
                yield knots[-1]


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day09PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_09/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
