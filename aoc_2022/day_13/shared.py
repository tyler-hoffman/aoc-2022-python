from aoc_2022.day_13.models import Element, Ordering, Packet


def compare_packets(left: Packet, right: Packet) -> Ordering:
    smaller_len = min(len(left), len(right))

    for i in range(smaller_len):
        ordering = compare_elements(left[i], right[i])
        if ordering != Ordering.EQUAL:
            return ordering

    if len(left) < len(right):
        return Ordering.LESS
    elif len(left) > len(right):
        return Ordering.GREATER
    else:
        return Ordering.EQUAL


def compare_elements(left: Element, right: Element) -> Ordering:
    match (left, right):
        case int(a), int(b):
            return compare_ints(a, b)
        case list(a), list(b):
            return compare_packets(a, b)
        case list(a), int(b):
            return compare_elements(a, [b])
        case int(a), list(b):
            return compare_elements([a], b)
        case _:
            assert False, "How on earth did we get here?"


def compare_ints(left: int, right: int) -> Ordering:
    if left < right:
        return Ordering.LESS
    elif left > right:
        return Ordering.GREATER
    else:
        return Ordering.EQUAL
