import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setwarnings(False)  # Disable warnings

# Define the GPIO pin for PWM (for example, GPIO18)
motor_pin = 18

# Set up the motor pin as an output
GPIO.setup(motor_pin, GPIO.OUT)

# Initialize PWM on the motor pin at 1000Hz
pwm = GPIO.PWM(motor_pin, 1000)  # 1000Hz frequency
pwm.start(0)  # Start with 0% duty cycle (motor off)

try:
    while True:
        # Increase speed from 0% to 100%
        for speed in range(0, 101, 5):  # Steps of 5% duty cycle
            pwm.ChangeDutyCycle(speed)  # Set duty cycle
            print(f"Motor speed: {speed}%")
            time.sleep(0.1)  # Wait for a bit

        # Decrease speed from 100% to 0%
        for speed in range(100, -1, -5):
            pwm.ChangeDutyCycle(speed)
            print(f"Motor speed: {speed}%")
            time.sleep(0.1)

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    pwm.stop()  # Stop PWM
    GPIO.cleanup()  # Reset GPIO settings
