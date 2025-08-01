def find(search_list: list[int], value: int) -> int:
    """
    Find a value in the sorted search_list realizing binary search algorithm.
    Args:
        search_list(list[int]): given list of numbers
        value(int): a value to find in the list
    Returns:
        int: position of the value in the list, ValueError raised if not found.
    """
    low, high = 0, len(search_list) - 1
    while low <= high:
        mid = (high + low) // 2
        if search_list[mid] == value:
            return mid
        elif search_list[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    raise ValueError("value not in array")
