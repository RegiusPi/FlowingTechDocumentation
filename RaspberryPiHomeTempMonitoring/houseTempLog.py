import board
import busio
import adafruit_sht31d
import os
import time

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)

while True:
    """Loops indefinitly every five seconds. grabs the temperature through the sensor object that was 
    instantiated above and then used the os.popen library to execute the bash script with several 
    args"""
    hum = str(sensor.relative_humidity)
    temp = str(sensor.temperature)
    os.popen(r'./logtemp.sh ' + temp + ' ' + hum)
    time.sleep(5)
