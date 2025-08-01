from itertools import groupby
import re


def encode(string: str) -> str:
    """
    Encodes a given string using Running Length encoding(RLE).
    Args:
        string (str): a string to encode with RLE.
    Returns:
        str: encoded string.
    """
    # Solution 1, for loop:
    # if not string:
    #     return ""
    # result = []
    # current = string[0]
    # count = 0
    # for letter in string:
    #     if letter == current:
    #         count += 1
    #     else:
    #         count_str = count if count > 1 else ""
    #         result.append(f"{count_str}{current}")
    #         current, count = letter, 1
    # count_str = count if count > 1 else ""
    # result.append(f"{count if count>1 else ''}{current}")
    # return "".join(result)
    # Solution 2 groupby
    # result = []
    # for k, g in groupby(string):
    #     group_list = list(g)
    #     count = len(group_list) if len(group_list) > 1 else ""
    #     result.append(f"{count}{k}")
    # return "".join(result)
    # Solution 3, groupby+comprehension:
    groupby_list = [(len(list(g)), k) for k, g in groupby(string)]
    return "".join(str(g) + k if g > 1 else k for g, k in groupby_list)


def decode(string: str) -> str:
    """
    Decodes a given string encoded with Run-length encoding(RLE).
    Args:
        string (str): a string to decode.
    Returns:
        str: decoded string.
    """
    # result, num = [], ""
    # for ch in string:
    #     if ch.isdigit():
    #         num += ch
    #     else:
    #         if num:
    #             result.append(f"{int(num)*ch}")
    #         else:
    #             result.append(ch)
    #         num = ""
    # return "".join(result)
    # Solution 2 with re.findall()
    return "".join(
        int(count) * letter if count else letter
        for count, letter in re.findall(r"(\d*)(\D)", string)
    )
