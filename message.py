import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
class Message:

    def convert_to_bits(self, value, num_of_bits):
        return list(bin(value)[2:].zfill(num_of_bits))

    def send(self, key, value):
        if (key == "x" or key == "y"):
            if key == "x":
                print(f"Sending x coordinate: {value}")
                self.send("header", 2)
            else:
                print(f"Sending y coordinate: {value}")
                self.send("header", 3)
            # self.send_x(self.convert_to_bits(value))
            pins = [36, 15, 19, 21, 23, 29, 31, 33, 35, 37]
            value_in_bits = self.convert_to_bits(value, 10)
        elif (key == "header"):
            print(f"Sending header: {value}")
            pins = [7, 32]
            value_in_bits = self.convert_to_bits(value, 2)


        for i in range(len(value_in_bits)):
            bit = value_in_bits[i]
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

        if (key == "y"):

            time.sleep(3)
            self.send("header", 0)
            GPIO.cleanup

