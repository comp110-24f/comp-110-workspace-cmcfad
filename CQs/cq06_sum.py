"""Summing the elements of a list using different loops"""

__author__ = "730764947"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    count: float = 0.0
    while idx < len(vals):
        count += vals[idx]
        idx += 1
    return count


def f_sum(vals: list[float]) -> float:
    count: float = 0.0
    for num in vals:
        count += num
    return count


def f_range_sum(vals: list[float]) -> float:
    count: float = 0.0
    for idx in range(0, len(vals)):
        count += vals[idx]
    return count
