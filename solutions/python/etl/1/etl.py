def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    """
    Takes the legacy_data with 1 to many mapping of letter to points and transforms it to one letter to one point mapping.
    Args:
        legacy_data(dict[int, list[str]]): legacy mapping of point-to-letters.
    Returns:
        dict[str, int]: letter in lowercase to point mapping.
    """
    # Solution 1, 2 for-loops:
    # result = dict()
    # for k, v in legacy_data.items():
    #     for value in v:
    #         result[value.lower()] = k
    # return result

    # Solution 2, comprehension
    return {value.lower(): k for k, v in legacy_data.items() for value in v}
