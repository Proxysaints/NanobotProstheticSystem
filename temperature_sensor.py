# temperature_sensor.py

from w1thermsensor import W1ThermSensor

class TemperatureSensor:
    def __init__(self):
        self.sensor = W1ThermSensor()

    def get_temperature(self):
        return self.sensor.get_temperature()

class SimulatedTemperatureSensor:
    def get_temperature(self):
        return 25.0 + np.random.normal(0, 0.5)
