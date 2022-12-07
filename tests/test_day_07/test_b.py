from aoc_2022.day_07.b import get_solution, solve

SAMPLE_DATA = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


def test_solve():
    assert solve(SAMPLE_DATA) == 24933642


def test_my_solution():
    assert get_solution() == 10096985
