SIMPLE_NUMBERS = (
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
)

NUMBERS_TENS = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}


def break_numbers(number: int) -> list[int]:
    """
    Helper function to break the numbers into list of thousands.
    """
    chunks = []
    while number > 0:
        chunks.append(number % 1000)
        number //= 1000
    return list(reversed(chunks or [0]))


def num_to_text(number: int) -> str:
    """
    Helper function to convert number from 0 to 999 to str.
    """
    if 0 <= number < 20:
        result = SIMPLE_NUMBERS[number]
    elif 20 <= number < 100:
        tens = NUMBERS_TENS[number // 10]
        if ones := number % 10:
            result = f"{tens}-{SIMPLE_NUMBERS[ones]}"
        else:
            result = tens
    else:
        hundreds = number // 100
        if rest := number % 100:
            result = f"{SIMPLE_NUMBERS[hundreds]} hundred {num_to_text(rest)}"
        else:
            result = f"{SIMPLE_NUMBERS[hundreds]} hundred"
    return result


def add_scales(chunks: list[int]) -> str:
    """
    Helper function to add scales into a string with transcribed numbers.
    """
    scales = ("", "thousand", "million", "billion")
    parts = []
    if chunks == [0]:
        return "zero"
    for index, chunk in enumerate(reversed(chunks)):
        if chunk == 0:
            continue
        chunk_text = (
            f"{num_to_text(chunk)} {scales[index]}"
            if scales[index]
            else num_to_text(chunk)
        )
        parts.append(chunk_text)
    return " ".join(reversed(parts))


def say(number: int) -> str:
    """
    Given a number from 0 to 999,999,999,999, spell out that number in English.
    Args:
        number (int): a number to spell out.
    Returns:
        str: a spelled number.
    """
    # Handling out of range input:
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")
    numbers = break_numbers(number)
    return add_scales(numbers)
