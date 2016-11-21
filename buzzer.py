#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

chosenpin = 2

GPIO.setup(chosenpin,GPIO.OUT)

loop_count = 0

def morsecode ():

	#Dot Dot Dot
	GPIO.output(chosenpin,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(chosenpin,GPIO.LOW)
	time.sleep(.1)
	GPIO.output(chosenpin,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(chosenpin,GPIO.LOW)
	time.sleep(.1)
	GPIO.output(chosenpin,GPIO.HIGH)
	time.sleep(.1)

	#Dash Dash Dah
	GPIO.output(chosenpin,GPIO.LOW)
	time.sleep(.2)
	GPIO.output(chosenpin,GPIO.HIGH)
	time.sleep(.2)
	GPIO.output(chosenpin,GPIO.LOW)
	time.sleep(.2)
	GPIO.output(chosenpin,GPIO.HIGH)
	time.sleep(.2)
	GPIO.output(chosenpin,GPIO.LOW)
	time.sleep(.2)
	GPIO.output(chosenpin,GPIO.HIGH)
	time.sleep(.2)
	GPIO.output(chosenpin,GPIO.LOW)
	time.sleep(.2)

	#Dot Dot Dot
	GPIO.output(chosenpin,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(chosenpin,GPIO.LOW)
	time.sleep(.1)
	GPIO.output(chosenpin,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(chosenpin,GPIO.LOW)
	time.sleep(.1)
	GPIO.output(chosenpin,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(chosenpin,GPIO.LOW)
	time.sleep(.7)

os.system('clear')
print "Morse Code"
loop_count = input("How many times would you like SOS to loop?: ")
while loop_count > 0:
	loop_count = loop_count - 1
	morsecode ()
