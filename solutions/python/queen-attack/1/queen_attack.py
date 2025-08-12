# Solution to https://exercism.org/tracks/python/exercises/queen-attack


class Queen:
    """
    Create an instance of a queen in chess with coordinates row and column.
    """

    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")
        self.row = row
        self.column = column

    def can_attack(self, another_queen) -> bool:
        """
        Check if one queen in chess can attack another one by:
        1. Being on the same row.
        2. Being on the same column.
        3. Being on the diagonal line.
        """
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        return (
            self.row == another_queen.row
            or self.column == another_queen.column
            or abs(self.row - another_queen.row)
            == abs(self.column - another_queen.column)
        )
