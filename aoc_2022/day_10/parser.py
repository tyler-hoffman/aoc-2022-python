from aoc_2022.day_10.models import Addx, Instruction, Noop


class Parser(object):
    @staticmethod
    def parse(input: str) -> list[Instruction]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> Instruction:
        parts = line.split()
        if parts[0] == "noop":
            return Noop()
        else:
            return Addx(int(parts[1]))
