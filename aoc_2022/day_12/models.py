from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass
class Map:
    heightmap: Mapping[Point, int]
    start: Point
    target: Point
