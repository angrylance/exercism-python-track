def distance(strand_a: str, strand_b: str) -> int:
    """
    Calculates and returns hamming distance of 2 DNA strands
    Args:
        strand_a(str): DNA strand 1 to compare
        strand_b(str): DNA strand 2 to compare strand_a with.
    Returns:
        int: Hamming distance of 2 DNS strands, or total number of differences.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    # Solution 1, for loop:
    # difference = 0
    # for i, v in enumerate(strand_a):
    #     if v != strand_b[i]:
    #         difference += 1
    # return difference

    # Solution 2 one-liner with enumerate:
    # return sum(1 for i, v in enumerate(strand_a) if v != strand_b[i])

    # Solution 3 one-liner with zip():
    return sum(a != b for a, b in zip(strand_a, strand_b))
