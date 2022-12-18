from typing import Sequence


class Parser(object):
    @staticmethod
    def parse(input: str) -> Sequence[int]:
        return [-1 if x == "<" else 1 for x in input]
