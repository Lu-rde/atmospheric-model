import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from atmospheric_model.profiles import generate_profiles
from atmospheric_model.utils import create_plot


def main() -> None:
    """
    Generate all ISA atmospheric profile plots.
    """

    profiles = generate_profiles()

    plots = [
        {
            "y": profiles["temperature"],
            "title": "ISA Temperature Profile",
            "ylabel": "Temperature (K)",
            "output": "temperature_profile.png",
        },
        {
            "y": profiles["pressure"],
            "title": "ISA Pressure Profile",
            "ylabel": "Pressure (Pa)",
            "output": "pressure_profile.png",
        },
        {
            "y": profiles["density"],
            "title": "ISA Density Profile",
            "ylabel": "Density (kg/m³)",
            "output": "density_profile.png",
        },
        {
            "y": profiles["speed_of_sound"],
            "title": "ISA Speed of Sound Profile",
            "ylabel": "Speed of Sound (m/s)",
            "output": "speed_of_sound_profile.png",
        },
    ]

    for plot in plots:
        create_plot(
            x=profiles["altitude"],
            y=plot["y"],
            title=plot["title"],
            xlabel="Altitude (m)",
            ylabel=plot["ylabel"],
            output_name=plot["output"],
        )


if __name__ == "__main__":
    main()