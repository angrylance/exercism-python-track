from string import ascii_uppercase


def rows(letter: str) -> list[str]:
    """
    Returns rows in a diamond shape.
    Args:
        letter (str): letter of the alphabet to place in the widest place of the shape.
    Returns:
        list[str]: number of strings to form a diamond shape.
    """
    pos = ascii_uppercase.index(letter.upper())
    result = []

    for i in range(pos + 1):
        letter = ascii_uppercase[i]
        outer = pos - i
        if i == 0:
            line = outer * " " + letter + outer * " "
        else:
            inner = 2 * i - 1
            line = outer * " " + letter + inner * " " + letter + outer * " "
        result.append(line)

    return result + result[-2::-1]
