#!/usr/bin/env python

import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
import sys


GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering
pino = 7
GPIO.setup(pino, GPIO.OUT) ## Setup GPIO Pin 7 to OUT

p = GPIO.PWM(pino, int(sys.argv[1]))
p.start(0)

try:
	while 1:
		print "Frequencia = " + sys.argv[1]
		p.ChangeDutyCycle(int(sys.argv[1]))
		time.sleep(3)
		print "Frequencia = " + str(int(sys.argv[1])+50)
		p.ChangeDutyCycle(int(sys.argv[1])+50)
		time.sleep(3)
except (KeyboardInterrupt):
	print "nnVoce pressionou ctrl c para sair"
	p.stop()
	GPIO.cleanup()
