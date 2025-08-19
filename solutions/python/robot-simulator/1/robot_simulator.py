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
        self.direction = direction
        self.coordinates = (x_pos, y_pos)
        self._dir = DIRECTIONS.index(self.direction)

    def move(self, instruction: str):
        i = self._dir
        x, y = self.coordinates
        for letter in instruction:
            if letter == "R":
                i = (i + 1) % 4
            elif letter == "L":
                i = (i - 1) % 4
            elif letter == "A":
                dx, dy = VECTORS[i]
                x += dx
                y += dy
        self.direction = DIRECTIONS[i]
        self.coordinates = (x, y)
