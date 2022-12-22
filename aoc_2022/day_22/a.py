from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional, Sequence

from aoc_2022.day_22.models import Instruction, Map, Move, Turn
from aoc_2022.day_22.parser import Parser
from aoc_2022.shared.models import Point

DIRECTIONS: Sequence[Point] = [
    Point(1, 0),
    Point(0, 1),
    Point(-1, 0),
    Point(0, -1),
]


@dataclass
class Day22PartASolver:
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
        d = DIRECTIONS[self.direction_index]
        pos = self.position
        for _ in range(amount):
            x, y = pos.x, pos.y
            next_pos = Point(x + d.x, y + d.y)
            if next_pos not in self.map.all_points:
                match d:
                    case Point(-1, 0):
                        next_pos = Point(self.map.max_x_by_y[y], y)
                    case Point(1, 0):
                        next_pos = Point(self.map.min_x_by_y[y], y)
                    case Point(0, 1):
                        next_pos = Point(x, self.map.min_y_by_x[x])
                    case Point(0, -1):
                        next_pos = Point(x, self.map.max_y_by_x[x])
                    case _:
                        assert False

            if next_pos in self.map.walls:
                break
            elif next_pos in self.map.spaces:
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
    solver = Day22PartASolver(map, instructions)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_22/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
