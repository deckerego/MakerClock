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
    hour = now.hour % 12
    minute = now.minute
    display.print(f"{now.hour: 2}:{now.minute:02}")
    display.top_left_dot = now.hour >= 12
    time.sleep(15)
