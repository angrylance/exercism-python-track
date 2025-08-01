def square_of_sum(number: int) -> int:
    """
    Returns a square of sum from 1 to number.
    Args:
        number(int): the number up to which to summarize.
    Returns:
        int: square of sum.
    """
    # Solution 1 sum,range, **
    # return (sum(range(1, number + 1))) ** 2
    # Solution 2 math formulas for square of sum:
    return (number * (number + 1) / 2) ** 2


def sum_of_squares(number: int) -> int:
    """
    Returns a sum of squares of numbers from 1 to number.
    Args:
        number(int): the number up to which to calculate squares and summarize
    Returns:
        int: sum of squares
    """
    # Solution 1 sum+map+lambda
    # return sum(map(lambda x: x**2, range(1, number + 1)))
    # Solution 2, faster than 1 - list comprehension
    # return sum([x**2 for x in range(1, number + 1)])
    # Solution 3 math formulas for sum of squares:
    return number * (number + 1) * (2 * number + 1) / 6


def difference_of_squares(number: int) -> int:
    """
    Returns the difference between the square of the sum and the sum of the squares of the first N natural numbers.
    Args:
        number(int): the number of first natural numbers to calculate the difference of squares for.
    Returns:
        int: the difference between the square of the sum and the sum of the squares.
    """
    return square_of_sum(number) - sum_of_squares(number)
