from aoc_2022.day_10.models import Addx, Noop, Operation


class Parser(object):
    @staticmethod
    def parse(input: str) -> list[Operation]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> Operation:
        parts = line.split()
        if parts[0] == "noop":
            return Noop()
        else:
            return Addx(int(parts[1]))
