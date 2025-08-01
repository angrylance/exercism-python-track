def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    # Solution 1 - for loop:
    # Checking only up to the half of N, because everything above N//2 won't be a divisor of N.
    div_sum = sum(i for i in range(1, number // 2 + 1) if number % i == 0)
    if div_sum == number:
        return "perfect"
    if div_sum > number:
        return "abundant"
    return "deficient"
