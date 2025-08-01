from collections import Counter  # Import of collections.Counter class for solution 3.


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """
    Checks and returns a list of anagrams for the word from the given candidates list.
    Args:
        word(str): a word to check for anagrams
        candidates(list[str]): list of potential anagrams
    Returns:
        list[str]: list of thec confirmed anagrams
    """
    # Solution 1 - sorting:
    # anagrams = []
    # sorted_word = sorted(word.lower())
    # for candidate in candidates:
    #     sorted_candidate = sorted(candidate.lower())
    #     if word.lower() != candidate.lower() and sorted_word == sorted_candidate:
    #         anagrams.append(candidate)
    # return anagrams

    # Solution 2 using helper function for counting chars:
    # def count_chars(some_string: str):
    #     """
    #     Helper function to count chars a given string.
    #     """
    #     counter = {}
    #     for char in some_string.lower():
    #         counter[char] = counter.get(char, 0) + 1
    #     return counter

    # anagrams = []
    # count_of_word = count_chars(word)
    # for candidate in candidates:
    #     if candidate.lower() != word.lower() and count_of_word == count_chars(
    #         candidate.lower()
    #     ):
    #         anagrams.append(candidate)
    # return anagrams

    # Solution 3, using Counter class from collections
    # anagrams = []
    # word_lower = word.lower()
    # word_counter = Counter(word_lower)
    # for candidate in candidates:
    #     candidate_lower = candidate.lower()
    #     if word_lower != candidate_lower and word_counter == Counter(candidate_lower):
    #         anagrams.append(candidate)
    # return anagrams

    # Solution 4, comprehension:
    return [
        candidate
        for candidate in candidates
        if candidate.lower() != word.lower()
        and sorted(word.lower()) == sorted(candidate.lower())
    ]
