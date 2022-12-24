import pytest
from aoc_2022.day_19.b import get_solution, solve
from aoc_2022.day_19.parser import Parser
from aoc_2022.day_19.shared import QualityChecker

SAMPLE_DATA = """
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
"""  # noqa: E501


@pytest.mark.parametrize(
    "index, expected",
    [
        (0, 56),
        (1, 62),
    ]
)
def test_quality_checkers(index: int, expected: int):
    blueprints = Parser.parse(SAMPLE_DATA)
    checker = QualityChecker(blueprints[index], 32)

    assert checker.max_geodes == expected


# def test_my_solution():
#     solution = get_solution()
#     assert solution > 28710
#     assert solution == -1
