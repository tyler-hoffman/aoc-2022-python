from aoc_2022.day_12.a import get_solution, solve

SAMPLE_DATA = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


def test_solve():
    assert solve(SAMPLE_DATA) == 31


def test_my_solution():
    assert get_solution() == 352
