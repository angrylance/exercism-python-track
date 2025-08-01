import string


def is_pangram(sentence):
    """
    Checks if the provided sentence is pangram - contain each of 26 letters of english alphabet.
    Args:
    sentence(str): provided string to check
    Returns:
    bool - True of given sentence is pangram, False-if not.
    """
    letters = set(c.lower() for c in sentence.strip(string.punctuation) if c.isalpha())
    return len(letters) == 26


print(is_pangram("The quick brown fox jumps over the lazy dog."))
