def append(list1: list, list2: list) -> list:
    """
    Returns concatenated list.
    """
    return list1 + list2


def concat(lists: list[list]) -> list:
    """
    Returns a single flat list, comnining all lists.
    """
    result = []
    for l in lists:
        result += l
    return result


def filter(function, list: list) -> list:
    """
    Filters the elements of the list using function as predicate.
    """
    result = []
    for element in list:
        if function(element):
            result += [element]
    return result


def length(list: list) -> int:
    """
    Returns a total number of elements in a given list.
    """
    result = 0
    for element in list:
        result += 1
    return result


def map(function, list: list) -> list:
    """
    Returns the list of the results of applying function(item) on all items.
    """
    result = []
    for element in list:
        result += [function(element)]
    return result


def foldl(function, list, initial) -> int | float:
    """
    Returns the folded (reduced) result of each item into the initial accumulator from the left.
    """
    result = initial
    for element in list:
        result = function(result, element)
    return result


def foldr(function, list, initial) -> int | float:
    """
    Returns the folded (reduced) result of each item into the initial accumulator from the right.
    """
    result = initial
    for element in list[::-1]:
        result = function(result, element)
    return result


def reverse(list: list) -> list:
    """
    Returns a list with all the original items, but in reversed order.
    """
    return list[::-1]
