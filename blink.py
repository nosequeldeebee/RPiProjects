#!/usr/bin/env python

import time
import random
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT)  # Set up GPIO pins as outputs
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)

pins = [4, 18, 23, 24]

try:
    while True:
        x = random.choice(pins)  # Pick a random pin
        y = random.choice(pins)
        z = random.choice(pins)
        if (x != y and x != z and y != z):
            GPIO.output(x, GPIO.HIGH)  # Turn random LED on
            GPIO.output(y, GPIO.HIGH)
            GPIO.output(z, GPIO.HIGH)
            time.sleep(0.15)  # Pause
            GPIO.output(x, GPIO.LOW)  # Turn random LED off
            GPIO.output(y, GPIO.LOW)
            GPIO.output(z, GPIO.LOW)

except KeyboardInterrupt:
    print "\nYou quit the program"
except:
    print "\n an error has occurred"

finally:
    GPIO.cleanup()

