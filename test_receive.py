from receive import Receive
import time 
receive = Receive()
print("waiting.", end="")
while True:
    time.sleep(2)
    print(receive.receive_from_arm())
