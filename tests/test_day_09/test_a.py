from aoc_2022.day_09.a import get_solution, solve

SAMPLE_DATA = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""


def test_solve():
    assert solve(SAMPLE_DATA) == 13


def test_my_solution():
    assert get_solution() == 6284
