# Solution to https://exercism.org/tracks/python/exercises/transpose


def transpose(text: str) -> str:
    """
    Transpose the given string. If the input has rows of different lengths,
    this is to be solved as follows: Pad to the left with spaces. Don't pad to the right.
    Args:
        text (str): a string to transpose.
    Returns:
        str: transposed string.
    """
    text_matrix = text.split("\n")
    n_to_just = len(max(text_matrix, key=len))
    adjusted_matrix = [line.ljust(n_to_just, " ") for line in text_matrix]

    # Transpose using your zip + padding approach
    transposed_rows = (
        ["".join(col) for col in zip(*adjusted_matrix)] if n_to_just else []
    )

    # Smart trim: walk bottom-up and keep as many rightmost chars as needed
    keep_width = 0
    for i in range(len(transposed_rows) - 1, -1, -1):
        row_width = len(transposed_rows[i].rstrip())
        keep_width = max(keep_width, row_width)
        transposed_rows[i] = transposed_rows[i][:keep_width]

    return "\n".join(transposed_rows)
