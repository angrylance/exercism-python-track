from collections.abc import Iterable


def flatten(iterable: list) -> list:
    """
    Takes a nested iterable and returns flattened array.
    Args:
        iterable(list): nested input iterable.
    Returns:
        list: flattened list.
    """
    # Solution 1 with Iterable class and reversing+appending
    # flattened = []
    # stack = list(reversed(iterable))
    # while stack:
    #     current = stack.pop()
    #     if isinstance(current, Iterable):
    #         stack.extend(reversed(current))
    #     elif current is not None:
    #         flattened.append(current)
    # return flattened
    # Solution 2 - recursion:
    flattened = []
    for item in iterable:
        if isinstance(item, Iterable):
            flattened.extend(flatten(item))
        elif item is not None:
            flattened.append(item)
    return flattened
