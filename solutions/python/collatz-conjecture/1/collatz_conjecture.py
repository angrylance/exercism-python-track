def steps(number: int) -> int:
    """
    Calculates the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture.
    Args:
    number(int): initial number
    Returns:
    int: number of steps required to reach 1.
    """
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    # Solution 1- while loop:
    # steps = 0
    # while number != 1:
    #     if number % 2 == 0:
    #         number = number // 2
    #     else:
    #         number = number * 3 + 1
    #     steps += 1
    # return steps

    # Solution 2 - ternary operator:
    # steps = 0
    # while number != 1:
    #     number = number // 2 if number % 2 == 0 else number * 3 + 1
    #     steps += 1
    # return steps

    # Solution 3 - recursion:
    # if number == 1:
    #     return 0
    # if number % 2 == 0:
    #     return 1 + steps(number // 2)
    # else:
    #     return 1 + steps(number * 3 + 1)
