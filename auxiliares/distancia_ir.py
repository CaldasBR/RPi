#!/usr/bin/env python
import RPi.GPIO as GPIO ## Import GPIO library
import time
import os

#GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering

#EN_DIST_IR = 18
SINAL_DIST_IR = 16

#GPIO.setup(EN_DIST_IR, GPIO.OUT) #direita_enable
GPIO.setup(SINAL_DIST_IR, GPIO.IN, pull_up_down=GPIO.PUD_UP) #direita_frente

print("Teste proximidade, pressione ctrl+c para finalizar")

def loop():
    while True:
        if(0 == GPIO.input(SINAL_DIST_IR)):
	   print "Pare o carro!"
	   time.sleep(0.2)
	   os.system('cls' if os.name == 'nt' else 'clear')

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    try:
	loop()
    except KeyboardInterrupt:
	destroy(0)
