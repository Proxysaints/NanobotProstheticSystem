# Magnetic Nanobot Simulation

This project simulates a fleet of magnetic nanobots that can navigate based on GPS data, magnetic field sensing, and temperature sensing. The system uses particle filtering for localization, where the nanobots adjust their positions based on sensor data and a magnetic field source. The project supports both real and simulated sensor data for testing and development.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Project Overview

This simulation consists of several components:

- **GPS Positioning System**: Integrates with real GPS hardware or simulates GPS data for testing.
- **Magnetic Gradient Sensing**: Uses a magnetometer and magnetic gradient sensors to detect a magnetic field source and navigate towards it.
- **Temperature Sensing**: Simulates or reads real temperature data from a sensor to adjust measurements based on environmental factors.
- **Particle Filter Localization**: The particle filter algorithm helps the nanobots estimate their positions based on noisy sensor data.
- **Nanobot Manager**: Manages multiple nanobots, coordinates their movements, and tracks their states.

This project is useful for researching and simulating navigation algorithms, sensor fusion, and swarm robotics.

## Features

- Real and simulated GPS positioning.
- Simulated and real magnetic field sensing (using a magnetometer).
- Temperature sensing with the DS18B20 temperature sensor or a simulated model.
- Particle filtering for nanobot localization with magnetic gradient sensing.
- Modular structure, with different components (e.g., sensors, controllers) being easily interchangeable for testing and expansion.

## Installation

### Prerequisites

Before you begin, ensure you have the following software installed:

- Python 3.7 or later
- Required libraries: `numpy`, `gps`, `smbus2`, `w1thermsensor`

### Install Dependencies

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/magnetic-nanobot-simulation.git
    cd magnetic-nanobot-simulation
    ```

2. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can run the simulation by executing the `main.py` script. This script allows you to toggle between real and simulated modes.

1. To run the simulation with real sensors (GPS, magnetometer, temperature sensor):

    ```bash
    python main.py
    ```

2. To run the simulation with simulated data:

    In `main.py`, set `use_simulation = True`.

    ```python
    use_simulation = True  # Toggle for real or simulated mode
    ```

3. The nanobot positions will be updated every second, and you can view the current positions printed in the terminal.

## File Structure
