# Solution for https://exercism.org/tracks/python/exercises/twelve-DAYS

DAYS = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]
GIFTS = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves, and ",
    "three French Hens, ",
    "four Calling Birds, ",
    "five Gold Rings, ",
    "six Geese-a-Laying, ",
    "seven Swans-a-Swimming, ",
    "eight Maids-a-Milking, ",
    "nine Ladies Dancing, ",
    "ten Lords-a-Leaping, ",
    "eleven Pipers Piping, ",
    "twelve Drummers Drumming, ",
]

INTRO = ("On the", "day of Christmas my true love gave to me:")


def build_verse(n: int) -> str:
    """
    Helper function building n-th verse in "The Twelve DAYS of Christmas."
    """
    gifts_on_nth_day = "".join(GIFTS[:n][::-1])
    return f"{INTRO[0]} {DAYS[n-1]} {INTRO[1]} {gifts_on_nth_day}"


def recite(start_verse: int, end_verse: int) -> list[str]:
    """
    Recites specified verses of the song: "The Twelve DAYS of Christmas."
    Args:
        start_verse (int): a verse to start reciting from.
        end_verse (int): a verse to finish reciting.
    Returns:
        list[str]: recited verses.
    """
    return [build_verse(n) for n in range(start_verse, end_verse + 1)]
