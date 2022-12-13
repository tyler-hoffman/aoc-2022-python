import functools
from dataclasses import dataclass
from functools import cached_property

from aoc_2022.day_13.models import Element, Packet
from aoc_2022.day_13.parser import Parser

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

    def elements_in_correct_order(self, pair: tuple[Element, Element]) -> bool:
        left, right = pair

        match (left, right):
            case int(a), int(b):
                return a < b
            case list(a), list(b):
                return self.lists_in_correct_order((a, b))
            case list(a), int(b):
                return self.elements_in_correct_order((a, [b]))
            case int(a), list(b):
                return self.elements_in_correct_order(([a], b))
            case _:
                assert False, "How on earth did we get here?"

    def lists_in_correct_order(self, pair: tuple[Packet, Packet]) -> bool:
        left, right = pair
        smaller_len = min(len(left), len(right))

        for i in range(smaller_len):
            if self.elements_in_correct_order((left[i], right[i])):
                return True
            elif self.elements_in_correct_order((right[i], left[i])):
                return False

        return len(left) < len(right)

    def compare(self, left: Element, right: Element) -> int:
        if self.elements_in_correct_order((left, right)):
            return -1
        elif self.elements_in_correct_order((right, left)):
            return 1
        else:
            return 0


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
