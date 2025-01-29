import RPi.GPIO as GPIO
import time

# GPIO pin configuration
DIR_PIN = 23  # Direction pin
STEP_PIN = 18  # Step pin
SPR = 200  # Steps per revolution for your stepper motor

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)

def rotate_motor(steps, direction, delay=0.01):
    """Rotate the stepper motor."""
    GPIO.output(DIR_PIN, direction)  # Set the direction
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(delay)

try:
    while True:
        # Rotate clockwise
        print("Rotating clockwise")
        rotate_motor(SPR, GPIO.HIGH)
        time.sleep(1)

        # Rotate counterclockwise
        print("Rotating counterclockwise")
        rotate_motor(SPR, GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping motor and cleaning up")
finally:
    GPIO.cleanup()  # Cleanup GPIO on exit
import RPi.GPIO as GPIO
import time

# GPIO pin configuration
DIR_PIN = 23  # Direction pin
STEP_PIN = 18  # Step pin
SPR = 200  # Steps per revolution for your stepper motor

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)

def rotate_motor(steps, direction, delay=0.01):
    """Rotate the stepper motor."""
    GPIO.output(DIR_PIN, direction)  # Set the direction
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(delay)

try:
    while True:
        # Rotate clockwise
        print("Rotating clockwise")
        rotate_motor(SPR, GPIO.HIGH)
        time.sleep(1)

        # Rotate counterclockwise
        print("Rotating counterclockwise")
        rotate_motor(SPR, GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping motor and cleaning up")
finally:
    GPIO.cleanup()  # Cleanup GPIO on exit
