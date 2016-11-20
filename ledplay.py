#!/usr/bin/env python

import RPi.GPIO as GPIO

def my_callback(self):
    GPIO.output(18, GPIO.input(17))
    GPIO.output(23, GPIO.input(27))
    GPIO.output(24, GPIO.input(22))

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)


GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)


GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)

GPIO.add_event_detect(17, GPIO.BOTH, callback=my_callback)
GPIO.add_event_detect(27, GPIO.BOTH, callback=my_callback)
GPIO.add_event_detect(22, GPIO.BOTH, callback=my_callback)


run = 1
while (run != 0):
    try:
        pass
    except KeyboardInterrupt:
        run = 0
        GPIO.cleanup()
        print 'KeyboardInterrupt caught'
        break
print 'EXITED!'
