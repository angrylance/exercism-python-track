import string


def rotate(text: str, key: int) -> str:
    """
    Applies a Caesar (ROT) cipher to a string.
    Args:
        text (str): The string to be encrypted.
        key (int): The number of positions to rotate each letter.
    Returns:
        str: The encrypted string after applying the cipher.
    """
    # Solution 1 with for-loop:
    # phrase = []
    # for letter in text:
    #     if letter.isalpha():
    #         if 65 <= ord(letter) <= 90:
    #             phrase.append(chr(65 + (ord(letter) - 65 + key) % 26))
    #         elif 97 <= ord(letter) <= 122:
    #             phrase.append(chr(97 + (ord(letter) - 97 + key) % 26))
    #     else:
    #         phrase.append(letter)
    # return "".join(phrase)

    # Solution 2 with maketrans() and string.ascii_lowercase and string.ascii_uppercase:
    lower_case_alphabet = string.ascii_lowercase
    upper_case_alphabet = string.ascii_uppercase
    rotated_lower_case = lower_case_alphabet[key:] + lower_case_alphabet[:key]
    rotated_upper_case = upper_case_alphabet[key:] + upper_case_alphabet[:key]
    full_translation = str.maketrans(
        lower_case_alphabet + upper_case_alphabet,
        rotated_lower_case + rotated_upper_case,
    )
    return text.translate(full_translation)
