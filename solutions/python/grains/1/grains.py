def square(number: int) -> int:
    """
    Calculates the number of grains on a given square where the number on the next square exery time doubles.
    Args:
    number (int): the number of a square
    Returns:
    int: the number of grains on a "number"-th square.

    """
    ## Solution 1
    # if 1 <= number <= 64:
    #     return 2 ** (number - 1)
    # raise ValueError("square must be between 1 and 64")

    # #Solution 2 - recursion:
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    if number == 1:
        return 1
    if number == 2:
        return 2
    if number > 2:
        return 2 * square(number - 1)


def total() -> int:
    """
    Calculates the total number of grains on a chess board
    Returns:
    int:the total number of grains on a chess board.

    """
    return sum([square(num) for num in range(1, 65)])
