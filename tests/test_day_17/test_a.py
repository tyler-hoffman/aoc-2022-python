from aoc_2022.day_17.a import get_solution, solve

SAMPLE_DATA = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"


def test_solve():
    assert solve(SAMPLE_DATA) == 3068


def test_my_solution():
    assert get_solution() == 3098
