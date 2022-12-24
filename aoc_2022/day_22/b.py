from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional, Sequence

from aoc_2022.day_22.models import Instruction, Map, Move, PointAtDirection, Turn
from aoc_2022.day_22.parser import Parser
from aoc_2022.shared.models import Point

DIRECTIONS: Sequence[Point] = [
    Point(1, 0),
    Point(0, 1),
    Point(-1, 0),
    Point(0, -1),
]


@dataclass
class Day22PartBSolver:
    map: Map
    instructions: list[Instruction]
    direction_index: int = 0
    _position: Optional[Point] = field(default=None, init=False)

    @property
    def solution(self) -> int:
        for instruction in self.instructions:
            match instruction:
                case Turn(direction):
                    self.turn(direction)
                case Move(amount):
                    self.move(amount)
        return self.score

    @property
    def score(self) -> int:
        p = self.position
        d = DIRECTIONS[self.direction_index]
        return 1000 * p.y + 4 * p.x + DIRECTIONS.index(d)

    def turn(self, direction: str) -> None:
        match direction:
            case "L":
                self.direction_index = (self.direction_index + 3) % 4
            case "R":
                self.direction_index = (self.direction_index + 1) % 4
            case _:
                assert False

    def move(self, amount: int) -> None:
        pos = self.position
        for _ in range(amount):
            d = DIRECTIONS[self.direction_index]
            x, y = pos.x, pos.y
            next_pos = Point(x + d.x, y + d.y)
            if next_pos in self.map.all_points:
                if next_pos in self.map.walls:
                    break
                elif next_pos in self.map.spaces:
                    pos = next_pos
                else:
                    assert False
            else:
                next_pos_and_direction = self.map.side_map[PointAtDirection(pos, d)]
                next_pos = next_pos_and_direction.point
                if next_pos in self.map.walls:
                    break
                elif next_pos in self.map.spaces:
                    self.direction_index = DIRECTIONS.index(
                        next_pos_and_direction.direction
                    )
                    pos = next_pos
                else:
                    assert False

        self.position = pos

    @cached_property
    def start(self) -> Point:
        y = 1
        x = self.map.min_x_by_y[y]
        return Point(x, y)

    @property
    def position(self) -> Point:
        return self._position or self.start

    @position.setter
    def position(self, pos: Point) -> None:
        self._position = pos


def solve(input: str) -> int:
    map, instructions = Parser.parse(input)
    solver = Day22PartBSolver(map, instructions)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_22/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
