#!/usr/bin/env python

import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
import sys

print "arg1 = " + sys.argv[1]
print "arg2 = " + sys.argv[2]


GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering
pino = 7
GPIO.setup(pino, GPIO.OUT) ## Setup GPIO Pin 4 to OUT

##Define a function named Blink()
def Blink(numTimes,speed):
	## Ask user for total number of blinks and length of each blink
	print "Total number of times to blink: " + str(numTimes)
	print "Time : " + str(speed) + " seconds"

	for i in range(0,numTimes):## Run loop numTimes
		print "Iteration " + str(i+1)## Print current loop
		GPIO.output(pino,True)## Switch on pin
		time.sleep(speed)## Wait
		GPIO.output(pino,False)## Switch off pin
		time.sleep(speed)## Wait
	print "Done" ## When loop is complete, print "Done"
	GPIO.cleanup()


## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
Blink(int(sys.argv[1]),float(sys.argv[2]))
