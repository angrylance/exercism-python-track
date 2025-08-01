def check_if_triangle(sides: list) -> bool:
    """
    Checks if the given sides form triangle.

    Args:
    sides (list): list of 3 sides length

    Returns:
    bool:  True if the figure is a triangle, False - if it's not.
    """

    a, b, c = sides
    non_zero_sides = [a > 0, b > 0, c > 0]
    triangle_inequality = [a + b >= c, b + c >= a, a + c >= b]
    return all(non_zero_sides) and all(triangle_inequality)


def equilateral(sides: list) -> bool:
    """
    Determine if the the given sides form an equilateral triangle

    Args:
    sides (list): List of 3 sides length

    Returns:
    bool: True if the triangle is equilateral, False - if not, or if it's not a triangle
    """
    if check_if_triangle(sides):
        a, b, c = sides
        return a == b and b == c
    return False


def isosceles(sides: list) -> bool:
    """
    Determine if the the given sides form an isosceles triangle
    Args:
    sides (list): List of 3 sides length

    Returns:
    bool: True if the triangle is isosceles, False - if not, or if it's not a triangle
    """
    if check_if_triangle(sides):
        a, b, c = sides
        return a == b or b == c or a == c
    return False


def scalene(sides: list) -> bool:
    """
    Determine if the the given sides form an scalene triangle

    Args:
    sides (list): List of 3 sides length

    Returns:
    bool: True if the triangle is scalene, False - if not, or if it's not a triangle
    """
    if check_if_triangle(sides):
        a, b, c = sides
        return not (a == b or b == c or a == c)
    return False
