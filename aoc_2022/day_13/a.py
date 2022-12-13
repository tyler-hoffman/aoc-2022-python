from dataclasses import dataclass

from aoc_2022.day_13.models import Element, Packet
from aoc_2022.day_13.parser import Parser


@dataclass
class Day13PartASolver:
    pairs: list[tuple[Packet, Packet]]

    @property
    def solution(self) -> int:
        output = 0
        for i, pair in enumerate(self.pairs):
            if self.elements_in_correct_order(pair):
                output += i + 1
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
