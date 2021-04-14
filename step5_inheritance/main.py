"""
"""

#import sensors package
import sensors


def print_sensor_value(sensor):
    print ("Sensor name: '{}' value: {}".format(sensor.name, sensor.data))


first_sensor =sensors.PressureSensor("Pressure sensor", 1)
second_sensor = sensors.TemperatureSensor("Temperature sensor", 1)
third_sensor = sensors.PressureSensor("Pressure sensor", 2)

print_sensor_value(first_sensor)
print_sensor_value(second_sensor)
print_sensor_value(third_sensor)