def reverse(text: str) -> str:
    """
    Returns reversed string.
    Args:
    text(str) - a given string to reverse
    Returns:
    str - reversed given string.
    """
    # Solution 1 - slicing:
    # return text[::-1]

    # Solution 2 - reversed built-in and "".join()
    # return "".join(reversed(text))

    # Solution 3 - range and append():
    output = []
    length = len(text) - 1
    for index in range(length, -1, -1):
        output.append(text[index])
    return "".join(output)
