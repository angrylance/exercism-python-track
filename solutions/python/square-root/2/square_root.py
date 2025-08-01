def square_root(number: int) -> int:
    """
    Square root implementation without use of built-ins.
    Args:
        number (int): the number to calculate the square root from.
    Returns:
        int: the resulting number.
    """
    # Solution with linear search of a number that gives number when squared:
    # for i in range(1, number + 1):
    #     if i**2 == number:
    #         return i

    # Solution with binary search of a number that gives number when squared:
    # low, high = 0, number
    # while low <= high:
    #     mid = (low + high) // 2
    #     if mid**2 == number:
    #         return mid
    #     if mid**2 > number:
    #         high = mid - 1
    #     elif mid**2 < number:
    #         low = mid + 1

    # Solution Herons's method:
    guess = number / 2
    while guess**2 != number:
        guess = 0.5 * (guess + number / guess)
    return guess
