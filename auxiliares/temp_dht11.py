import RPi.GPIO as GPIO

import sys
sys.path.insert(0,'/home/pi/Documents/Arquivos/Raspberry_pi/DHT11_Python/')
import dht11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin = 29)
result = instance.read()

if result.is_valid():
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)
else:
    print("Error: %d" % result.error_code)
