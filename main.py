from typing import Callable, List


def func1(f: Callable[[int], bool], collection: List[int]) -> List[int]:
    s: List[int] = []
    for item in collection:
        if f(item):
            s.append(item)
    return s


def filters(li: List) -> List:
    s = sorted(li, key=lambda x: x if x > 2 else -x)
    return s


lp = [1, 5, 8, 4, 9, 0]
z = func1(filters, lp)
print(z)
