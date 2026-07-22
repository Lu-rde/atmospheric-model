import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from atmospheric_model import Atmosphere


def test_sea_level_temperature():
    atm = Atmosphere(0)

    assert atm.temperature == 288.15


def test_sea_level_pressure():
    atm = Atmosphere(0)

    assert round(atm.pressure) == 101325


def test_sea_level_density():
    atm = Atmosphere(0)

    assert round(atm.density, 3) == 1.225


def test_speed_of_sound():
    atm = Atmosphere(0)

    assert round(atm.speed_of_sound, 2) == 340.29


def test_temperature_decreases_with_altitude():
    sea = Atmosphere(0)
    mountain = Atmosphere(5000)

    assert mountain.temperature < sea.temperature


def test_pressure_decreases_with_altitude():
    sea = Atmosphere(0)
    mountain = Atmosphere(5000)

    assert mountain.pressure < sea.pressure


def test_density_decreases_with_altitude():
    sea = Atmosphere(0)
    mountain = Atmosphere(5000)

    assert mountain.density < sea.density


def test_speed_of_sound_decreases_with_altitude():
    sea = Atmosphere(0)
    mountain = Atmosphere(5000)

    assert mountain.speed_of_sound < sea.speed_of_sound