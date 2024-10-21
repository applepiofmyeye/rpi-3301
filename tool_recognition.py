import cv2
import numpy as np
from ultralytics import YOLO
import time
import uuid


class Camera:
    # Function to capture a single frame using OpenCV
    CAMERA_WIDTH_MM = 240 
    CAMERA_HEIGHT_MM = 180 
    CAMERA_WIDTH_PIXELS = 640
    CAMERA_HEIGHT_PIXELS = 480
    def __init__(self):
        pass

    def capture_single_frame(self):
        cap = cv2.VideoCapture(0)  # Open the default camera (index 0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.CAMERA_WIDTH_PIXELS)  # Set the width
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.CAMERA_HEIGHT_PIXELS)  # Set the height

        if not cap.isOpened():
            print("Error: Could not open camera.")
            return None

        ret, frame = cap.read()  # Capture a single frame
        cap.release()  # Release the camera after capturing the frame

        if not ret:
            print("Error: Failed to capture frame.")
            return None

        return frame

class Info:
    def __init__(self, x, y, type, cropped_img):
        self.x_coord = x
        self.y_coord = y
        self.type = type
        self.cropped_img = cropped_img

    def __iter__(self):
        return iter((self.x_coord, self.y_coord, self.type))

class ToolRecognition:
    # Load your custom YOLOv8 model
    camera = Camera()
    def __init__(self):
        self.info = []
        self.identify_model = YOLO('./models/last.pt') 
        self.inspect_model = YOLO('./models/best.pt')

    def locate(self):
        """
            This function gets the x and y coordinate of the tool
            - Gets input from camera 
            - Runs YOLOv8 inference on the input
            - Processes the results
            - Sends the x and y coordinates (in mm) to the raspberry pi
        """
        
        frame = None

        while frame is None:
            frame = self.camera.capture_single_frame()
            
        if frame is not None:
            # Run YOLOv8 inference on the captured frame
            results = self.identify_model.predict(frame)
            # Process first results
            # for result in results:
            result = results[0]
            boxes = result.boxes.cpu().numpy()
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].astype(int)
                class_id = box.cls[0].astype(int)
                conf = box.conf[0]
                    
                # Draw bounding box and label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f"{self.identify_model.names[class_id]} {conf:.2f}"
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                # Crop image
                cropped_img = frame [y1:y2, x1:x2]
                    
                # Print detection data
                print(f"Detected {label} at coordinates: ({x1}, {y1}, {x2}, {y2})")
                x_mm = int((x1 + x2) / 2) 
                y_mm = int((y1 + y2) / 2) 
                self.info.append(Info(x_mm, y_mm, class_id, cropped_img))
                    
                print(f"Center of the tool is at ({x_mm}, {y_mm})")
            

            image_id = str(uuid.uuid1())
            cv2.imwrite(f"./images/{image_id}.jpg", frame)
        else:
            print("No frame to process.")
        return self.info
    

    def isClean(self, cropped_img):
        """
            This function gets the cleaniness of the tool
            - Gets input from camera 
            - Runs YOLOv8 inference on the input
            - Processes the results
            - Sends whether there were results or not to the raspberry pi
        """
        if cropped_img is None:
            print("No image to process.")
            return False
        
        results = self.inspect_model.predict(cropped_img)

        if len(results) > 0:
            print("Tool is dirty")
            return False
        else:
            print("Tool is clean.")
            return True
    
    
