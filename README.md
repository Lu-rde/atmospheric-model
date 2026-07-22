# 🌍 Atmospheric Model

> A Python implementation of the International Standard Atmosphere (ISA) for aerospace engineering applications.

Part of the **AeroPortfolio**, a collection of aerospace engineering software projects developed to learn, simulate and analyze real aerospace systems.

---

## ✨ Features

- 🌡️ Temperature calculation
- 🌬️ Pressure calculation
- ☁️ Air density calculation
- 🔊 Speed of sound calculation
- 📈 Scientific plots
- 🧪 Automated tests with pytest
- 🧩 Modular architecture
- 🚀 Designed for future aerospace simulators

---

## 📁 Project Structure

```text
atmospheric-model/

├── docs/
├── examples/
├── images/
├── src/
│   └── atmospheric_model/
├── tests/
├── README.md
├── requirements.txt
└── pyproject.toml
```

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/atmospheric-model.git

cd atmospheric-model

pip install -r requirements.txt
```

---

## 🚀 Quick Start

```python
from atmospheric_model import Atmosphere

atm = Atmosphere(5000)

atm.summary()
```

Example output:

```text
Altitude: 5000.0 m
Layer: Troposphere
Temperature: 255.65 K
Pressure: 54019.91 Pa
Density: 0.7361 kg/m³
Speed of sound: 320.53 m/s
```

---

## 📊 Generated Results

The library can automatically generate atmospheric profiles.

### Temperature Profile

*(Insert image here)*

### Pressure Profile

*(Insert image here)*

### Density Profile

*(Insert image here)*

### Speed of Sound Profile

*(Insert image here)*

---

## 📚 Scientific Background

The project implements the International Standard Atmosphere (ISA) within the troposphere.

Currently implemented:

- Temperature
- Pressure
- Density
- Speed of sound

Future versions will include additional atmospheric layers and more advanced atmospheric models.

---

## 🧪 Testing

Run all automated tests:

```bash
pytest
```

---

## 🗺️ Roadmap

- [x] ISA Troposphere
- [x] Temperature
- [x] Pressure
- [x] Density
- [x] Speed of sound
- [x] Scientific plots
- [x] Automated tests
- [ ] Complete ISA atmosphere
- [ ] CSV export
- [ ] JSON export
- [ ] NumPy support

---

## 🚀 AeroPortfolio

This project is one component of the AeroPortfolio ecosystem.

Future projects include:

- 🚀 Rocket Flight Simulator
- 🛰️ CubeSat Mission Simulator
- 🌍 Wind Field Model
- 🪐 Orbital Mechanics Toolkit
- 📡 CanSat Descent Simulator

---

## 📄 License

This project is released under the MIT License.