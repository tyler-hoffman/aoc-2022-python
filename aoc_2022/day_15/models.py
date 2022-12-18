from dataclasses import dataclass
from functools import cached_property
from typing import Optional

from aoc_2022.shared.models import Point


@dataclass
class Range:
    low: int
    high: int

    def in_range(self, value: int) -> bool:
        return value >= self.low and value <= self.high

    @property
    def count(self) -> int:
        return self.high - self.low + 1


@dataclass(frozen=True)
class Sensor:
    position: Point
    closest_beacon: Point

    @property
    def range(self) -> int:
        return abs(self.position.x - self.closest_beacon.x) + abs(
            self.position.y - self.closest_beacon.y
        )

    def in_range(self, point: Point) -> bool:
        return (
            abs(self.position.x - point.x) + abs(self.position.y - point.y)
            <= self.range
        )

    @cached_property
    def outline(self) -> set[Point]:
        output: set[Point] = set()
        dist = self.range + 1
        for y_offset in range(dist + 1):
            x_offset = dist - y_offset
            output.add(Point(self.position.x - x_offset, self.position.y + y_offset))
            output.add(Point(self.position.x - x_offset, self.position.y - y_offset))
            output.add(Point(self.position.x + x_offset, self.position.y + y_offset))
            output.add(Point(self.position.x + x_offset, self.position.y - y_offset))
        return output

    def covered_x_range_for_y(self, y: int) -> Optional[Range]:
        dist = abs(y - self.position.y)
        to_expand = self.range - dist
        if to_expand >= 0:
            return Range(self.position.x - to_expand, self.position.x + to_expand)
        else:
            return None
