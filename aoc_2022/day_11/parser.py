import math
from typing import Callable

from aoc_2022.day_11.models import Monkey


class Parser(object):
    @staticmethod
    def parse(input: str) -> list[Monkey]:
        lines = input.strip().splitlines()
        count = math.ceil(len(lines) / 7)

        output: list[Monkey] = []
        for i in range(count):
            monkey_start = i * 7
            output.append(
                Monkey(
                    index=0,
                    items=Parser.items(lines[monkey_start + 1]),
                    operation=Parser.operation(lines[monkey_start + 2]),
                    divisible_test=Parser.last_int(lines[monkey_start + 3]),
                    on_true=Parser.last_int(lines[monkey_start + 4]),
                    on_false=Parser.last_int(lines[monkey_start + 5]),
                )
            )

        return output

    @staticmethod
    def items(line: str) -> list[int]:
        items = line.split(": ")[1]
        return [int(x) for x in items.split(",")]

    @staticmethod
    def operation(line: str) -> Callable[[int], int]:
        parts = line[23:].split()
        operand = parts[1]

        match parts[0]:
            case "+":
                return lambda num: num + (num if operand == "old" else int(operand))
            case "*":
                return lambda num: num * (num if operand == "old" else int(operand))
            case _:
                assert False, "Invalid operator"

    @staticmethod
    def last_int(line: str) -> int:
        return int(line.split()[-1])
