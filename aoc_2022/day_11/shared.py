from abc import ABC, abstractmethod
from dataclasses import dataclass

from aoc_2022.day_11.models import Monkey


@dataclass
class Day11Solver(ABC):
    monkeys: list[Monkey]
    rounds: int

    @property
    def solution(self) -> int:
        for _ in range(self.rounds):
            for m in self.monkeys:
                while m.items:
                    item = m.items.pop(0)
                    item = m.operation(item)
                    item = self.manager_worry_level(item)
                    if item % m.divisible_test == 0:
                        self.monkeys[m.on_true].items.append(item)
                    else:
                        self.monkeys[m.on_false].items.append(item)
                    m.yeets += 1
        yeets = sorted([m.yeets for m in self.monkeys])
        return yeets[-1] * yeets[-2]

    @abstractmethod
    def manager_worry_level(self, worry_level: int) -> int:
        ...
