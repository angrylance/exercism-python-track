# Solution to https://exercism.org/tracks/python/exercises/phone-number
import re


class PhoneNumber:
    """
    Creates a phone number after validating it's correctness.
    """

    def __init__(self, number):
        if re.search(r"[a-zA-Z]", number):
            raise ValueError("letters not permitted")
        if re.search(r"[^0-9 .\-()+]", number):
            raise ValueError("punctuations not permitted")

        cleaned_number = "".join(x for x in number if x.isdigit())
        if len(cleaned_number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(cleaned_number) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(cleaned_number) == 11 and cleaned_number[0] != "1":
            raise ValueError("11 digits must start with 1")
        if len(cleaned_number) == 11 and cleaned_number[0] == "1":
            cleaned_number = cleaned_number[1:]
        area_code, exchange_code, subscriber_number = (
            cleaned_number[0:3],
            cleaned_number[3:6],
            cleaned_number[6:],
        )
        if area_code[0] == "0":
            raise ValueError("area code cannot start with zero")
        if area_code[0] == "1":
            raise ValueError("area code cannot start with one")
        if exchange_code[0] == "0":
            raise ValueError("exchange code cannot start with zero")
        if exchange_code[0] == "1":
            raise ValueError("exchange code cannot start with one")

        self.number = cleaned_number
        self.area_code = area_code
        self.exchange_code = exchange_code
        self.subscriber_number = subscriber_number

    def pretty(self):
        """
        Return a phone number in a format: (AREA_CODE)-EXCHANGE_CODE-SUBSCRIBER_NUMBER
        """
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
