# import time
from machine import I2C
# import pycom
import bme280
from ADS1115 import ADS1115


# def blink(seconds, rgb):
#     pycom.rgbled(rgb)
#     time.sleep(seconds/2)
#     pycom.rgbled(0x000000)  # off
#     time.sleep(seconds/2)


# pycom.heartbeat(False)

i2c = I2C(0, I2C.MASTER, pins=('P10', 'P9'), baudrate=100000)
scan = i2c.scan()
print("scan ", scan)
bme = bme280.BME280(i2c=i2c)
# Default address for adc is 0x48 (72 dec)
adc = ADS1115(i2c, address=0x48)

for i in range(1):
    #
    #     print("scan", i, " - ", scan)
    if len(scan) > 0:
        print("\nChannel 0 voltage: {}V".format(adc.get_voltage(0)))
        print("Channel 0 ADC value: {}\n".format(adc.read(0)))
        # print("bme:", bme.formated_values)
#         blink(1, 0xffffff)  # blink white
#     else:
#         blink(1, 0xff0000)  # blink red
