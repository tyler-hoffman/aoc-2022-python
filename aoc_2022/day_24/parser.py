from dataclasses import dataclass

from aoc_2022.day_24.models import Blizzard, Direction
from aoc_2022.shared.models import Point


@dataclass
class Map:
    blizzards: list[Blizzard]
    start: Point
    end: Point
    width: int
    height: int


class Parser(object):
    @staticmethod
    def parse(input: str) -> Map:
        lines = input.strip().splitlines()

        blizzards: list[Blizzard] = []
        start = Point(Parser.find_space(lines[0]), -1)
        end = Point(Parser.find_space(lines[-1]), len(lines) - 2)

        for y, line in enumerate(lines[1:-1]):
            assert line[0] == "#"
            assert line[-1] == "#"

            for x, ch in enumerate(line[1:-1]):
                point = Point(x, y)
                match ch:
                    case "^":
                        blizzards.append(Blizzard(point, Direction.NORTH))
                    case ">":
                        blizzards.append(Blizzard(point, Direction.EAST))
                    case "v":
                        blizzards.append(Blizzard(point, Direction.SOUTH))
                    case "<":
                        blizzards.append(Blizzard(point, Direction.WEST))
                    case other:
                        assert other != "."

        width = len(lines[0]) - 2
        height = len(lines) - 2
        return Map(blizzards, start, end, width, height)

    @staticmethod
    def find_space(line: str) -> int:
        return line.index(".") - 1
