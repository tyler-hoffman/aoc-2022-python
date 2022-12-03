from .shared import ABC, XYZ, Match


class Parser(object):
    @staticmethod
    def parse(input: str) -> list[Match]:
        output: list[Match] = []
        for line in input.strip().splitlines():
            a, b = line.split()
            output.append(Match(ABC.from_string(a), XYZ.from_string(b)))

        return output
