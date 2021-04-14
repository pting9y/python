"""
Sensor.py

Reading out sensor data
and return the reading. 
"""

class Sensor():
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def read_sensor(self):
        # reading data from a ABC sensor.
        result = {
            "source": self.name,
            "value": self.data,
        }

        return result
    
    def get_value(self):
        return self.data
    
    """
    def get_value(self):
        print("Error you should call this function")
    """
