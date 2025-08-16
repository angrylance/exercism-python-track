# Solution to https://exercism.org/tracks/python/exercises/saddle-points


def saddle_points(matrix: list[list[int]]) -> list[dict[str, int]]:
    """
    Find coordinates of the largest in the row and the smallest in the column value.
    Args:
        matrix (list[list[int]]): 2D-matrix.
    Returns:
        list[dict[str, int]]: searched coordinates in the matrix.
    """
    # Raise exception for irregular matrices:
    if matrix and len(set(len(row) for row in matrix)) > 1:
        raise ValueError("irregular matrix")

    # Early exit for empty matrix and matrix of empty elements (which qualify as regular matrices)
    if not matrix or len(matrix[0]) == 0:
        return []

    # Solution 1 for-loops over rows and cols:

    # coordinates = []
    # # Precompute the lowest values in columns
    # min_in_cols = [min(col) for col in zip(*matrix)]

    # for row_number, row in enumerate(matrix, 1):
    #     max_in_row = max(row)
    #     for col_number, value in enumerate(row, 1):
    #         if value == max_in_row and value == min_in_cols[col_number - 1]:
    #             coordinates.append({"row": row_number, "column": col_number})
    # return coordinates

    # Solution 2 row and col candidates + sets intersecion:
    # max_in_rows = [max(row) for row in matrix]
    # min_in_cols = [min(col) for col in zip(*matrix)]
    # row_candidates = {
    #     (r, c)
    #     for r, row in enumerate(matrix)
    #     for c, v in enumerate(row)
    #     if v == max_in_rows[r]
    # }
    # col_candidates = {
    #     (r, c)
    #     for r, row in enumerate(matrix)
    #     for c, v in enumerate(row)
    #     if v == min_in_cols[c]
    # }
    # coordinates = [
    #     {"row": row + 1, "column": col + 1}
    #     for row, col in row_candidates & col_candidates
    # ]
    # return coordinates

    # Solution 3 max rows, min cols and 1 comprehension:
    max_in_rows = [max(row) for row in matrix]
    min_in_cols = [min(col) for col in zip(*matrix)]
    return [
        {"row": r + 1, "column": c + 1}
        for r, row in enumerate(matrix)
        for c, v in enumerate(row)
        if v == max_in_rows[r] and v == min_in_cols[c]
    ]
