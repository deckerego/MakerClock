"""rotarytest.py

Raspberry Pi Python3 port of the commented Arduino rotary encoder code.

Pins (BCM numbering):
- CLK: 24
- DT: 25
- BUTTON (switch): 23

Usage:
  - Run on a Raspberry Pi with `RPi.GPIO` installed.
  - Example: `python3 rotarytest.py`

Notes:
  - This script uses BCM GPIO numbering. If you prefer physical pin numbers,
    change `GPIO.setmode(GPIO.BCM)` to `GPIO.setmode(GPIO.BOARD)` and update
    the pin constants accordingly.
  - The encoder signals and button are configured with internal pull-ups,
    matching the Arduino `digitalWrite(pin, HIGH)` pull-up behavior.
"""

import time
import sys

try:
    import RPi.GPIO as GPIO
except Exception as e:
    print("Error importing RPi.GPIO:", e)
    print("This script must be run on a Raspberry Pi with RPi.GPIO installed.")
    sys.exit(1)

# Use BCM numbering (GPIO numbers)
GPIO.setmode(GPIO.BCM)

# Pin assignments (BCM)
PIN_CLK = 24    # CLK
PIN_DT = 25     # DAT
PIN_BUTTON = 23 # SW

# Shared state
COUNT = 0
_last_rot_time = 0.0
DEBOUNCE_MS = 20


def rota_callback(channel):
    """Called on falling edge of CLK. Read DT to determine direction."""
    global COUNT, _last_rot_time
    now = time.time()
    if (now - _last_rot_time) * 1000.0 < DEBOUNCE_MS:
        return
    _last_rot_time = now

    # If DT is HIGH on CLK falling edge, treat as forward (match Arduino logic)
    try:
        if GPIO.input(PIN_DT) == GPIO.HIGH:
            COUNT += 1
        else:
            COUNT -= 1
    except RuntimeError:
        # In case GPIO has been cleaned up while callback is pending
        return


def button_callback(channel):
    """Called when button is pressed (active low). Resets COUNT and prints message."""
    global COUNT
    COUNT = 0
    print("STOP COUNT = 0")
    # emulate Arduino behavior that delays 2 seconds after reset
    time.sleep(2)


def main():
    global COUNT
    # Configure inputs with internal pull-ups (like Arduino's pull-high)
    GPIO.setup(PIN_CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PIN_DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PIN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Attach event detection
    GPIO.add_event_detect(PIN_CLK, GPIO.FALLING, callback=rota_callback, bouncetime=5)
    GPIO.add_event_detect(PIN_BUTTON, GPIO.FALLING, callback=button_callback, bouncetime=200)

    print("Starting rotary encoder test. Press Ctrl-C to exit.")
    try:
        while True:
            print(COUNT)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()