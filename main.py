from send import Send 
from tool_recognition import ToolRecognition
import time
msg = Send()
toolRecognition = ToolRecognition()
import RPi.GPIO as GPIO
try:
    #x, y = toolRecognition.locate()
    #msg.send_x(int(x))
    #msg.send_x(100)
    toolRecognition.inspect()
    #time.sleep(3)
    #msg.send_y(int(y))
    time.sleep(3)
except KeyboardInterrupt:
    GPIO.cleanup()
