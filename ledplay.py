#!/usr/bin/env python

import RPi.GPIO as GPIO

light1 = 18
light2 = 23
light3 = 24

button1 = 10
button2 = 27
button3 = 22

def my_callback(self):
    GPIO.output(light1, GPIO.input(button1))
    GPIO.output(light2, GPIO.input(button2))
    GPIO.output(light3, GPIO.input(button3))

GPIO.setmode(GPIO.BCM)

GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(light1, GPIO.OUT, initial=GPIO.LOW)


GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(light2, GPIO.OUT, initial=GPIO.LOW)


GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(light3, GPIO.OUT, initial=GPIO.LOW)

GPIO.add_event_detect(button1, GPIO.BOTH, callback=my_callback)
GPIO.add_event_detect(button2, GPIO.BOTH, callback=my_callback)
GPIO.add_event_detect(button3, GPIO.BOTH, callback=my_callback)


run = 1
while (run != 0):
    try:
        pass
    except KeyboardInterrupt:
        GPIO.cleanup()
        run = 0
        print 'KeyboardInterrupt caught'
        break

print 'EXITED!'
