def factors(value: int) -> list[int]:
    """
    Returns a list of prime factors of a value number.
    Args:
        value (int): a given number to find prime factor for.
    Returns:
        list[int]: prime factors of a value number.
    """
    result = []
    div = 2
    while value > 1:
        if value % div == 0:
            value = value // div
            result.append(div)
        else:
            div += 1
    return result
