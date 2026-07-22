"""
Utility functions for the Atmospheric Model.
"""
from pathlib import Path

import matplotlib.pyplot as plt


def create_plot(
    x,
    y,
    title: str,
    xlabel: str,
    ylabel: str,
    output_name: str,
) -> None:
    """
    Create and save a scientific plot.
    """

    plt.figure(figsize=(8, 5))

    plt.plot(x, y, linewidth=2)

    plt.title(title)

    plt.xlabel(xlabel)

    plt.ylabel(ylabel)

    plt.grid(True)

    images_dir = (
        Path(__file__).resolve().parents[2]
        / "images"
    )

    images_dir.mkdir(exist_ok=True)

    plt.savefig(images_dir / output_name, dpi=300)

    plt.show()