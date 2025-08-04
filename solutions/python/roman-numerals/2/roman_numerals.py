# Solution to https://exercism.org/tracks/python/exercises/roman-numerals

roman_map = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
]


def roman(number: int) -> str:
    """
    Converts a number from Arabic numerals to Roman numerals.
    Args:
        number (int): number in Arabic numerals.
    Returns:
        str: the same number in Roman numerals.
    """
    if number < 1 or number > 3999:
        raise ValueError("The number is out of range.")
    roman_numerals = []
    for letter, value in roman_map:
        while number >= value:
            roman_numerals.append(letter)
            number -= value
    return "".join(roman_numerals)
