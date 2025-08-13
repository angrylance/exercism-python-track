# Solution to https://exercism.org/tracks/python/exercises/transpose

from itertools import zip_longest


def transpose(text: str) -> str:
    """
    Transpose the given string. If the input has rows of different lengths,
    this is to be solved as follows: Pad to the left with spaces. Don't pad to the right.
    Args:
        text (str): a string to transpose.
    Returns:
        str: transposed string.
    """
    padded = zip_longest(*text.splitlines(), fillvalue="$")
    return "\n".join("".join(char).rstrip("$").replace("$", " ") for char in padded)
