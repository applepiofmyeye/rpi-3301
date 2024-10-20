from send import Send 
from tool_recognition import ToolRecognition
import time
msg = Send()
toolRecognition = ToolRecognition()

x, y = toolRecognition.locate()
msg.send_x(int(x))
time.sleep(3)
msg.send_y(int(y))
time.sleep(3)
