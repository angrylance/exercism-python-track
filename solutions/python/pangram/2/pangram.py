import string


def is_pangram(sentence):
    """
    Checks if the provided sentence is pangram - contain each of 26 letters of english alphabet.
    Args:
    sentence(str): provided string to check
    Returns:
    bool - True of given sentence is pangram, False-if not.
    """
    ##Solution 1 - set comprehension with isalpha and string.punctuation:
    # letters = set(c.lower() for c in sentence.strip(string.punctuation) if c.isalpha())
    # return len(letters) == 26

    ## Solution 2:
    # return all(letter in sentence.lower() for letter in string.ascii_lowercase)

    ## Soltuion 3 - issubset()
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(sentence.lower())
