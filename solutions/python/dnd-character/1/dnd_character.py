# Solution to https://exercism.org/tracks/python/exercises/dnd-character
import random


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = Character.ability()
        self.wisdom = Character.ability()
        self.charisma = Character.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability():
        """
        Helper function generating ability score randomly.
        """
        rolls = list(random.randint(1, 6) for _ in range(4))
        return sum(rolls) - min(rolls)


def modifier(value: int) -> int:
    """
    Calculates generated character's constitution modifier from a given value.
    Args:
        value (int): a value of character's constitution.
    Returns:
        int: constutution modifier calculated by formula:
            rounded_down ((character's constitution - 10)/2)
    """
    return (value - 10) // 2
