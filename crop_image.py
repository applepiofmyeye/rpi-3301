import cv2
from ultralytics import YOLO
import numpy as np
import os

# Define the input image path
input_image_path = "./img.jpg"

# Load the image
frame = cv2.imread(input_image_path)
if frame is None:
    print("Failed to load image.")
else:
    # Define crop area (adjust these values as needed)
    x_start, y_start, x_end, y_end = 92, 29, 1187, 674
    cropped_frame = frame[y_start:y_end, x_start:x_end]

    # Create 'images' folder if it doesn't exist
    output_folder = "images"
    os.makedirs(output_folder, exist_ok=True)

    # Initialize YOLOv8 model
    # model = YOLO("yolov8n.pt")  # Replace with your specific YOLOv8 model

    # Counter for image naming
    counter = 0

    # Save the raw cropped image
    raw_image_path = os.path.join(output_folder, f"raw_0{counter}.jpg")
    cv2.imwrite(raw_image_path, cropped_frame)

    # Run YOLOv8 inference on the cropped image
    # results = model(cropped_frame)

    # Draw bounding boxes on a copy of the cropped frame
    drawn_frame = cropped_frame.copy()


    x1, y1, x2, y2 = 0, 0, 640, 480
    # Draw bounding box
    cv2.rectangle(drawn_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Save the image with bounding boxes
    drawn_image_path = os.path.join(output_folder, f"drawn_0{counter}.jpg")
    cv2.imwrite(drawn_image_path, drawn_frame)

    # Optional: Display the image with bounding boxes in a window
    cv2.imshow("YOLOv8 Detection", drawn_frame)
    cv2.waitKey(0)  # Press any key to close the window

    # Cleanup
    cv2.destroyAllWindows()
