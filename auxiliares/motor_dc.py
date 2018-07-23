#!/usr/bin/env python
import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
import sys
import xbox
import math

#GPIO.cleanup()
GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering

#Configura Outputs
#DIR_ENABLE = 11
#DIR_FRENTE = 13
#DIR_RE = 15


GPIO.setup(11, GPIO.OUT) #direita_enable
GPIO.setup(13, GPIO.OUT) #direita_frente
GPIO.setup(15, GPIO.OUT) #direita_re
GPIO.setup(33, GPIO.OUT) #esquerda_enable
GPIO.setup(35, GPIO.OUT) #esquerda_frente
GPIO.setup(37, GPIO.OUT) #esquerda_re


print("Teste de motor DC, pressione ctrl+c para finalizar")

def controlador(motor,sinal):
	if motor=='esq':
                GPIO.output(33,1)
                GPIO.output(11,0)
                if sinal=='frente':
                    GPIO.output(35,1)
                    GPIO.output(37,0)
                if sinal=='re':
                    GPIO.output(37,1)
                    GPIO.output(35,0)
	if motor=='dir':
                GPIO.output(33,0)
                GPIO.output(11,1)
                if sinal=='frente':
                    GPIO.output(13,1)
                    GPIO.output(15,0)
                elif sinal=='re':
                    GPIO.output(15,1)
                    GPIO.output(13,0)
        if motor=='all':
                GPIO.output(33,1)
                GPIO.output(11,1)
                if sinal=='frente':
                    GPIO.output(35,1)
                    GPIO.output(13,1)
                    GPIO.output(37,0)
                    GPIO.output(15,0)
                if sinal=='re':
                    GPIO.output(37,1)
                    GPIO.output(15,1)
                    GPIO.output(35,0)
                    GPIO.output(13,0)

motor = sys.argv[1]
sinal = sys.argv[2]

try:
    print("\nMotor selecionado = " + motor)
    contador = 0
    while(contador < 40000):
        controlador(motor,sinal)
        if motor=='all':
            contador = contador + 3
        else:
            contador += 1

except KeyboardInterrupt:
    print("\nInterrupcao pelo teclado")


except:
    print("Houve algum erro")

finally:
    print("Limpando status das portas")
    GPIO.cleanup()
