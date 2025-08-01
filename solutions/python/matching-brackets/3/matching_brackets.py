import re


def is_paired(input_string: str) -> bool:
    """
    Checks if brackets are matching in the given string.
    Args:
        input_string (str): a given string to check.
    Returns:
        bool: True if brackets are matching, False-if not.
    """
    # # Solution 1, stack + one-pass:
    # mapping_pairs = {")": "(", "]": "[", "}": "{"}
    # symbols = [symbol for symbol in input_string if symbol in "(){}[]"]
    # check_stack = []
    # for element in symbols:
    #     # Adding to stack opening brackets
    #     if element in mapping_pairs.values():
    #         check_stack.append(element)
    #     # Removing from stack matching closing brackets or false if mismatch
    #     elif element in mapping_pairs:
    #         if not check_stack or check_stack.pop() != mapping_pairs[element]:
    #             return False
    # return not check_stack

    # Solution 2, iterative with re.sub():
    symbols = re.sub(r"[^(){}\[\]]", "", input_string)  # Filtering non-brackets.
    while any(
        b in symbols for b in ("()", "[]", "{}")
    ):  # Looking for matched brackets.
        symbols = re.sub(
            r"\(\)|\[\]|\{\}", "", symbols
        )  # Replacing matched brackets to "".
    return not symbols
