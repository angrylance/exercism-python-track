import re


def translate(text: str) -> str:
    """
    Translates the given string into Pig Latin, by following the rules:
    1. If a word begins with a vowel, or starts with "xr" or "yt",
    add an "ay" sound to the end of the word.
    2. If a word begins with one or more consonants, first move those consonants
    to the end of the word and then add an "ay" sound to the end of the word.
    3. If a word starts with zero or more consonants followed by "qu", first move
    those consonants (if any) and the "qu" part to the end of the word,
    and then add an "ay" sound to the end of the word.
    4. If a word starts with one or more consonants followed by "y", first move
    the consonants preceding the "y" to the end of the word,
    and then add an "ay" sound to the end of the word.
    Args:
        text (str): given word to translate to Pig Latin.
    Returns:
        str: a word translated to Pig Latin.
    """
    SUFFIX = "ay"
    words = text.split()
    result = []
    pattern_vowel = r"^(?:[aeiou]|xr|yt)\w*"
    pattern_consonants_qu = r"(^[^aeiou]*)(qu)(\w*)"
    pattern_consonants_y = r"(^[^aeiou]+)(y\w*)"
    pattern_consonants = r"(^[^aeiou]*)(\w*)"
    for word in words:
        if re.match(pattern_vowel, word):
            word = word + SUFFIX
        elif match := re.match(pattern_consonants_qu, word):
            word = match.group(3) + match.group(1) + match.group(2) + SUFFIX
        elif match := re.match(pattern_consonants_y, word):
            word = match.group(2) + match.group(1) + SUFFIX
        elif match := re.match(pattern_consonants, word):
            word = match.group(2) + match.group(1) + SUFFIX
        result.append(word)
    return " ".join(result)
