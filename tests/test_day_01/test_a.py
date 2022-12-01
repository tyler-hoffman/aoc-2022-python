from aoc_2022.day_01.a import get_solution, solve

SAMPLE_INPUT = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def test_solve():
    assert solve(SAMPLE_INPUT) == 24000


def test_my_solution():
    assert get_solution() == 68923
