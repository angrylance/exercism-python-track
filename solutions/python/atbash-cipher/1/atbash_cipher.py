import string


def encode(plain_text: str) -> str:
    """
    Returns text encoded by Atbash cipher.
    Args:
        plain_text (str) : text to encode.
    Returns:
        str: encoded text.
    """
    PLAIN = "abcdefghijklmnopqrstuvwxyz"
    CIPHER = "zyxwvutsrqponmlkjihgfedcba"
    encoding_map = str.maketrans(PLAIN, CIPHER, string.punctuation + " ")
    encoded = plain_text.lower().translate(encoding_map)
    return " ".join([encoded[i : i + 5] for i in range(0, len(encoded), 5)])


def decode(ciphered_text: str) -> str:
    """
    Decodes text encoded with Atbash cipher.
    Args:
        ciphered_text (str): encoded text to decode.
    Returns:
        str: decoded text.
    """
    PLAIN = "abcdefghijklmnopqrstuvwxyz"
    CIPHER = "zyxwvutsrqponmlkjihgfedcba"
    decoding_map = str.maketrans(CIPHER, PLAIN)
    encoded = ciphered_text.replace(" ", "")
    return encoded.translate(decoding_map)
