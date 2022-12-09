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

    x_min = head.x - 1
    x_max = head.x + 1
    y_min = head.y - 1
    y_max = head.y + 1

    if max(abs(x - head.x), abs(y - head.y)) < 2:
        return tail
    elif x == head.x:
        if y < y_min:
            return Point(x, y + 1)
        elif y > y_max:
            return Point(x, y - 1)
        else:
            return tail
    elif y == head.y:
        if x < x_min:
            return Point(x + 1, y)
        elif x > x_max:
            return Point(x - 1, y)
        else:
            return tail

    elif x < head.x and y < head.y:
        return Point(x + 1, y + 1)
    elif x > head.x and y > head.y:
        return Point(x - 1, y - 1)
    elif x < head.x and y > head.y:
        return Point(x + 1, y - 1)
    elif x > head.x and y < head.y:
        return Point(x - 1, y + 1)
    else:
        return tail
