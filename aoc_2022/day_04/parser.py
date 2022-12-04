from aoc_2022.day_04.shared import Range


class Parser(object):
    @staticmethod
    def parse(input: str) -> list[tuple[Range, Range]]:
        return [Parser.parse_line(line) for line in input.strip().splitlines()]

    @staticmethod
    def parse_line(line: str) -> tuple[Range, Range]:
        first, second = line.split(",")
        return Parser.parse_range(first), Parser.parse_range(second)

    @staticmethod
    def parse_range(line: str) -> Range:
        start, end = line.split("-")
        return Range(int(start), int(end))
