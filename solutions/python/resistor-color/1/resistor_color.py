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


def color_code(color: str) -> int:
    """
    Returns the resistance value by the given resistor color
    Args:
        color(str): given color of the resistor
    Returns:
        int: resistor value
    """
    return LOOKUP_RESISTORS[color]


def colors() -> list:
    """
    Returns all possible resistor colors.
    """
    return list(LOOKUP_RESISTORS.keys())
