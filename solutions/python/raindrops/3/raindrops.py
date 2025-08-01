def convert(number: int) -> str:
    """
    Converts a number into its corresponding raindrop sounds.
    If a given number:
    - is divisible by 3, add "Pling" to the result.
    - is divisible by 5, add "Plang" to the result.
    - is divisible by 7, add "Plong" to the result.
    - is not divisible by 3, 5, or 7, the result should be the number as a string.
    Args:
    number(int): Given number to check and convert
    Returns:
    str: return value based on the conditions
    """
    # Solution 1 - sequential if statements to build-up a string:
    # result = ""
    # if number % 3 == 0:
    #     result += "Pling"
    # if number % 5 == 0:
    #     result += "Plang"
    # if number % 7 == 0:
    #     result += "Plong"
    # return result or str(number)
    #
    # Solution 2 - more elegant, using .join() and generator expression:
    # word_map = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    # result = "".join(word for div, word in word_map if number % div == 0)
    # return result or str(number)

    # Solution 3 - dictionary of sounds and generator expression:
    sounds = {3: "Pling", 5: "Plang", 7: "Plong"}
    result = "".join(value for key, value in sounds.items() if number % key == 0)
    return result or str(number)
