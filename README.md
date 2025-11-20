# MakerClock
Software to let a Raspberry Pi Zero W live on as a smart alarm clock


# Construction

## Printed Case

https://www.printables.com/model/764024-digital-clock/

## Assembly

https://learn.adafruit.com/digital-clock-with-circuitpython/

## Audio Setup

https://learn.adafruit.com/adafruit-speaker-bonnet-for-raspberry-pi/raspberry-pi-usage

## Display Setup

https://learn.adafruit.com/adafruit-led-backpack/0-dot-56-seven-segment-backpack-python-wiring-and-setup

## Cheap Rotary Encoder

https://community.microcenter.com/kb/articles/640-inland-rotary-encoder-module


# Installation

## Software Dependencies



## Running Notes

```
python3 -m venv ./clockenv --system-site-packages
source clockenv/bin/activate
pip install adafruit-circuitpython-ht16k33 adafruit-python-shell rpi.gpio
```


# Developer Notes

https://github.com/adafruit/Adafruit_CircuitPython_HT16K33/blob/main/adafruit_ht16k33/segments.py