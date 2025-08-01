import re
import string


def abbreviate(words: str) -> str:
    """
    Abbreviates a given string.
    Args:
        words (str): a given string to abbreaviate.
    Returns:
        str: abbreviation.
    """
    # Solution 1 - regex:
    # sep_normaliazed = re.sub(r"-|_", " ", words)
    # tokens = re.sub(r"[^a-zA-Z\s]", "", sep_normaliazed)
    # return "".join(word[0].upper() for word in tokens.split())

    # Solution 2 - replace() + maketrans()
    sep_normalized = words.replace("-", " ").replace("_", " ")
    cleaned = sep_normalized.translate(str.maketrans("", "", string.punctuation))
    return "".join(word[0].upper() for word in cleaned.split())
