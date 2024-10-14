"""Mutating functions"""

__author__ = "730764947"


def manual_append(lists: list[int], num_append: int) -> None:
    lists.append(num_append)


def double(lists: list[int]) -> None:
    index: int = 0
    while index < len(lists):
        lists[index] = lists[index] * 2  # replaces at index with current * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)  # list 1 will be the same, list 2 will be doubled
# didnt do that they were both doubled
