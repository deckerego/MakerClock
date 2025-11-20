import time
import datetime
import board
import busio
from adafruit_ht16k33 import segments

i2c = busio.I2C(board.SCL, board.SDA)
display = segments.BigSeg7x4(i2c)
display.brightness = 0.5
display.fill(False)

while True:
    now = datetime.datetime.now()
    display.print(f"{now.hour:02}:{now.minute:02}")
    display.ampm = now.hour >= 12
    time.sleep(15)