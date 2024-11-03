import time
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO

# Define LCD setup
lcd = CharLCD(
    numbering_mode=GPIO.BCM,
    cols=16,
    rows=2,
    pin_rs=7,
    pin_e=8,
    pins_data=[25, 24, 23, 18]
)

# Write text to LCD
lcd.write_string("Hello, World!")
time.sleep(2)

# Clear the display
lcd.clear()
lcd.write_string("Welcome to Pi!")
time.sleep(2)

# Clean up
lcd.clear()
GPIO.cleanup()
