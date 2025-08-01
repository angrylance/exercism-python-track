def is_isogram(string_to_check: str) -> bool:
    """
    Checks if a given string is an isogram - does not contain repeated letters.
    Args:
    string_to_check(str): input string to check
    Returns:
    bool: True if a string is isogram, False-if it's not
    """
    # Solution 1 - for-loop:
    # modified_string = sorted(
    #     [letter.lower() for letter in string_to_check if letter.isalpha()]
    # )
    # for letter in range(1, len(modified_string)):
    #     if modified_string[letter] == modified_string[letter - 1]:
    #         return False
    # return True

    # Solution 2 - dictionary with counts:
    # modified_string = [letter.lower() for letter in string_to_check if letter.isalpha()]
    # counts = dict()
    # for letter in modified_string:
    #     counts[letter] = counts.get(letter, 0) + 1
    #     if counts[letter] > 1:
    #         return False
    # return True

    # Solution 3 - using sets:
    # modified_string = [letter.lower() for letter in string_to_check if letter.isalpha()]
    # return len(set(modified_string)) == len(modified_string)

    # Solution 3.1 optimized performance with one pass and early exit:
    seen = set()
    for char in string_to_check:
        if char.isalpha():
            char = char.lower()
            if char in seen:
                return False
            seen.add(char)
    return True
