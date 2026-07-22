import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from atmospheric_model import Atmosphere


def main():

    altitudes = [0, 1000, 1500, 5000, 10000]

    for altitude in altitudes:

        atm = Atmosphere(altitude)

        atm.summary()

        print("-" * 40)


if __name__ == "__main__":
    main()