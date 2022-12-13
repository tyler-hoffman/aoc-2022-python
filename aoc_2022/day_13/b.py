import functools
from dataclasses import dataclass
from functools import cached_property

from aoc_2022.day_13.models import Packet
from aoc_2022.day_13.parser import Parser
from aoc_2022.day_13.shared import compare_packets

EXTRA_PACKET_A: Packet = [[2]]
EXTRA_PACKET_B: Packet = [[6]]


@dataclass
class Day13PartBSolver:
    pairs: list[tuple[Packet, Packet]]

    @property
    def solution(self) -> int:
        a = self.sorted_packets.index(EXTRA_PACKET_A) + 1
        b = self.sorted_packets.index(EXTRA_PACKET_B) + 1

        return a * b

    @cached_property
    def sorted_packets(self) -> list[Packet]:
        return sorted(
            self.all_packets_plus_dividers, key=functools.cmp_to_key(self.compare)
        )

    @cached_property
    def all_packets_plus_dividers(self) -> list[Packet]:
        output: list[Packet] = [EXTRA_PACKET_A, EXTRA_PACKET_B]
        for left, right in self.pairs:
            output.append(left)
            output.append(right)
        return output

    def compare(self, left: Packet, right: Packet) -> int:
        return compare_packets(left, right).int_value


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day13PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_13/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
