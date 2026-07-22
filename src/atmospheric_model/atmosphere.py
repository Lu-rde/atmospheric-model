from . import constants


class Atmosphere:
    """
    Represents the atmospheric conditions at a given altitude
    using the International Standard Atmosphere (ISA).
    """

    def __init__(self, altitude: float):

        self.altitude = altitude

        self.temperature = self.calculate_temperature()
        self.pressure = self.calculate_pressure()

        self.density = self.calculate_density()
        self.speed_of_sound = None
        self.layer = "Troposphere"

    def calculate_temperature(self):
        """
        Calculates temperature according to ISA.
        """

        return (
            constants.SEA_LEVEL_TEMPERATURE
            + constants.TEMPERATURE_LAPSE_RATE * self.altitude
        )

    def calculate_pressure(self):
        """
        Calculates pressure according to ISA.
        """

        exponent = (
            -constants.GRAVITY /
            (constants.TEMPERATURE_LAPSE_RATE * constants.GAS_CONSTANT)
        )

        return (
            constants.SEA_LEVEL_PRESSURE *
            (
                self.temperature /
                constants.SEA_LEVEL_TEMPERATURE
            ) ** exponent
        )
    
    def calculate_density(self):
        """
        Calculates air density according to the ideal gas law.
        """
        
        return (
            self.pressure /
            (
                constants.GAS_CONSTANT *
                self.temperature
                
            )
        )

    def summary(self):

        print(f"Altitude: {self.altitude:.1f} m")
        print(f"Layer: {self.layer}")
        print(f"Temperature: {self.temperature:.2f} K")
        print(f"Pressure: {self.pressure:.2f} Pa")
        print(f"Density: {self.density:.4f} kg/m³")
        print(f"Speed of sound: {self.speed_of_sound}")