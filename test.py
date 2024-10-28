from send import Send
import time
send = Send()

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
    send.send_x(100)

if __name__ == "__main__":
    main()
