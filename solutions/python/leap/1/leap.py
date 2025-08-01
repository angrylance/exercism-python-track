def leap_year(year: int) -> bool:
    """
    Calculates if the given year is the leap year.

    Args:
    year (int) - year

    Returns:
    bool - True if it's leap year, False -if it's not.
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
