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

    @property
    def coordinates(self) -> tuple[int, int]:
        """Current (x, y) position."""
        return (self._x, self._y)

    def turn_right(self) -> None:
        self._dir = (self._dir + 1) % 4

    def turn_left(self) -> None:
        self._dir = (self._dir - 1) % 4

    def advance(self) -> None:
        dx, dy = VECTORS[self._dir]
        self._x += dx
        self._y += dy

    def move(self, instruction: str):
        actions = {
            "R": self.turn_right,
            "L": self.turn_left,
            "A": self.advance,
        }
        for ch in instruction:
            action = actions.get(ch)
            if action:
                action()
