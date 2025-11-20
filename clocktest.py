import board
import busio
from adafruit_ht16k33 import segments
i2c = busio.I2C(board.SCL, board.SDA)
display = segments.BigSeg7x4(i2c)
display.brightness = 0.5
display.fill(False)
display.print("88:88")
display.top_left_dot = True
display.bottom_left_dot = True
display.ampm = True