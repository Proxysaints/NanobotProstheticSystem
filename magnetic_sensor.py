# magnetic_sensor.py

import smbus
import numpy as np

class MagneticGradientSensor:
    def __init__(self, position, temperature=25.0):
        self.position = np.array(position)
        self.temperature = temperature

    def read_magnetic_field(self, field_source_position, field_strength=1.0):
        distance = np.linalg.norm(self.position - field_source_position)
        temp_factor = 1 - 0.01 * (self.temperature - 25)
        magnetic_field = (field_strength * temp_factor) / (distance**2)
        gradient = (self.position - field_source_position) / distance
        return magnetic_field, gradient

    def update_temperature(self, ambient_temperature):
        self.temperature = ambient_temperature

class Magnetometer:
    def __init__(self, bus=1, address=0x1E):
        self.bus = smbus.SMBus(bus)
        self.address = address

    def read_magnetic_field(self):
        try:
            data = self.bus.read_i2c_block_data(self.address, 3, 6)
            x = np.int16((data[0] << 8) | data[1])
            y = np.int16((data[2] << 8) | data[3])
            z = np.int16((data[4] << 8) | data[5])
            return np.array([x, y, z])
        except Exception as e:
            print(f"Magnetometer Error: {e}")
            return np.array([0, 0, 0])

class SimulatedMagnetometer:
    def read_magnetic_field(self):
        return np.random.normal(0, 1, size=3)
