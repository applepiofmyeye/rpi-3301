from send import Send
from tool_recognition import ToolRecognition
import time
from receive import Receive
send = Send()
toolRecognition = ToolRecognition()
receive = Receive()



# Inspect the tool (cam 1)
def main():
    """
        Steps:
        3. rpi receives status 1
        4. rpi inspects and observes
        5. rpi sends xy coords to arm

        10. rpi receives status 2
        11. rpi inspects
        12. rpi sends the type to the arm
        
        16. arduino reads load cell
        17. rpi receives load cell “tool is placed” from arduino
        18. rpi tells arm tool is placed
    """ 

    # Setup
    receive.connect_to_mqtt()

    #Send the x and y coordinates to the robot arm
    while True:
        # Wait for status 2
        status = receive.receive_from_arm()

        if status == 1: # Observation point
            # TODO: Inspect

            # Observe
            x_coord, y_coord, class_id = toolRecognition.locate()[0]

            # Send data to the robot arm
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

if __name__ == "__main__":
    main()