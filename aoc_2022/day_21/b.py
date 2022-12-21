from dataclasses import dataclass, field
from functools import cache, cached_property
from typing import Mapping

from aoc_2022.day_21.models import ConstantMonkey, Monkey, OperationMonkey
from aoc_2022.day_21.parser import Parser


@dataclass(frozen=True)
class Day21PartASolver:
    monkey_list: list[Monkey] = field(hash=False)

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

    @cached_property
    def root(self) -> OperationMonkey:
        root = self.monkey_dict["root"]
        assert isinstance(root, OperationMonkey)
        return root

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
