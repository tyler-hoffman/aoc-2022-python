from dataclasses import dataclass

from aoc_2022.day_13.models import Ordering, Packet
from aoc_2022.day_13.parser import Parser
from aoc_2022.day_13.shared import compare_packets


@dataclass
class Day13PartASolver:
    pairs: list[tuple[Packet, Packet]]

    @property
    def solution(self) -> int:
        output = 0
        for i, (left, right) in enumerate(self.pairs):
            if compare_packets(left, right) == Ordering.LESS:
                output += i + 1
        return output


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day13PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_13/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
