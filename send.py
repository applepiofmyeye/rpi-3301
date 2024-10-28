import RPi.GPIO as GPIO
import time
class Send:

    def convert_to_bits(self, value, num_of_bits):
        return list(bin(value)[2:].zfill(num_of_bits))
    
    def send_x(self, value):

        print("Sending x", value)
        pins = [7, 32]
        value_in_bits = self.convert_to_bits(3, 2)
        self.send(pins, value_in_bits)

        pins = [36]
        value_in_bits = self.convert_to_bits(1, 1) if value < 0 else self.convert_to_bits(0, 1)
        self.send(pins, value_in_bits)

        pins = [15, 19, 21, 23, 29, 31, 33, 35, 37]
        value_in_bits = self.convert_to_bits(abs(value), 9)
        self.send(pins, value_in_bits)
    
    def send_y(self, value):
        print("Sending y", value)
        pins = [7, 32]
        value_in_bits = self.convert_to_bits(2, 2)
        self.send(pins, value_in_bits)

        pins = [36] 
        value_in_bits = self.convert_to_bits(1, 1) if value < 0 else self.convert_to_bits(0, 1)
        self.send(pins, value_in_bits)

        pins = [15, 19, 21, 23, 29, 31, 33, 35, 37]
        value_in_bits = self.convert_to_bits(abs(value), 9)
        self.send(pins, value_in_bits, reset=True)

    def send_type(self, value):
        pins = [16, 18]
        value_in_bits = self.convert_to_bits(value, 2)
        self.send(pins, value_in_bits, reset=True)
        
    def send(self, pins, value_in_list_of_bits, reset=False):
        GPIO.setmode(GPIO.BOARD)

        for i in range(len(value_in_list_of_bits)):
            bit = value_in_list_of_bits[i]
            xy_pin = pins[i]
            if bit == "1":
                GPIO.setup(xy_pin, GPIO.OUT)
                GPIO.output(xy_pin, GPIO.HIGH)

            else:
                GPIO.setup(xy_pin, GPIO.IN)
        

        # Set all to in
        if reset:
            time.sleep(5)
            GPIO.setup([7, 32, 15, 19, 21, 23, 29, 31, 33, 35, 37, 36, 16, 18], GPIO.IN)
            #for i in range(len(value_in_list_of_bits)):
                #time.sleep(3)
                #xy_pin = pins[i]
                #GPIO.setup(xy_pin, GPIO.IN)

