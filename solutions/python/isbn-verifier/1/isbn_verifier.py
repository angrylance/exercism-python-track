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
    preprocessed_isbn = isbn.replace("-", "")  # Removing dashes
    # Filtering non-valid characters in wrong positions:
    if len(preprocessed_isbn) != 10:
        return False
    if any(
        not (c.isdigit() or (i == 9 and c.lower() == "x"))
        for i, c in enumerate(preprocessed_isbn)
    ):
        return False
    mapped_numbers = (
        10 if char.lower() == "x" else int(char) for char in preprocessed_isbn
    )
    return sum(d * m for d, m in zip(mapped_numbers, range(10, 0, -1))) % 11 == 0

    # preprocessed_isbn = isbn.replace("-", "")
    # if len(preprocessed_isbn) != 10:
    #     return False
    # preprocessed_isbn = [
    #     10 if char.lower() == "x" else int(char)
    #     for char in preprocessed_isbn
    #     if char.isdigit() or char.lower() == "x"
    # ]
    # if len(preprocessed_isbn) != 10 or 10 in preprocessed_isbn[0:9]:
    #     return False
    # acc, multiplier = 0, 10
    # for d in preprocessed_isbn:
    #     acc += d * multiplier
    #     multiplier -= 1
    # return acc % 11 == 0


print(is_valid("3598P215088"))
print(is_valid("3-598-2X507-9"))
print(is_valid("3598215088"))
