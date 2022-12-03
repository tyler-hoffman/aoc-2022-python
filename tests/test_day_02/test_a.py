from aoc_2022.day_02.a import get_solution, solve

SAMPLE_INPUT = """
A Y
B X
C Z
"""


def test_solve():
    assert solve(SAMPLE_INPUT) == 15


def test_my_solution():
    assert get_solution() == 13675
