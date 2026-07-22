import math

from . import constants


class Atmosphere:
    """
    Represents the atmospheric conditions at a given altitude
    using the International Standard Atmosphere (ISA).
    """

    def __init__(self, altitude: float) -> None:
        """
        Initialize the atmosphere model for a given altitude.

        Args:
            altitude: Altitude above sea level in meters.
        """

        self.altitude = altitude

        self.temperature = self._calculate_temperature()
        self.pressure = self._calculate_pressure()
        self.density = self._calculate_density()
        self.speed_of_sound = self._calculate_speed_of_sound()

        self.layer = "Troposphere"

    def _calculate_temperature(self) -> float:
        """Return the ISA temperature."""

        return (
            constants.SEA_LEVEL_TEMPERATURE
            + constants.TEMPERATURE_LAPSE_RATE * self.altitude
        )

    def _calculate_pressure(self) -> float:
        """Return the ISA pressure."""

        exponent = (
            -constants.GRAVITY
            / (constants.TEMPERATURE_LAPSE_RATE * constants.GAS_CONSTANT)
        )

        return (
            constants.SEA_LEVEL_PRESSURE
            * (
                self.temperature
                / constants.SEA_LEVEL_TEMPERATURE
            )
            ** exponent
        )

    def _calculate_density(self) -> float:
        """Return the air density."""

        return (
            self.pressure
            / (
                constants.GAS_CONSTANT
                * self.temperature
            )
        )

    def _calculate_speed_of_sound(self) -> float:
        """Return the speed of sound."""

        return math.sqrt(
            constants.GAMMA
            * constants.GAS_CONSTANT
            * self.temperature
        )

    def summary(self) -> None:
        """Print a formatted summary."""

        print(f"Altitude: {self.altitude:.1f} m")
        print(f"Layer: {self.layer}")
        print(f"Temperature: {self.temperature:.2f} K")
        print(f"Pressure: {self.pressure:.2f} Pa")
        print(f"Density: {self.density:.4f} kg/m³")
        print(f"Speed of sound: {self.speed_of_sound:.2f} m/s")

    def to_dict(self) -> dict:
        """Return the atmospheric properties as a dictionary."""

        return {
            "altitude": self.altitude,
            "layer": self.layer,
            "temperature": self.temperature,
            "pressure": self.pressure,
            "density": self.density,
            "speed_of_sound": self.speed_of_sound,
        }