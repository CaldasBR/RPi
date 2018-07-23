import RPi.GPIO as GPIO
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

def tocaBuzzer(repeticoes,delay):
    buzzer = 12
    GPIO.setup(buzzer,GPIO.OUT)
    GPIO.output(buzzer,0)

    for _ in xrange(repeticoes):
        for value in [True, False]:
            GPIO.output(buzzer, value)
            time.sleep(delay)


try:
    while True:
       tocaBuzzer(10,0.01)
       time.sleep(0.1)
       tocaBuzzer(10,0.01)
       time.sleep(2)

except KeyboardInterrupt:
    GPIO.output(buzzer,0)
    gpio.cleanup()
    exit
