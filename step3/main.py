"""
main.py
"""

import sensor

sensor_pattern = "Source: {} - Value: {}"
sensor_data = sensor.read_sensor()

print(sensor_pattern.format(sensor_data["source"], sensor_data["value"]))