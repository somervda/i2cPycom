import time
from machine import I2C
import pycom
import bme280


def blink(seconds, rgb):
    # print("blink", rgb)
    pycom.rgbled(rgb)
    time.sleep(seconds/2)
    pycom.rgbled(0x000000)  # off
    time.sleep(seconds/2)


pycom.heartbeat(False)

i2c = I2C(0, I2C.MASTER, pins=('P10', 'P9'), baudrate=100000)
bme = bme280.BME280(i2c=i2c)

for i in range(1):
    scan = i2c.scan()
    print("scan", i, " - ", scan)
    if len(scan) > 0:
        print("bme:", bme.formated_values)
        blink(1, 0xffffff)  # blink white
    else:
        blink(1, 0xff0000)  # blink red
