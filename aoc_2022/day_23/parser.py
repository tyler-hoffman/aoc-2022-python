from aoc_2022.shared.models import Point


class Parser(object):
    @staticmethod
    def parse(input: str) -> set[Point]:
        output: set[Point] = set()
        lines = input.strip().splitlines()
        for y, line in enumerate(lines):
            for x, ch in enumerate(line):
                if ch == "#":
                    output.add(Point(x, y))
                else:
                    assert ch == "."
        return output
