from typing import Mapping

from aoc_2022.shared.models import Point


class Parser(object):
    @staticmethod
    def parse(input: str) -> Mapping[Point, int]:
        output: dict[Point, int] = {}
        lines = input.strip().splitlines()
        for y, line in enumerate(lines):
            for x, num in enumerate(line):
                output[Point(x, y)] = int(num)
        return output
