# Solution to https://exercism.org/tracks/python/exercises/robot-name

import random
import string


class Robot:
    # Class attribute for storing used names
    _used_names = set()

    def __init__(self):
        self.name = self._allocate_unique_name()

    @staticmethod
    def _generate_name_candidate():
        """
        Generate name candidates following the naming convention: LLDDD.
        """
        letters = random.choices(string.ascii_uppercase, k=2)
        digits = random.choices(string.digits, k=3)
        return "".join(letters + digits)

    @classmethod
    def _allocate_unique_name(cls):
        """
        Generate a name unique name checking already used names counter.
        """
        while True:
            generated_name = cls._generate_name_candidate()
            if generated_name not in cls._used_names:
                cls._used_names.add(generated_name)
                return generated_name

    def reset(self):
        """
        Reset the robot name and release it from names pool.
        """
        new_name = self._allocate_unique_name()
        self._used_names.discard(self.name)
        self.name = new_name
