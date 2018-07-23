#!/usr/bin/env python
import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
import sys


#GPIO.cleanup()
GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering

#Configura Outputs
GPIO.setup(33, GPIO.OUT) #led1
GPIO.setup(31, GPIO.OUT) #led2
GPIO.setup(35, GPIO.OUT) #led3
GPIO.setup(37, GPIO.OUT) #led4

def limpa_todos(limite):
	i=1
	while i <= limite:
		led_sinal(str(i),0)
		i=i+1

def led_sinal(led,sinal):
	if led=='1':
		pino = 33
	elif led=='2':
		pino = 31
	elif led=='3':
		pino = 35
	elif led=='4':
		pino = 37
	else:
		pino = 'nenhum'

	if pino != 'nenhum':
		print "Pino selecionado = " + str(pino)
		GPIO.output(pino,sinal)
		print "Sinal enviado = " + str(sinal)

#Chama  as funcoes
#limpa_todos(4)

led = sys.argv[1]
sinal = sys.argv[2]

print "\nLed selecionado = " + led

led_sinal(led,int(sinal))


