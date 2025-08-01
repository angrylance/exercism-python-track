def commands(binary_str: str) -> list[str]:
    """
    Translate a given binary sequence to a str representing actions of secret handshake.
    Args:
        binary_str(str): given binary string.
    Returns:
        list[str]: sequence of secret handshake action.
    """
    normalized_str = binary_str.zfill(5)
    actions = ["wink", "double blink", "close your eyes", "jump"]
    result = [
        action for action, bit in zip(actions, normalized_str[::-1]) if bit == "1"
    ]
    if normalized_str[0] == "1":
        result.reverse()
    return result
