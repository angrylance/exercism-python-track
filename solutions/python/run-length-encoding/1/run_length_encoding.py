def encode(string: str) -> str:
    """
    Encodes a given string using Running Length encoding(RLE).
    Args:
        string (str): a string to encode with RLE.
    Returns:
        str: encoded string.
    """
    if not string:
        return ""
    result = []
    current = string[0]
    count = 0
    for letter in string:
        if letter == current:
            count += 1
        else:
            count_str = count if count > 1 else ""
            result.append(f"{count_str}{current}")
            current, count = letter, 1
    count_str = count if count > 1 else ""
    result.append(f"{count if count>1 else ''}{current}")
    return "".join(result)


def decode(string: str) -> str:
    """
    Decodes a given string encoded with Run-length encoding(RLE).
    Args:
        string (str): a string to decode.
    Returns:
        str: decoded string.
    """
    result, num = [], ""
    for ch in string:
        if ch.isdigit():
            num += ch
        else:
            if num:
                result.append(f"{int(num)*ch}")
            else:
                result.append(ch)
            num = ""
    return "".join(result)
