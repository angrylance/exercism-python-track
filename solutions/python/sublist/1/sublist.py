"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one: list[int], list_two: list[int]) -> int:
    """
    Checks if list_one is either equal, sublist, superlist or unequal to list_two.
    Args:
        list_one (list[int]): list to compare with list_two.
        list_two (list[int]): list to compare with list one.
    Returns:
        int: SUBLIST = 1, SUPERLIST = 2, EQUAL = 3, UNEQUAL = 4.
    """
    if list_one == list_two:
        return EQUAL

    if len(list_one) < len(list_two):
        smaller, bigger = list_one, list_two
        result_if_match = SUBLIST
    elif len(list_one) > len(list_two):
        smaller, bigger = list_two, list_one
        result_if_match = SUPERLIST
    else:
        return UNEQUAL

    for i in range(len(bigger) - len(smaller) + 1):
        if bigger[i : i + len(smaller)] == smaller:
            return result_if_match

    return UNEQUAL
