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
    word_map = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    # result = ""
    # if number % answer[0][0] == 0:
    #     result += answer[0][1]
    # if number % answer[1][0] == 0:
    #     result += answer[1][1]
    # if number % answer[2][0] == 0:
    #     result += answer[2][1]
    # if not result:
    #     return str(number)
    # return result
    result = "".join(word for div, word in word_map if number % div == 0)
    return result or str(number)
