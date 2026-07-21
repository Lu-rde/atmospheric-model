from . import constants


class Atmosphere:
    """
    Represents the atmospheric conditions at a given altitude.
    """

    def __init__(self, altitude: float):
        self.altitude = altitude

        self.temperature = None
        self.pressure = None
        self.density = None
        self.speed_of_sound = None
        self.layer = None

    def summary(self):
        print(f"Altitude: {self.altitude} m")
        print(f"Temperature: {self.temperature}")
        print(f"Pressure: {self.pressure}")
        print(f"Density: {self.density}")
        print(f"Speed of sound: {self.speed_of_sound}")