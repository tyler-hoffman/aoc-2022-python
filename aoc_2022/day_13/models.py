from __future__ import annotations

from enum import Enum
from typing import Union

Element = Union[int, list["Element"]]
Packet = list[Element]


class Ordering(Enum):
    LESS = -1
    EQUAL = 0
    GREATER = 1

    @property
    def int_value(self) -> int:
        return self.value
