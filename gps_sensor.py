# gps_sensor.py

import numpy as np
import gps

class RealGpsPositioningSystem:
    def __init__(self):
        self.session = gps.gps(mode=gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

    def update_position(self):
        try:
            self.session.next()  # Get the latest GPS data
            if self.session.fix.mode >= 2:
                latitude = self.session.fix.latitude
                longitude = self.session.fix.longitude
                altitude = self.session.fix.altitude
                return np.array([latitude, longitude, altitude])
            else:
                print("No valid GPS fix.")
                return None
        except Exception as e:
            print(f"GPS Error: {e}")
            return None

class SimulatedGpsPositioningSystem:
    def __init__(self):
        self.position = np.array([0.0, 0.0, 0.0])

    def update_position(self):
        self.position += np.random.normal(0, 0.01, size=3)
        return self.position
