def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """
    Returns a number of points a player is awarded upon completing a level.
    Args:
        limit(int): the level completed by a player.
        multiples(list[int]): base values of magical items players have.
    Returns:
        int: the number of points the player receives, that is equal to a sum of non-duplicated multiples that are less than the limit.
    """
    # Solution 1, loops and set.add()
    # result = set()
    # for item in multiples:
    #     if item != 0:
    #         for level in range(item, limit, item):
    #             if level % item == 0:
    #                 result.add(level)
    # return sum(result)

    # Solution 2, sum + set comprehension.
    return sum(
        {level for item in multiples if item != 0 for level in range(item, limit, item)}
    )
