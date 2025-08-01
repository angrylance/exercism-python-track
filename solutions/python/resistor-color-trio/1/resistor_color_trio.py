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


def label(colors):
    """
    The program takes color names as input and output a two digit number of resistance value, even if the input is more than two colors.
    Args:
        colors (list): the list of colors of bands representing resistance value
    Returns:
        int: Resistance value calculated from LOOKUP_RESISTORS using color1=N and color2=M, the result is NM. The last digit defines
             how many zeros in the end.
             For example: brown and green bands will be 15.
                          brown, green and orange will be 15000 ohms or 15 kiloohms.
    """
    band1, band2, multiplier = colors[:3]
    value = (
        LOOKUP_RESISTORS[band1] * 10 + LOOKUP_RESISTORS[band2]
    ) * 10 ** LOOKUP_RESISTORS[multiplier]
    if value >= 1000000000:
        return f"{value // 1000000000} gigaohms"
    elif value >= 1000000:
        return f"{value // 1000000} megaohms"
    elif value >= 1000:
        return f"{value // 1000} kiloohms"
    else:
        return f"{value} ohms"
