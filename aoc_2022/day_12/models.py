from dataclasses import dataclass
from typing import Mapping

from aoc_2022.shared.models import Point


@dataclass
class Map:
    heightmap: Mapping[Point, int]
    start: Point
    target: Point
