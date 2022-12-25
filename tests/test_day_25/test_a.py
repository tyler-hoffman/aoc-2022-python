from aoc_2022.day_25.a import get_solution, solve

SAMPLE_DATA = """
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122
"""


def test_solve():
    assert solve(SAMPLE_DATA) == "2=-1=0"


def test_my_solution():
    assert get_solution() == "2-121-=10=200==2==21"
