from dataclasses import dataclass

from aoc_2022.day_11.models import Monkey
from aoc_2022.day_11.parser import Parser


@dataclass
class Day11PartASolver:
    monkeys: list[Monkey]

    @property
    def solution(self) -> int:
        for _ in range(20):
            for m in self.monkeys:
                while m.items:
                    item = m.items.pop(0)
                    item = m.operation(item) // 3
                    if item % m.divisible_test == 0:
                        self.monkeys[m.on_true].items.append(item)
                    else:
                        self.monkeys[m.on_false].items.append(item)
                    m.yeets += 1
        yeets = sorted([m.yeets for m in self.monkeys])
        return yeets[-1] * yeets[-2]


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day11PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_11/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
