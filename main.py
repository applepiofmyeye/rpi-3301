from message import Message
from tool_recognition import ToolRecognition
import time
msg = Message()
toolRecognition = ToolRecognition()

# Inspect the tool (cam 1)

#Send the x and y coordinates to the robot arm
info_arr = toolRecognition.locate()
for info in info_arr:
    msg.send_x(int(info.x_coord))
    time.sleep(3)
    msg.send_y(int(info.y_coord))
    time.sleep(3)
    print(info.class_id)

    # In the arm:
    # Pick the tool 
    # Show to second camera
    # Place to the box coordinates
    # Release

    # Check if the tool is placed (load cell, take from arduino)

    # If placed, go back to inspection point

# Loop: one loop = pick and place 1 whole tool.



