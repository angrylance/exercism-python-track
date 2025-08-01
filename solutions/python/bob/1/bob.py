def response(hey_bob: str) -> str:
    """
    Returns a string depending on a list of conditions for hey_bob input:
    Args:
    hey_bob(str): Input string based
    Returns:
    str - a response based on various conditions.
    """
    trimmed = hey_bob.strip()
    if trimmed.isupper() and trimmed.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if trimmed.endswith("?"):
        return "Sure."
    if trimmed.isupper():
        return "Whoa, chill out!"
    if not trimmed:
        return "Fine. Be that way!"
    return "Whatever."
