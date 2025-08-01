from math import sqrt


def score(x, y) -> int:
    """
    Calculate the score for each toss in Darts game
    Args:
    x: coordinate x
    y: coordinate y
    Returns:
    int: score for toss.
    """
    distance = sqrt(x**2 + y**2)
    if distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1
    return 0
