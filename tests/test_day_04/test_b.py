from aoc_2022.day_04.b import get_solution, solve

SAMPLE_INPUT = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def test_solve():
    assert solve(SAMPLE_INPUT) == 4


def test_my_solution():
    assert get_solution() == 924
