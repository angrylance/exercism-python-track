class SpaceAge:
    """
    Defines an age in seconds for a person.
    """

    ORBITAL_PERIODS = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_age = seconds / 31557600

    def age_on(self, orbital_period):
        return round(self.earth_age / orbital_period, 2)

    def on_earth(self):
        """
        Returns age for a person in Earth years.
        """
        return self.age_on(self.ORBITAL_PERIODS["earth"])

    def on_mercury(self):
        """
        Returns age for a person in Mercury years.
        """
        return self.age_on(self.ORBITAL_PERIODS["mercury"])

    def on_venus(self):
        """
        Returns age for a person in Venus years.
        """
        return self.age_on(self.ORBITAL_PERIODS["venus"])

    def on_mars(self):
        """
        Returns age for a person in Mars years.
        """
        return self.age_on(self.ORBITAL_PERIODS["mars"])

    def on_jupiter(self):
        """
        Returns age for a person in Jupiter years.
        """
        return self.age_on(self.ORBITAL_PERIODS["jupiter"])

    def on_saturn(self):
        """
        Returns age for a person in Saturn years.
        """
        return self.age_on(self.ORBITAL_PERIODS["saturn"])

    def on_uranus(self):
        """
        Returns age for a person in Uranus years.
        """
        return self.age_on(self.ORBITAL_PERIODS["uranus"])

    def on_neptune(self):
        """
        Returns age for a person in Neptune years.
        """
        return self.age_on(self.ORBITAL_PERIODS["neptune"])
