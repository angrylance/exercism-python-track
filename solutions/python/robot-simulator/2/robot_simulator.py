# Solution to https://exercism.org/tracks/python/exercises/robot-simulator

# Globals for the directions
# Change the values as you see fit
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]
VECTORS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self._dir = DIRECTIONS.index(direction)  # Internal index
        self._x = x_pos
        self._y = y_pos

    @property
    def direction(self) -> str:
        """Current facing direction"""
        return DIRECTIONS[self._dir]

    def direction(self, value: str) -> None:
        self._dir = DIRECTIONS.index(value)

    @property
    def coordinates(self) -> tuple[int, int]:
        """Current (x, y) coordinates."""
        return (self._x, self._y)

    def move(self, instruction: str):
        i = self._dir
        x, y = self._x, self._y

        for ch in instruction:
            if ch == "R":
                i = (i + 1) % 4
            elif ch == "L":
                i = (i - 1) % 4
            elif ch == "A":
                dx, dy = VECTORS[i]
                x += dx
                y += dy
        self._dir = i
        self._x, self._y = x, y
