from functools import reduce  # Import for reduce() - solution 2


def is_armstrong_number(number: int) -> bool:
    """
    Checks if the gives number is an armstrong number - https://en.wikipedia.org/wiki/Narcissistic_number
    Args:
    number(int): nunber to check
    Returns:
    bool: True if the given number is an armstrong number, False - if not.
    """
    # # Soution 1 - comprehensions and map():
    # chars = [int(char) for char in str(number)]
    # answer = sum(map(lambda x: x ** len(chars), chars))
    # return answer == number

    # Solution 2 - reduce():
    chars = [int(char) for char in str(number)]
    power = len(chars)
    answer = reduce(lambda acc, digit: acc + digit**power, chars, 0)
    return answer == number
