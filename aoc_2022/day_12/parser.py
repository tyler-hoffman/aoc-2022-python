import string
from typing import Mapping, Optional

from aoc_2022.day_12.models import Map, Point

ALPHABET = string.ascii_lowercase
CHARACTER_TO_HEIGHT_MAP: Mapping[str, int] = {ch: i for i, ch in enumerate(ALPHABET)}
CHARACTER_TO_HEIGHT_MAP["S"] = CHARACTER_TO_HEIGHT_MAP["a"]
CHARACTER_TO_HEIGHT_MAP["E"] = CHARACTER_TO_HEIGHT_MAP["z"]


class Parser(object):
    @staticmethod
    def parse(input: str) -> Map:
        lines = input.strip().splitlines()
        heightmap: dict[Point, int] = {}
        start: Optional[Point] = None
        end: Optional[Point] = None

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                point = Point(x, y)
                heightmap[point] = CHARACTER_TO_HEIGHT_MAP[char]
                if char == "S":
                    start = point
                elif char == "E":
                    end = point

        assert start is not None
        assert end is not None

        return Map(heightmap, start, end)
