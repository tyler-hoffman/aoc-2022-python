from aoc_2022.day_20.a import get_solution, solve

SAMPLE_DATA = """
1
2
-3
3
-2
0
4
"""


def test_solve():
    assert solve(SAMPLE_DATA) == 3


def test_my_solution():
    assert get_solution() == 4151
