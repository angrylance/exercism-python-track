# Solution to https://exercism.org/tracks/python/exercises/eliuds-eggs


def egg_count(display_value: int) -> int:
    """Return the number of set bits (1s) in the binary representation.
    Args:
        display_value (int): decimal number to convert to binary
    Returns:
        int: number of 1s in the binary representation of the given value.
    """
    # Solution 1 bin().count():
    return bin(display_value).count("1")

    # Solution 2 f-string +count():
    # return f"{display_value:b}".count("1")
