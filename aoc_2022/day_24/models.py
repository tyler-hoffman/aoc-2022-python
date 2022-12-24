from dataclasses import dataclass
from enum import Enum

from aoc_2022.shared.models import Point


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


@dataclass(frozen=True)
class Blizzard:
    position: Point
    direction: Direction


@dataclass(frozen=True)
class Map:
    blizzards: list[Blizzard]
    start: Point
    end: Point
    width: int
    height: int
