from aoc_2022.day_14.a import get_solution, solve

SAMPLE_DATA = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""


def test_solve():
    assert solve(SAMPLE_DATA) == 24


def test_my_solution():
    assert get_solution() == 793
