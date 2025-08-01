import re


def is_valid(isbn: str) -> bool:
    """
    Checks if the given isbn string is a valid ISBN code.
    The validity criteria is:
    (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
    Args:
    isbn(str): ISBN code to check for validity
    Returns:
    bool: True if the code is valid, False - if not.
    """
    # Removing dashes
    # preprocessed_isbn = isbn.replace("-", "")
    # if len(preprocessed_isbn) != 10:
    #     return False
    # # Filtering non-valid codes by checking for if char isdigit() and the last char being "x"
    # if any(
    #     not (c.isdigit() or (i == 9 and c.lower() == "x"))
    #     for i, c in enumerate(preprocessed_isbn)
    # ):
    #     return False
    # # Mapping characters to numbers: 'X' → 10, others → int
    # mapped_numbers = (
    #     10 if char.lower() == "x" else int(char) for char in preprocessed_isbn
    # )
    # # Running a validation check using generator and zip and unpacking:
    # return sum(d * m for d, m in zip(mapped_numbers, range(10, 0, -1))) % 11 == 0

    # Solution 2 using regex for filtering:
    cleaned_isbn = isbn.replace("-", "")
    if not re.fullmatch(r"\d{9}[\dXx]", cleaned_isbn):
        return False
    digits = [10 if char.lower() == "x" else int(char) for char in cleaned_isbn]
    return sum(x * y for x, y in zip(digits, range(10, 0, -1))) % 11 == 0
