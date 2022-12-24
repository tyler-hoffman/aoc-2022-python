from aoc_2022.day_23.a import get_solution, solve

SAMPLE_DATA = """
..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............
"""


def test_solve():
    assert solve(SAMPLE_DATA) == 110


def test_my_solution():
    assert get_solution() == 4336
