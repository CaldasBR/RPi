#!/usr/bin/env python
import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
import sys

funcao = sys.argv[1]
tempo = sys.argv[2]

GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering

#Configura Outputs
GPIO.setup(33, GPIO.OUT) 
GPIO.setup(31, GPIO.OUT) 
GPIO.setup(35, GPIO.OUT) 
GPIO.setup(37, GPIO.OUT) 

#Define FUNCAO 1
def pisca_seq(speed):
	#Ask user for total number of blinks and length of each blink
	print "Entrei no pisca_seq"
	i = 0
	sinal = 1
	while 1:
		print "Sequencia: " + str(i)
		GPIO.output(33,sinal)
		time.sleep(speed)
		GPIO.output(31,sinal)
		time.sleep(speed)
		GPIO.output(35,sinal)
		time.sleep(speed)
		GPIO.output(37,sinal)
		time.sleep(speed)
		sinal = not sinal
		i=i+1

## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
print "Programa selecionado = " + funcao
print "Intervalo selecionado = " + tempo

if funcao == '1':
	pisca_seq(float(tempo))

GPIO.cleanup()
