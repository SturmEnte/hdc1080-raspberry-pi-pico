import time

class HDC1080:
    def __init__(self, i2c):
        self.i2c = i2c
        self.i2c.writeto(0x40, b'\x02\x10')
        
    def readSensor(self):
        self.i2c.writeto(0x40, b'\x00')
        time.sleep(0.02)
        data = self.i2c.readfrom(0x40, 4)
        temp = (data[0] << 8) | data[1]
        temperature = temp / 65536 * 165 - 40
        humidity = ((data[2] << 8) | data[3]) / 65536 * 100
        return (temperature, humidity)

