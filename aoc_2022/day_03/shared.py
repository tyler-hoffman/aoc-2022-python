import string
from dataclasses import dataclass
from functools import cached_property
from typing import Mapping

ALL_ITEM_TYPES = string.ascii_lowercase + string.ascii_uppercase

CHAR_PRIORITY_MAP: Mapping[str, int] = {
    ch: i + 1 for i, ch in enumerate(ALL_ITEM_TYPES)
}


@dataclass
class Rucksack:
    contents: str

    @cached_property
    def first_half(self) -> str:
        return self.contents[: self.half_length]

    @cached_property
    def second_half(self) -> str:
        return self.contents[self.half_length :]

    @cached_property
    def half_length(self) -> int:
        return len(self.contents) // 2
