# Solution to https://exercism.org/tracks/python/exercises/ocr-numbers

DIGITS = {
    (" _ ", "| |", "|_|", "   "): "0",
    ("   ", "  |", "  |", "   "): "1",
    (" _ ", " _|", "|_ ", "   "): "2",
    (" _ ", " _|", " _|", "   "): "3",
    ("   ", "|_|", "  |", "   "): "4",
    (" _ ", "|_ ", " _|", "   "): "5",
    (" _ ", "|_ ", "|_|", "   "): "6",
    (" _ ", "  |", "  |", "   "): "7",
    (" _ ", "|_|", "|_|", "   "): "8",
    (" _ ", "|_|", " _|", "   "): "9",
}


def validate(input_grid: list[str]):
    """
    Validate input grid.
    Args:
        input_grid (list[str]): the given input grid.
    Raises:
        ValueError: if Number of input lines is not a multiple of four
        or if Number of input columns is not a multiple of three.
    """
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(x) % 3 != 0 for x in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")


def iter_line_blocks(input_grid: list[str]):
    """
    Divide input grid into 4-row blocks for multi-line support.
    Args:
        input_grid (list[str]): the given input grid.
    Yields:
        list[str]: a consecutive block of four rows, representing one line of OCR digits.
    """
    return (input_grid[n : n + 4] for n in range(0, len(input_grid), 4))


def iter_glyphs(input_grid: list[str]):
    """
    Iterate over a 4-line block and yield glyphs (digits) in 3-column chunks.
    Args:
        input_grid (list[str]): the given input grid.
    Yields:
        tuple(str,str,str,str): A glyph representing a single digit.
    """
    width = len(input_grid[0])
    return (tuple(row[c : c + 3] for row in input_grid) for c in range(0, width, 3))


def convert(input_grid: list[str]) -> str:
    """
    Convert into string any valid (3x4)n grid.
    Args:
        input_grid (list[str]): the given input grid.
    Returns:
        str: converted into a string input grid.
    """
    validate(input_grid)
    result = []
    for block in iter_line_blocks(input_grid):
        line = []
        for glyph in iter_glyphs(block):
            line.append(DIGITS.get(glyph, "?"))
        result.append("".join(line))
    return ",".join(result)
