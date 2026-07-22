from atmospheric_model import Atmosphere


def test_temperature():

    atm = Atmosphere(0)

    assert atm.temperature == 288.15