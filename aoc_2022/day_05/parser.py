import math
import re
from dataclasses import dataclass
from typing import Mapping

from aoc_2022.day_05.shared import Move


@dataclass
class Data:
    starting_stacks: Mapping[int, list[str]]
    moves: list[Move]


class Parser(object):
    move_regex = re.compile(r"move (\d+) from (\d+) to (\d+)")

    @staticmethod
    def parse(data: str) -> Data:
        lines = Parser.input_to_lines(data)
        separator_index = lines.index("")
        stack_count = Parser.get_stack_count(lines[separator_index - 1])
        moves = [Parser.parse_move(line) for line in lines[separator_index + 1 :]]
        stacks = Parser.create_stacks(stack_count, lines[: separator_index - 1])
        return Data(starting_stacks=stacks, moves=moves)

    @staticmethod
    def input_to_lines(data: str) -> list[str]:
        lines = data.splitlines()
        while lines[0].strip() == "":
            lines = lines[1:]
        while lines[-1].strip() == "":
            lines = lines[:-1]
        return lines

    @staticmethod
    def get_stack_count(line: str) -> int:
        return int(line.split()[-1])

    @staticmethod
    def parse_move(line: str) -> Move:
        match = Parser.move_regex.search(line)
        assert match is not None
        return Move(
            count=int(match.group(1)),
            from_stack=int(match.group(2)),
            to_stack=int(match.group(3)),
        )

    @staticmethod
    def create_stacks(stack_count: int, lines: list[str]) -> Mapping[int, list[str]]:
        stacks = {i: [] for i in range(1, stack_count + 1)}
        for line in lines:
            segments = math.ceil(len(line) / 4)
            for segment_index in range(segments):
                char_index = 4 * segment_index + 1
                if char_index < len(line) and line[char_index] != " ":
                    stacks[segment_index + 1].append(line[char_index])

        return {i: l[::-1] for i, l in stacks.items()}
