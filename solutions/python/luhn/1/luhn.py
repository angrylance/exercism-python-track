class Luhn:
    """
    Creates an instance of a Luhn number.
    """

    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self) -> bool:
        """
        Checks if provided Luhn-number is valid.
        Returns:
            bool: True if number is valid, False-if not.
        """
        number = self.card_num.replace(" ", "")
        if not number.isdigit() or len(number) < 2:
            return False

        numbers = list(map(int, number))

        total = 0
        # Choosing for-loop for readability because of the conditions:
        for i, n in enumerate(reversed(numbers)):
            if i % 2:
                doubled = n * 2
                total += doubled - 9 if doubled > 9 else doubled
            else:
                total += n

        return total % 10 == 0
