def two_fer(name: str = "you") -> str:
    """
    Returns a string in a format "One for {name}, one for me", if name is given, if not- {Name} is substituted for "you".
    Args:
        name(str): optional, default "you"
    Returns:
        str:  a string in a format "One for {name}, one for me", if name isn't specified - "you".
    """
    return f"One for {name}, one for me."
