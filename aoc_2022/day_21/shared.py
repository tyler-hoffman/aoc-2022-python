from dataclasses import dataclass, field
from functools import cached_property
from typing import Mapping

from aoc_2022.day_21.models import ConstantMonkey, Monkey, OperationMonkey


@dataclass(frozen=True)
class Day21Solver:
    monkey_list: list[Monkey] = field(hash=False)

    @property
    def solution(self) -> int:
        self.monkey_dict["root"]
        return self.get_monkey_value("root")

    def get_monkey_value(self, name: str) -> int:
        m = self.monkey_dict[name]

        match m:
            case ConstantMonkey(value=value):
                return value
            case OperationMonkey(a=a, operation="+", b=b):
                return self.get_monkey_value(a) + self.get_monkey_value(b)
            case OperationMonkey(a=a, operation="-", b=b):
                return self.get_monkey_value(a) - self.get_monkey_value(b)
            case OperationMonkey(a=a, operation="*", b=b):
                return self.get_monkey_value(a) * self.get_monkey_value(b)
            case OperationMonkey(a=a, operation="/", b=b):
                return self.get_monkey_value(a) // self.get_monkey_value(b)
            case _:
                assert False

    @cached_property
    def root(self) -> OperationMonkey:
        root = self.monkey_dict["root"]
        assert isinstance(root, OperationMonkey)
        return root

    @cached_property
    def monkey_dict(self) -> Mapping[str, Monkey]:
        return {m.name: m for m in self.monkey_list}
