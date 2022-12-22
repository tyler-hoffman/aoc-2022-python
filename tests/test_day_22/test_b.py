from aoc_2022.day_22.b import get_solution, solve

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
    assert solve(SAMPLE_DATA) == 5031


def test_my_solution():
    solution = get_solution()
    assert solution == 4578
