import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
class Message:

    def convert_to_bits(self, value, num_of_bits):
        return list(bin(value)[2:].zfill(num_of_bits))
    
    def send_x(self, value):
        pins = [7, 32]
        value_in_bits = self.convert_to_bits(1, 2)
        self.send(pins, value_in_bits)

        pins = [36, 15, 19, 21, 23, 29, 31, 33, 35, 37]
        value_in_bits = self.convert_to_bits(value, 10)
        self.send(pins, value_in_bits)
    
    def send_y(self, value):
        pins = [7, 32]
        value_in_bits = self.convert_to_bits(2, 2)
        self.send(pins, value_in_bits)

        pins = [36, 15, 19, 21, 23, 29, 31, 33, 35, 37]
        value_in_bits = self.convert_to_bits(value, 10)
        self.send(pins, value_in_bits)
    



    def send(self, pins, value_in_list_of_bits):

        for i in range(len(value_in_list_of_bits)):
            bit = value_in_list_of_bits[i]
            print("current bit:", bit)
            xy_pin = pins[i]
            print("current pin:", xy_pin, end=" ")
            if bit == "1":
                # GPIO.output(xy_pin, GPIO.HIGH)
                GPIO.setup(xy_pin, GPIO.OUT)
                GPIO.output(xy_pin, GPIO.HIGH)
                print("out")

            else:

                GPIO.setup(xy_pin, GPIO.IN)
                # GPIO.output(xy_pin, GPIO.LOW) # For new relay board
                print("in")
        
        time.sleep(5)

        # Set all to in
        for i in range(len(value_in_list_of_bits)):
            xy_pin = pins[i]
            GPIO.setup(xy_pin, GPIO.IN)
            print("current pin:", xy_pin)  

