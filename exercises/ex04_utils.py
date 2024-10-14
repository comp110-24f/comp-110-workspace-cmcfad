"""EX04 List utility functions"""

__author__ = "730764947"


def all(lst: list[int], num: int) -> bool:
    """All ints in lst are num"""
    if lst == []:  # list is empty stop and false
        return False
    for elem in lst:  # cycles through each elem
        if elem != num:  # if not = stop and rtn false
            return False
    return True  # none of the above then true


def max(lst: list[int]) -> int:
    large_int: int = lst[0]
    if len(lst) == 0:
        raise ValueError("max() arg is an empty List")
    for elem in lst:
        if elem > large_int:  # if the elem is larger than 0 or last int
            large_int = elem  # set equal
    return large_int


def is_equal(lst1: list[int], lst2: list[int]) -> bool:
    if len(lst1) != len(lst2):  # checks to see if lists are the same len
        return False
    for idx in range(0, len(lst1)):  # using indexs
        if lst1[idx] != lst2[idx]:  # if current idx of elem lst1 doesn't = lst2 then F
            return False
    return True


def extend(lst1: list[int], lst2: list[int]) -> None:
    for elem in lst2:  # cycles through elem in lst2
        lst1.append(elem)  # appends it to the lst1
