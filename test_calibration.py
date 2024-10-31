from tool_recognition import ToolRecognition
import time
toolRecognition = ToolRecognition()

results = toolRecognition.locate()
if len(results) == 0:
    print("No tool detected")
else:
    x, y, class_id = results[0]
    print("x", x, "y", y, "class_id", class_id)

