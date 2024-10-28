from RPi import GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup([3, 5], GPIO.IN)

while True:
    print(int(GPIO.input(3)) , GPIO.input(5))
