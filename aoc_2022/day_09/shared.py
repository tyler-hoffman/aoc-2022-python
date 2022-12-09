from aoc_2022.day_09.models import Point


def move_knot_direction(current: Point, direction: str) -> Point:
    match direction:
        case "R":
            return Point(current.x + 1, current.y)
        case "L":
            return Point(current.x - 1, current.y)
        case "U":
            return Point(current.x, current.y + 1)
        case "D":
            return Point(current.x, current.y - 1)
        case _:
            assert False, "Invalid direction"


def move_knot_to_other_knot(head: Point, tail: Point) -> Point:
    x = tail.x
    y = tail.y

    y_diff = tail.y - head.y
    x_diff = tail.x - head.x

    if max(abs(x_diff), abs(y_diff)) < 2:
        return tail
    if x_diff == 0 and y_diff < 1:
        return Point(x, y + 1)
    elif x_diff == 0 and y_diff > 1:
        return Point(x, y - 1)
    elif y_diff == 0 and x_diff < 1:
        return Point(x + 1, y)
    elif y_diff == 0 and x_diff > 1:
        return Point(x - 1, y)
    elif x_diff < 0 and y_diff < 0:
        return Point(x + 1, y + 1)
    elif x_diff > 0 and y_diff > 0:
        return Point(x - 1, y - 1)
    elif x_diff < 0 and y_diff > 0:
        return Point(x + 1, y - 1)
    elif x_diff > 0 and y_diff < 0:
        return Point(x - 1, y + 1)
    else:
        assert False, "we shouldn't get here"
