from dataclasses import dataclass
from typing import Union


@dataclass
class Addx:
    amount: int


@dataclass
class Noop:
    ...


Instruction = Union[Addx, Noop]


@dataclass(frozen=True)
class State:
    t: int
    x: int

    @property
    def signal_strength(self) -> int:
        return self.t * self.x
