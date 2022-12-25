from dataclasses import dataclass
from functools import cached_property
from typing import Mapping

from aoc_2022.day_25.parser import Parser


@dataclass
class Day25PartASolver:
    snafu_lines: list[str]

    @property
    def solution(self) -> str:
        total = sum(self.decimal_lines)
        return self.decimal_to_snafu_2(total)

    @property
    def decimal_lines(self) -> list[int]:
        return [self.snafu_to_decimal(line) for line in self.snafu_lines]

    def snafu_to_decimal(self, value: str) -> int:
        output = 0
        for index, ch in enumerate(value[::-1]):
            multiplier = 5**index
            output += multiplier * self.shafu_to_decimal_map[ch]
        return output

    def decimal_to_snafu_2(self, value: int) -> str:
        keys = ["=", "-", "0", "1"]
        keys_reversed = keys[::-1]
        current = "2"
        while self.snafu_to_decimal(current) < value:
            current += "2"

        digits = "2" * (len(current))
        for i in range(len(digits)):
            for k in keys_reversed:
                new_digits = digits[:i] + k + digits[i + 1 :]
                as_decimal = self.snafu_to_decimal(new_digits)
                if as_decimal == value:
                    return new_digits
                elif as_decimal < value:
                    break
                else:
                    digits = new_digits
        assert False, "Better not get here"

    def decimal_to_snafu(self, value: int) -> str:
        chars = set(self.shafu_to_decimal_map.keys())
        states = {x for x in chars}
        while True:
            for s in states:
                if self.snafu_to_decimal(s) == value:
                    return s
            # didn't get one
            new_states: set[str] = set()
            for s in states:
                for ch in chars:
                    new_states.add(s + ch)
            states = new_states

    @cached_property
    def shafu_to_decimal_map(self) -> Mapping[str, int]:
        return {
            "0": 0,
            "1": 1,
            "2": 2,
            "-": -1,
            "=": -2,
        }

    @cached_property
    def decimal_to_snafu_map(self) -> Mapping[int, str]:
        return {v: k for k, v in self.shafu_to_decimal_map.items()}

    @cached_property
    def adjusted_decimal_to_snafu_map(self) -> Mapping[int, str]:
        return {k % 5: v for k, v in self.decimal_to_snafu_map.items()}


def solve(input: str) -> str:
    data = Parser.parse(input)
    solver = Day25PartASolver(data)

    return solver.solution


def get_solution() -> str:
    with open("aoc_2022/day_25/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
