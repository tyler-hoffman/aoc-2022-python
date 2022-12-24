from aoc_2022.day_22.a import get_solution, solve

SAMPLE_DATA = """
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""


def test_solve():
    assert solve(SAMPLE_DATA) == 6032


def test_my_solution():
    assert get_solution() == 131052
