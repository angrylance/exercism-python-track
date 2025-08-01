from math import isqrt


def prime(number: int) -> int:
    """
    Returns the n-th(number-th) prime number
    Args:
        number (int): the sequential number of the prime number.
    Returns:
        int: n-th prime number.
    """
    if number <= 0:
        raise ValueError("there is no zeroth prime")
    prime_list = [2]
    initial = 3
    while len(prime_list) < number:
        prime = True
        for i in range(2, isqrt(initial) + 1):
            if initial % i == 0:
                prime = False
                break
        if prime:
            prime_list.append(initial)
        initial += 2
    return prime_list[-1]
