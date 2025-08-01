def append(list1: list, list2: list) -> list:
    """
    Returns concatenated list.
    """
    return list1 + list2


def concat(lists: list[list]) -> list:
    """
    Returns a single flat list, comnining all lists.
    """
    # Solution 1, for-loop:
    # result = []
    # for l in lists:
    #     result += l
    # return result

    # Solution 2 list comprehension:
    return [x for lst in lists for x in lst]


def filter(function, list: list) -> list:
    """
    Filters the elements of the list using function as predicate.
    """
    # Solution 1, for-loop:
    # result = []
    # for element in list:
    #     if function(element):
    #         result += [element]
    # return result

    # Solution 2, list comprehension:
    return [x for x in list if function(x)]


def length(list: list) -> int:
    """
    Returns a total number of elements in a given list.
    """
    # Solution 1, for-loop:
    # result = 0
    # for element in list:
    #     result += 1
    # return result

    # Solution 2, sum(generator):
    return sum(1 for x in list)


def map(function, list: list) -> list:
    """
    Returns the list of the results of applying function(item) on all items.
    """
    # Solution 1, for-loop:
    # result = []
    # for element in list:
    #     result += [function(element)]
    # return result

    # Solution 2, list comprehension:
    return [function(element) for element in list]


def foldl(function, list, initial) -> any:
    """
    Returns the folded (reduced) result of each item into the initial accumulator from the left.
    """
    result = initial
    for element in list:
        result = function(result, element)
    return result


def foldr(function, list, initial) -> any:
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
