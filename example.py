from HDC1080 import HDC1080
from machine import I2C, Pin
import time

# Initialize the i2c pins
sda = Pin(26)
scl = Pin(27)
i2c = I2C(1, sda=sda, scl=scl)

# List i2c devices
devices = i2c.scan()
print(devices)

# Initialize the sensor
sensor = HDC1080(i2c)

# Main loop that prints the temperature and humidity every second + ~20 milliseconds to read the sensor
while True:
    data = sensor.readSensor()
    print("Temperature:", data[0], "°C")
    print("Humidity:", data[1], "%")
    time.sleep(1)
