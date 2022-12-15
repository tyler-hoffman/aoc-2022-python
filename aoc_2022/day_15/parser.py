import re

from aoc_2022.day_15.models import Point, Sensor


class Parser(object):
    regex_pattern = re.compile(r"-?\d+")

    @staticmethod
    def parse(input: str) -> list[Sensor]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> Sensor:
        x1, y1, x2, y2 = [int(x) for x in Parser.regex_pattern.findall(line)]
        return Sensor(Point(x1, y1), Point(x2, y2))
