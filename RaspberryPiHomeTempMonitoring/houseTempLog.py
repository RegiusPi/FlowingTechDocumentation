import board
import busio
import adafruit_sht31d
import os
import time

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)

while True:
    hum = str(sensor.relative_humidity)
    temp = str(sensor.temperature)
    os.popen(r'./logtemp.sh ' + temp + ' ' + hum)
    time.sleep(5)
