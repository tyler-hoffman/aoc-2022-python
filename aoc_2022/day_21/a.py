from dataclasses import dataclass
from functools import cached_property
from typing import Mapping

from aoc_2022.day_21.parser import Parser
from tests.test_day_21.models import ConstantMonkey, Monkey, OperationMonkey


@dataclass
class Day21PartASolver:
    monkey_list: list[Monkey]

    @property
    def solution(self) -> int:
        return self.get_monkey_value("root")

    def get_monkey_value(self, name: str) -> int:
        m = self.monkey_dict[name]

        match m:
            case ConstantMonkey(value=value):
                return value
            case OperationMonkey(a=a, operation=operation, b=b):
                match operation:
                    case "+":
                        return self.get_monkey_value(a) + self.get_monkey_value(b)
                    case "-":
                        return self.get_monkey_value(a) - self.get_monkey_value(b)
                    case "*":
                        return self.get_monkey_value(a) * self.get_monkey_value(b)
                    case "/":
                        return self.get_monkey_value(a) // self.get_monkey_value(b)
                    case _:
                        assert False

    @cached_property
    def monkey_dict(self) -> Mapping[str, Monkey]:
        return {m.name: m for m in self.monkey_list}


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day21PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2022/day_21/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
