# main.py

from sensors.gps_sensor import RealGpsPositioningSystem, SimulatedGpsPositioningSystem
from nanobots.nanobot_manager import NanobotManagerWithMagneticSensing
from nanobots.nanobot import MagneticNanobot
from sensors.magnetic_sensor import SimulatedMagnetometer
from sensors.temperature_sensor import SimulatedTemperatureSensor
import time
import numpy as np

if __name__ == "__main__":
    use_simulation = True  # Toggle this for real or simulated mode

    if use_simulation:
        position_system = SimulatedGpsPositioningSystem()
        field_source_position = np.array([0, 0, 0])
    else:
        position_system = RealGpsPositioningSystem()
        field_source_position = np.array([0, 0, 0])

    nanobot_manager = NanobotManagerWithMagneticSensing(position_system, None, field_source_position)

    # Add nanobots
    for _ in range(5):
        nanobot = MagneticNanobot()
        nanobot.magnetometer = SimulatedMagnetometer()  # Replace with simulated magnetometer
        nanobot.temperature_sensor = SimulatedTemperatureSensor()  # Replace with simulated sensor
        nanobot_manager.add_nanobot(nanobot)

    while True:
        nanobot_manager.update(None)  # Replace `None` with a valid controller if available
        print("Nanobot Positions:", nanobot_manager.get_positions())
        time.sleep(1)
