import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from atmospheric_model.profiles import generate_profiles
from atmospheric_model.utils import create_plot


def main() -> None:

    profiles = generate_profiles()

    create_plot(
        x=profiles["altitude"],
        y=profiles["temperature"],
        title="ISA Temperature Profile",
        xlabel="Altitude (m)",
        ylabel="Temperature (K)",
        output_name="temperature_profile.png",
    )


if __name__ == "__main__":
    main()