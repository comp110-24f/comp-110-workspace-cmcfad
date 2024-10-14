"""Coordinates for CQ04"""

__author__ = "730764947"


def get_coords(xs: str, ys: str) -> None:
    index_x: int = 0
    while index_x < len(xs):
        index_y: int = 0
        while index_y < len(ys):
            print("(" + xs[index_x] + "," + ys[index_y] + ")")
            index_y += 1
        index_x += 1
