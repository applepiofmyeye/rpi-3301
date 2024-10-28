from send import Send
from tool_recognition import ToolRecognition
import time
from receive import Receive
from RPi import GPIO
send = Send()
toolRecognition = ToolRecognition()
receive = Receive()

model_classes = ["Scissors", "Scalpel", "Scissors", "Scissors"]
communicated_classes = ["", "Scissors", "Scalpel", "Dirty"]

def translate_tool_class(model_class):
    if model_class > 1 or model_class == 0:
        return 1
    else:
        return 2

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
    """ 

    #Send the x and y coordinates to the robot arm
    while True:
        # Wait for status 1
        status = receive.receive_from_arm()

        if status == 1: # Observation point
            """
                Observe before inspecting: so that all the tools have been initialised.
            """
            # Observe, get the first one detected.
            print("Observing...")
            results = toolRecognition.locate()
            if len(results) == 0:
                print("No tool detected")
                continue
            
            x_coord, y_coord, class_id, img = results[0]

            #Inspect
            isClean = toolRecognition.isClean(img)

            # Get the actual class_id of the tool if it's clean, else it's dirty (class 3)
            class_id = translate_tool_class(class_id) if isClean else 3

            print(f"Picking the tool at: {x_coord}, {y_coord}, with type: {communicated_classes[class_id]}")

            # Send data to the robot arm
            send.send_x(int(x_coord))
            send.send_x(315)
            time.sleep(3)
            send.send_y(-212)
            send.send_y(int(y_coord))
            time.sleep(2)
            print(class_id)
        elif status == 2:
            isClean = toolRecognition.isClean_takePicture()
            class_id = class_id if isClean else 3

            print(f"Inspected the tool at with type: {communicated_classes[class_id]}, clean?: {isClean}")



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
