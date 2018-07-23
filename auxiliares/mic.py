import RPi.GPIO as GPIO
import time


#GPIO SETUP
microfone = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(microfone, GPIO.IN)

#Funcoes para controle do microfone
def detecta_som(microfone):
	if GPIO.input(microfone):
		print "Eu escuto voce"
	else:
		print "Eu escuto voce"

GPIO.add_event_detect(microfone, GPIO.FALLING, bouncetime=100)
GPIO.add_event_callback(microfone,detecta_som)

while True:
	time.sleep(0.05)
