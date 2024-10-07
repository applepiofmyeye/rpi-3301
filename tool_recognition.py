import cv2
import numpy as np
from ultralytics import YOLO
import time


class Camera:
    # Function to capture a single frame using OpenCV
    CAMERA_WIDTH_MM = 481
    CAMERA_HEIGHT_MM = 351 
    CAMERA_WIDTH_PIXELS = 640
    CAMERA_HEIGHT_PIXELS = 480
    
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

class ToolRecognition:
    # Load your custom YOLOv8 model
    
    def __init__(self):
        self.x_coord = 0.00
        self.y_coord = 0.00
        self.model = YOLO('path/to/your/custom_model.pt')

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
            frame = Camera.capture_single_frame()
            
            if frame is not None:
                # Run YOLOv8 inference on the captured frame
                results = self.model(frame)
                
                # Process results
                for result in results:
                    boxes = result.boxes.cpu().numpy()
                    for box in boxes:
                        x1, y1, x2, y2 = box.xyxy[0].astype(int)
                        class_id = box.cls[0].astype(int)
                        conf = box.conf[0]
                        
                        # Draw bounding box and label
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        label = f"{self.model.names[class_id]} {conf:.2f}"
                        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                        
                        # Print detection data
                        print(f"Detected {label} at coordinates: ({x1}, {y1}, {x2}, {y2})")
                        x_pix = (x1 + x2) / 2
                        y_pix = (y1 + y2) / 2

                        x_mm = (x_pix / self.CAMERA_WIDTH_PIXELS) * self.CAMERA_WIDTH_MM 
                        y_mm = (y_pix / self.CAMERA_HEIGHT_PIXELS) * self.CAMERA_HEIGHT_MM
                        self.x_coord = x_mm
                        self.y_coord = y_mm
                        
                        print(f"Center of the tool is at ({self.x_coord}, {self.y_coord})")
                
                # Display the frame with YOLO detection results
                cv2.imshow('YOLOv8 Object Detection', frame)
                cv2.waitKey(0)  # Wait for a key press to close the window
                cv2.destroyAllWindows()
                self.send()

            else:
                print("No frame to process.")
