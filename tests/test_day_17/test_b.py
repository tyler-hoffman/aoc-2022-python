from aoc_2022.day_17.b import get_solution, solve

SAMPLE_DATA = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"


def test_solve():
    # why does this fail???
    assert solve(SAMPLE_DATA) == 1514285714288


def test_my_solution():
    assert get_solution() == 1525364431487
