#!/usr/bin/env python

import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)

def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(1)

    GPIO.setup(RCpin, GPIO.IN)
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading

try:

    while True:
        print RCtime(27)     # Read RC timing using pin #18

except KeyboardInterrupt:
    print "\nYou quit the program"
except:
    print "\nAn error has occurred"

finally:
    GPIO.cleanup()

