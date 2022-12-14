from aoc_2022.day_14.models import Path, Point, State


class Parser(object):
    @staticmethod
    def parse(input: str) -> State:
        return State([Parser.parse_line(line) for line in input.strip().splitlines()])

    @staticmethod
    def parse_line(line: str) -> Path:
        points: list[Point] = []
        point_strings = line.split(" -> ")
        for p in point_strings:
            x, y = p.split(",")
            points.append(Point(int(x), int(y)))
        return Path(points)
