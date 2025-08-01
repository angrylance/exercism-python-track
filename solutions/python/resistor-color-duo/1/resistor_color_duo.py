LOOKUP_RESISTORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def value(colors: list) -> int:
    """
    The program takes color names as input and output a two digit number of resistance value, even if the input is more than two colors.
    Args:
        colors (list): the list of colors of bands representing resistance value
    Returns:
        int: Resistance value calculated from LOOKUP_RESISTORS using color1=N and color2=M, the result is NM.
             For example: brown and green bands will be 15.
    """

    return int("".join((str(LOOKUP_RESISTORS[value]) for value in colors[:2])))
