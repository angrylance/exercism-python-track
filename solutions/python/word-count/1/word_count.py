# Solution to https://exercism.org/tracks/python/exercises/word-count

import re
from collections import Counter


def count_words(sentence: str) -> dict:
    """
    Calculates the frequencies of the ocuring words in a phrase.
    Args:
        sentence (str): a phrase to count words from.
    Returns:
        dict: a map of each word in the phrase.
    """
    words = re.findall(r"[a-zA-Z0-9]+(?:'[a-zA-Z0-9]+)?", sentence.lower())

    # Solution 1, Counter():
    return dict(Counter(words))

    # Solution 2, dict.get(word,0)+1
    # count = {}
    # for word in words:
    #     count[word] = count.get(word, 0) + 1
    # return count
