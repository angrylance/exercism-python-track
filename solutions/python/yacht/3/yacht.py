# Solution to https://exercism.org/tracks/python/exercises/yacht


def digit_rolls(digit):
    return lambda dice: dice.count(digit) * digit


def YACHT(dice):
    return 50 if len(set(dice)) == 1 else 0


ONES = digit_rolls(1)
TWOS = digit_rolls(2)
THREES = digit_rolls(3)
FOURS = digit_rolls(4)
FIVES = digit_rolls(5)
SIXES = digit_rolls(6)


def FULL_HOUSE(dice):
    return sum(dice) if len(set(dice)) == 2 and dice.count(dice[0]) in [2, 3] else 0


def FOUR_OF_A_KIND(dice):
    return sum(x * 4 for x in set(dice) if dice.count(x) > 3)


def LITTLE_STRAIGHT(dice):
    return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0


def BIG_STRAIGHT(dice):
    return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0


def CHOICE(dice):
    return sum(dice)


def score(dice, category):
    return category(dice)
