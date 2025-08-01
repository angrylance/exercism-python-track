import re


def abbreviate(words: str) -> str:
    """
    Abbreviates a given string.
    Args:
        words (str): a given string to abbreaviate.
    Returns:
        str: abbreviation.
    """
    # Solution 1 - regex sub:
    # tokens = re.sub(r"-|_", " ", words).upper()
    # return "".join(word[0] for word in tokens.split())

    # Solution 2 -regex findall() - more optimal for regex that solution 1:
    # tokens = re.findall(r"[a-zA-Z']+", words)
    # return "".join(word[0] for word in tokens).upper()

    # Solution 3 - replace() + maketrans()
    normalized = words.replace("-", " ").replace("_", " ").upper().split()
    return "".join(word[0] for word in normalized)
