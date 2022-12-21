from aoc_2022.day_21.a import get_solution, solve

SAMPLE_DATA = """
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
"""


def test_solve():
    assert solve(SAMPLE_DATA) == 152


def test_my_solution():
    assert get_solution() == 158661812617812
