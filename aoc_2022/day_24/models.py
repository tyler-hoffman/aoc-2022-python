from dataclasses import dataclass
from enum import Enum

from aoc_2022.shared.models import Point


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


@dataclass
class Blizzard:
    position: Point
    direction: Direction
