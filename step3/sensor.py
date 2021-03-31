"""
Sensor.py

Reading out sensor data.
"""

def read_sensor():
    # reading data from a ABC sensor.
    data = 10.4
    result = {
        "source": "voltage sensor",
        "value": data,
    }

    return result
