from send import Send
from tool_recognition import ToolRecognition
import time
from receive import Receive
send = Send()
toolRecognition = ToolRecognition()
receive = Receive()

# Inspect the tool (cam 1)

#Send the x and y coordinates to the robot arm
while True:
    status = receive.receive_from_arm()
    receive.connect_to_mqtt()
    if status == 1: # Observation point
        # TODO: Inspect

        # Observe
        x_coord, y_coord, class_id = toolRecognition.locate()[0]
        send.send_x(int(x_coord))
        time.sleep(3)
        send.send_y(int(y_coord))
        time.sleep(3)
        print(class_id)

        
    elif status == 2: # Inspection point 
        # TODO: Inspect
        pass

        # Send the type of the tool (which box to put)
        send.send_type(class_id)
        time.sleep(3)

        # Arm: goes to the respective box

        # Check if the tool is placed (load cell, take from arduino)
        # If placed, go back to inspection point
        while not receive.isPlaced == "placed":
            time.sleep(1)
        
        if receive.isPlaced == "placed":
            send.send_load_cell(1)
            time.sleep(3)