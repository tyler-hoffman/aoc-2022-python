from aoc_2022.day_08.a import get_solution, solve

SAMPLE_DATA = """
30373
25512
65332
33549
35390
"""


def test_solve():
    assert solve(SAMPLE_DATA) == 21


def test_my_solution():
    assert get_solution() == 1688
