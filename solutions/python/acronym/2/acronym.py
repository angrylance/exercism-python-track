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
    # Solution 1 - regex sub:
    # sep_normaliazed = re.sub(r"-|_", " ", words).upper()
    # tokens = re.sub(r"[^a-zA-Z\s]", "", sep_normaliazed)
    # return "".join(word[0] for word in tokens.split())

    # Solution 3 -regex findall()
    tokens = re.findall(r"[a-zA-Z']+", words)
    return "".join(word[0] for word in tokens).upper()
    # Solution 2 - replace() + maketrans()
    # sep_normalized = words.replace("-", " ").replace("_", " ").upper()
    # cleaned = sep_normalized.translate(str.maketrans("", "", string.punctuation))
    # return "".join(word[0] for word in cleaned.split())
