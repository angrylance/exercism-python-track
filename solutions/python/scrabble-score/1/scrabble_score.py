# Solution to https://exercism.org/tracks/python/exercises/scrabble-score

# Using direct lookup table as constant for better performance:
LETTER_SCORES = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10,
}


def score(word: str) -> int:
    """
    Computes a word's Scrabble score by summing the values of its letters.
    Args:
        word (str): a word to calculate score.
    Returns:
        int: word's Scrabble score.
    """
    # Solution 1, for-loop:
    # score = 0
    # for letter in word.upper():
    #     score += LETTER_SCORES.get(letter, 0)
    # return score

    # Solution 2, sum(generator):
    return sum(LETTER_SCORES.get(letter, 0) for letter in word.upper())
