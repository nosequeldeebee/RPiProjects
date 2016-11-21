#!/usr/bin/env python

import time
import random
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

light1 = 18
light2 = 23
light3 = 24
light4 = 15
light5 = 14

GPIO.setup(light1,GPIO.OUT)  # Set up GPIO pins as outputs
GPIO.setup(light2,GPIO.OUT)
GPIO.setup(light3,GPIO.OUT)
GPIO.setup(light4,GPIO.OUT)
GPIO.setup(light5,GPIO.OUT)

pins = [light1, light2, light3, light4, light5]

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

