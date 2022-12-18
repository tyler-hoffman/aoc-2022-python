from aoc_2022.day_18.models import Point3D


class Parser(object):
    @staticmethod
    def parse(input: str) -> list[Point3D]:
        lines = input.strip().splitlines()
        return [Parser.parse_point(line) for line in lines]

    @staticmethod
    def parse_point(line: str) -> Point3D:
        x, y, z = [int(x) for x in line.split(",")]
        return Point3D(x, y, z)
