def resistor_label(colors):
    """
    The program takes 1, 4, or 5 colors as input and output the correct value in ohms
    Args:
        colors (list): the list of colors of bands representing resistance value
    Returns:
        int: Resistance value calculated from LOOKUP_RESISTORS and TOLERANCE.

    """
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

    TOLERANCE = {
        "grey": "±0.05%",
        "violet": "±0.1%",
        "blue": "±0.25%",
        "green": "±0.5%",
        "brown": "±1%",
        "red": "±2%",
        "gold": "±5%",
        "silver": "±10%",
    }
    if len(colors) == 1:
        return f"{LOOKUP_RESISTORS[colors[0]]} ohms"

    if len(colors) == 4:
        band1, band2, multiplier = colors[:3]
        toler = TOLERANCE[colors[3]]
        value = (
            LOOKUP_RESISTORS[band1] * 10 + LOOKUP_RESISTORS[band2]
        ) * 10 ** LOOKUP_RESISTORS[multiplier]
        if value >= 1000000000:
            return f"{value / 1000000000:g} gigaohms {toler}"
        elif value >= 1000000:
            return f"{value / 1000000:g} megaohms {toler}"
        elif value >= 1000:
            return f"{value / 1000:g} kiloohms {toler}"
        else:
            return f"{value:g} ohms {toler}"

    if len(colors) == 5:
        band1, band2, band3, multiplier = colors[:4]
        toler = TOLERANCE[colors[4]]
        value = (
            LOOKUP_RESISTORS[band1] * 100
            + LOOKUP_RESISTORS[band2] * 10
            + LOOKUP_RESISTORS[band3]
        ) * 10 ** LOOKUP_RESISTORS[multiplier]
        if value >= 1000000000:
            return f"{value / 1000000000:g} gigaohms {toler}"
        elif value >= 1000000:
            return f"{value / 1000000:g} megaohms {toler}"
        elif value >= 1000:
            return f"{value / 1000:g} kiloohms {toler}"
        else:
            return f"{value:g} ohms {toler}"
