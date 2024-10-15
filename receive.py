from RPi import GPIO
import paho.mqtt.client as mqtt
import time
GPIO.setmode(GPIO.BOARD)
class Receive:
    def __init__(self):
        self.status = 0
        self.isPlaced = "not placed"
        self.loadcell_topic = "loadcell"

    def convert_from_bits(self, bits_list):
        # Convert the list of bits to a string
        bits_str = ''.join(map(str, bits_list))
        # Convert the binary string to an integer
        return int(bits_str, 2)
    
    def receive_from_arm(self):
        GPIO.setup((3, 5), GPIO.IN)
        self.status = self.convert_from_bits([int(GPIO.input(3)), int(GPIO.input(15))]) 
        return self.status
    
    def connect_to_mqtt(self):
        client = mqtt.Client()
        client.connect("172.20.10.3", 1883, 60)
        client.subscribe(self.loadcell_topic)
        client.message_callback_add(self.load_cell_topic, self.loadcell_callback)
        client.loop_forever()


    def loadcell_callback(self, client, userdata, message):
        # receive "placed" or "not placed"
        self.isPlaced = message.payload.decode("utf-8")
