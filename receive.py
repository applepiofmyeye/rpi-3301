from RPi import GPIO
import paho.mqtt.client as mqtt
import time
GPIO.setmode(GPIO.BOARD)
class Receive:
    def __init__(self):
        self.status = 0

    def convert_from_bits(self, bits_list):
        # Convert the list of bits to a string
        bits_str = ''.join(map(str, bits_list))
        # Convert the binary string to an integer
        return int(bits_str, 2)
    
    def receive_from_arm(self):
        GPIO.setup((3, 5), GPIO.IN)
        self.status = self.convert_from_bits([int(GPIO.input(3)), int(GPIO.input(5))]) 
        return self.status
