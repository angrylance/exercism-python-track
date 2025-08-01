def two_fer(name: str = "you") -> str:
    """
    Returns a personalized string with a name or 'you' if no name is provided.

    Args:
        name (str): The person's name. Defaults to 'you'.
    Returns:
        str: A sentence in the format "One for <name>, one for me.".
    """
    return f"One for {name}, one for me."
