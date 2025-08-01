def is_paired(input_string: str) -> bool:
    """
    Checks if brackets are matching in the given string.
    Args:
        input_string (str): a given string to check.
    Returns:
        bool: True if brackets are matching, False-if not.
    """
    mapping_pairs = {")": "(", "]": "[", "}": "{"}
    symbols = [symbol for symbol in input_string if symbol in "(){}[]"]
    check_stack = []
    for element in symbols:
        # Adding to stack opening brackets
        if element in mapping_pairs.values():
            check_stack.append(element)
        # Removing from stack matching closing brackets or false if mismatch
        elif element in mapping_pairs:
            if not check_stack or check_stack.pop() != mapping_pairs[element]:
                return False
    return not check_stack
