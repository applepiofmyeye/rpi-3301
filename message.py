import RPi.GPIO as GPIO
import time

class Message:

    def convert_to_bits(self, value):
        return list(bin(value)[2:].zfill(10))

    def send(self, key, value):
        if (key == "x"):
            print(f"Sending x coordinate: {value}")
            # self.send_x(self.convert_to_bits(value))
            pass
        elif (key == "y"):
            print(f"Sending y coordinate: {value}")
            pass
        pass

    def send_xy(self, value):
        GPIO.setmode(GPIO.BOARD)
        pins = [13, 15, 19, 21, 23, 27, 29, 31, 33, 35]
        for i in range(len(value)):
            bit = value[i]
            xy_pin = pins[i]
            if bit == "1":
                # GPIO.output(xy_pin, GPIO.HIGH)
                GPIO.setup(xy_pin, GPIO.OUT)
                GPIO.output(xy_pin, GPIO.HIGH)
            else:
                GPIO.setup(xy_pin, GPIO.IN)

        GPIO.setup(xy_pin, GPIO.OUT)
        time.sleep(0.1)
        GPIO.output(xy_pin, GPIO.LOW)
        pass
