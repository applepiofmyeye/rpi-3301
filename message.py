import RPi.GPIO as GPIO
import time

class Message:

    def convert_to_bits(self, value, num_of_bits):
        return list(bin(value)[2:].zfill(num_of_bits))

    def send(self, key, value):
        if (key == "x" or key == "y"):
            if key == "x":
                print(f"Sending x coordinate: {value}")
            else:
                print(f"Sending y coordinate: {value}")
            # self.send_x(self.convert_to_bits(value))
            pins = [13, 15, 19, 21, 23, 27, 29, 31, 33, 35]
            value_in_bits = self.convert_to_bits(value, 10)
        elif (key == "header"):
            print(f"Sending header: {value}")
            pins = [4, 17]
            value_in_bits = self.convert_to_bits(value, 10)


        for i in range(len(value_in_bits)):
            bit = value_in_bits[i]
            xy_pin = pins[i]
            if bit == "1":
                # GPIO.output(xy_pin, GPIO.HIGH)
                GPIO.setup(xy_pin, GPIO.OUT)
                GPIO.output(xy_pin, GPIO.HIGH)
            else:
                GPIO.setup(xy_pin, GPIO.IN)
                # GPIO.output(xy_pin, GPIO.LOW) # For new relay board

        pass
