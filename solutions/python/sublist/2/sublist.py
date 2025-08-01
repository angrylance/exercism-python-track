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


def is_sublist(list_one: list[int], list_two: list[int]) -> bool:
    """
    Helper function checking if list_one is sublist of list_two.
    """
    for i in range(len(list_two) - len(list_one) + 1):
        if list_two[i : i + len(list_one)] == list_one:
            return True
    return False


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
    if is_sublist(list_one, list_two):
        return SUBLIST
    if is_sublist(list_two, list_one):
        return SUPERLIST
    return UNEQUAL
