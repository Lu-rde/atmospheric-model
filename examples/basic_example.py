import sys
from pathlib import Path

# Add the src directory to Python's search path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from atmospheric_model import Atmosphere


def main():
    atm = Atmosphere(1500)
    atm.summary()


if __name__ == "__main__":
    main()