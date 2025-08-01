"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    health = 3
    total_aliens_created = 0

    @classmethod
    def aliens_counter(cls):
        """
        Class methods that tracks the total number of classes created.
        """
        cls.total_aliens_created += 1

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.__class__.aliens_counter()

    def hit(self):
        """
        Decrements a health value by 1 for an instance of an Alien class.
        """
        self.health -= 1

    def is_alive(self):
        """
        Checks if intance of an Alien() has health > 0, is alive.
        """
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        """
        Changes coordinates of an instance to new x and y.
        """
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other_object):
        """
        TODO
        """
        pass


def new_aliens_collection(list_of_positions: list) -> list:
    """
    Creates a list of alien given a list of positions as tuples.
    Args:
    list_of_positions(list): A list of tuples representing (x,y) coordinates
    Returns:
    list: A list of Alien instances created coordinates from list_of_positions
    """
    return [Alien(x, y) for x, y in list_of_positions]
