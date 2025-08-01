import string

ENCODING_MAP = str.maketrans(
    string.ascii_lowercase, string.ascii_lowercase[::-1], string.punctuation + " "
)


def encode(plain_text: str) -> str:
    """
    Returns text encoded by Atbash cipher.
    Args:
        plain_text (str) : text to encode.
    Returns:
        str: encoded text.
    """
    encoded = plain_text.lower().translate(ENCODING_MAP)
    return " ".join([encoded[i : i + 5] for i in range(0, len(encoded), 5)])


def decode(ciphered_text: str) -> str:
    """
    Decodes text encoded with Atbash cipher.
    Args:
        ciphered_text (str): encoded text to decode.
    Returns:
        str: decoded text.
    """
    return ciphered_text.translate(ENCODING_MAP)
