from typing import Collection, Hashable, TypeVar

_T = TypeVar("_T", bound=Hashable)


def frequency_map(values: Collection[_T]) -> dict[_T, int]:
    output: dict[_T, int] = {}
    for x in values:
        if x not in output:
            output[x] = 0
        output[x] += 1
    return output
