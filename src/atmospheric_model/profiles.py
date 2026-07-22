from .atmosphere import Atmosphere


def generate_profiles(
    start: int = 0,
    end: int = 11000,
    step: int = 100,
) -> dict:
    """
    Generate ISA atmospheric profiles.
    """

    altitudes = []
    temperatures = []
    pressures = []
    densities = []
    speeds = []

    for altitude in range(start, end + step, step):

        atm = Atmosphere(altitude)

        altitudes.append(altitude)
        temperatures.append(atm.temperature)
        pressures.append(atm.pressure)
        densities.append(atm.density)
        speeds.append(atm.speed_of_sound)

    return {
        "altitude": altitudes,
        "temperature": temperatures,
        "pressure": pressures,
        "density": densities,
        "speed_of_sound": speeds,
    }