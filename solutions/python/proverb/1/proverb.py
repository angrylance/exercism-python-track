# Solution to https://exercism.org/tracks/python/exercises/proverb


def proverb(*args: str, qualifier: str = None) -> list[str]:
    """
    Given a list of arbitrary length, return the "For want a nail..."-style proverb.
    Args:
        *args (str): an input list of arbitrary length.
    Returns:
        list[str]: a constructed proverb.
    """

    def line_builder(a, b):
        """Helper function building lines."""
        return f"For want of a {a} the {b} was lost."

    # Handling special case with 0 elements
    if len(args) == 0:
        return []

    phrase = [line_builder(x, y) for x, y in zip(args, args[1:])]
    last_part = qualifier + " " + args[0] if qualifier else args[0]
    phrase.append(f"And all for the want of a {last_part}.")
    return phrase
