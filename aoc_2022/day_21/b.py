from dataclasses import dataclass
from functools import cache

from aoc_2022.day_21.models import ConstantMonkey, OperationMonkey
from aoc_2022.day_21.parser import Parser
from aoc_2022.day_21.shared import Day21Solver


@dataclass(frozen=True)
class Day21PartASolver(Day21Solver):
    @property
    def solution(self) -> int:
        a = self.root.a
        b = self.root.b

        split_name, value_name = (a, b) if self.contains(a, "humn") else (b, a)
        value: int = self.get_monkey_value(value_name)

        while True:
            m = self.monkey_dict[split_name]
            match m:
                case ConstantMonkey(name="humn"):
                    return value
                case OperationMonkey(a=a, operation="+", b=b):
                    split_name, value_name = (
                        (a, b) if self.contains(a, "humn") else (b, a)
                    )
                    value -= self.get_monkey_value(value_name)
                case OperationMonkey(a=a, operation="-", b=b):
                    split_name, value_name = (
                        (a, b) if self.contains(a, "humn") else (b, a)
                    )
                    if self.contains(a, "humn"):
                        value += self.get_monkey_value(b)
                    else:
                        value -= self.get_monkey_value(a)
                        value *= -1
                case OperationMonkey(a=a, operation="*", b=b):
                    split_name, value_name = (
                        (a, b) if self.contains(a, "humn") else (b, a)
                    )
                    value //= self.get_monkey_value(value_name)
                case OperationMonkey(a=a, operation="/", b=b):
                    split_name, value_name = (
                        (a, b) if self.contains(a, "humn") else (b, a)
                    )
                    if self.contains(a, "humn"):
                        value *= self.get_monkey_value(b)
                    else:
                        raise Exception(
                            "Hopefully we don't have to handle this case rofl"
                        )
                case _:
                    assert False, "We shouldn't get here"

    @cache
    def contains(self, monkey: str, target: str) -> bool:
        m = self.monkey_dict[monkey]
        if m.name == target:
            return True
        elif isinstance(m, ConstantMonkey):
            return False
        else:
            return self.contains(m.a, target) or self.contains(m.b, target)


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
