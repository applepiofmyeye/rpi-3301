from message import Message
from tool_recognition import ToolRecognition
import time
msg = Message()
toolRecognition = ToolRecognition()

x, y = toolRecognition.locate()
msg.send("x", int(x))
time.sleep(3)
msg.send("y", int(y))
time.sleep(3)
