import re

from aoc_2022.day_22.models import Instruction, Map, Move, Turn
from aoc_2022.shared.models import Point


class Parser(object):
    instruction_regex = re.compile(r"L|R|\d+")

    @staticmethod
    def parse(input: str) -> tuple[Map, list[Instruction]]:
        lines = input.splitlines()
        while not lines[0]:
            lines = lines[1:]
        while not lines[-1]:
            lines = lines[:-1]

        return Parser.parse_map(lines[:-2]), Parser.parse_instructions(lines[-1])

    @staticmethod
    def parse_map(lines: list[str]) -> Map:
        spaces: set[Point] = set()
        walls: set[Point] = set()
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == ".":
                    spaces.add(Point(x + 1, y + 1))
                elif char == "#":
                    walls.add(Point(x + 1, y + 1))

        return Map(spaces, walls)

    @staticmethod
    def parse_instructions(line: str) -> list[Instruction]:
        tokens = Parser.instruction_regex.findall(line)
        output: list[Instruction] = []
        for token in tokens:
            if token in {"L", "R"}:
                output.append(Turn(token))
            else:
                output.append(Move(int(token)))
        return output
