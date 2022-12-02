from .shared import Match, Selection


class Parser(object):
    @staticmethod
    def parse(input: str) -> list[Match]:
        output: list[Match] = []
        for line in input.strip().splitlines():
            a, b = line.split()
            output.append(Match(Selection.from_abc(a), Selection.from_xyz(b)))

        return output
