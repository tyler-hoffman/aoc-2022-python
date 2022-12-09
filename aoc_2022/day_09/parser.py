from aoc_2022.day_09.models import Movement


class Parser(object):
    @staticmethod
    def parse(input: str) -> list[Movement]:
        return [Parser.parse_line(line) for line in input.strip().splitlines()]

    @staticmethod
    def parse_line(line: str) -> Movement:
        direction, amount = line.split()
        return Movement(direction, int(amount))
