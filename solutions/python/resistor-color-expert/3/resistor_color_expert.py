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


def compute_resistance(digits_colors: list[str], multiplier_color: str) -> int:
    """
    Helper function that calculates the resistance value of the resistor.
    Args:
        digits_colors(list[str]): the list of colors of bands encoding the resistance value of the resistor
        multiplier_color(str): the last band which color represents the multiplier for the value of the resitance value.
    Returns:
        int: Numeric resistance value
    """
    digits = int("".join(str(LOOKUP_RESISTORS[color]) for color in digits_colors))
    multiplier = 10 ** LOOKUP_RESISTORS[multiplier_color]
    return digits * multiplier


def resistance_output_formatter(resistance_value: int, tolerance_color: str) -> str:
    """
    Helper function that returns formated resistance in SI value with tolerance %.
    Args:
        resistance_value(int):value calculated by compute_resistance().
        tolerance_color: tolerance value derived from TOLERANCE.
    Returns:
        str: String with resistance value in SI with % of tolerance.

    """
    tolerance = TOLERANCE.get(tolerance_color)
    suffix = ""
    if resistance_value >= 1000000000:
        resistance_value = resistance_value / 1000000000
        suffix = "giga"
    elif resistance_value >= 1000000:
        resistance_value = resistance_value / 1000000
        suffix = "mega"
    elif resistance_value >= 1000:
        resistance_value = resistance_value / 1000
        suffix = "kilo"
    return f"{resistance_value:g} {suffix}ohms" + (f" {tolerance}" if tolerance else "")


def resistor_label(colors: list[str]) -> str:
    """
    The program takes 1, 4, or 5 colors as input and output the correct value in ohms
    Args:
        colors (list): the list of colors of bands representing resistance value
    Returns:
        int: Resistance value calculated from LOOKUP_RESISTORS and TOLERANCE.

    """
    if len(colors) == 1:
        resistance = LOOKUP_RESISTORS[colors[0]]
        return resistance_output_formatter(resistance, None)
    if len(colors) == 4:
        resistance = compute_resistance(colors[:2], colors[2])
        return resistance_output_formatter(resistance, colors[3])
    if len(colors) == 5:
        resistance = compute_resistance(colors[:3], colors[3])
        return resistance_output_formatter(resistance, colors[4])
