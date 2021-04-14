"""
"""

from .sensor import Sensor

class PressureSensor(Sensor):
    def __init__(self, name, data):
        super().__init__(name, data)

