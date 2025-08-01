def slices(series: str, length: int) -> list[int]:
    """
    Outputs all the contiguous substrings of length in that string in the order that they appear.
    Args:
        series (str): given string to check.
        length (int): length of the substrings.
    Returns:
        list[int]: list of contiguous substrings in the order they appear.
    """
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if not series:
        # if the series provided is empty.
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    # Solutions 1, for loop:
    # substrings = []
    # for i in range(len(series) - length + 1):
    #     substrings.append(series[i : i + length])
    # return substrings

    # Solution 2, list comprehension:
    return [series[i : i + length] for i in range(len(series) - length + 1)]
