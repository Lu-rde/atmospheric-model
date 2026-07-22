from . import constants


class Atmosphere:
    """
    Represents the atmospheric conditions at a given altitude
    using the International Standard Atmosphere (ISA).
    """

    def __init__(self, altitude: float):

        self.altitude = altitude

        self.temperature = self.calculate_temperature()

        self.pressure = None
        self.density = None
        self.speed_of_sound = None
        self.layer = "Troposphere"

    def calculate_temperature(self):
        """
        Calculates the ISA temperature for altitudes
        between 0 and 11 km.
        """

        return (
            constants.SEA_LEVEL_TEMPERATURE
            + constants.TEMPERATURE_LAPSE_RATE * self.altitude
        )

    def summary(self):

        print(f"Altitude: {self.altitude:.1f} m")
        print(f"Layer: {self.layer}")
        print(f"Temperature: {self.temperature:.2f} K")
        print(f"Pressure: {self.pressure}")
        print(f"Density: {self.density}")
        print(f"Speed of sound: {self.speed_of_sound}")