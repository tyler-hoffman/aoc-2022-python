from dataclasses import dataclass
from typing import Union


@dataclass
class Addx:
    amount: int


@dataclass
class Noop:
    ...


Operation = Union[Addx, Noop]
