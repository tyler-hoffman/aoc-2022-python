from aoc_2022.day_03.shared import Rucksack


class Parser(object):
    @staticmethod
    def parse(s: str) -> list[Rucksack]:
        return [Rucksack(line) for line in s.strip().splitlines()]
