def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    # Solution 1 - for loop:
    divs = []
    # Checking only up to the half of N, because everything above N/2 won't be a divisor of N.
    for _ in range(1, int(number / 2) + 1):
        if number % _ == 0:
            divs.append(_)
    if sum(divs) == number:
        return "perfect"
    if sum(divs) > number:
        return "abundant"
    if sum(divs) < number:
        return "deficient"
    # Solution 2
