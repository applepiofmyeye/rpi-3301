import cv2
from ultralytics import YOLO
import os


# Define paths and output folder
input_folder = "./crop_these"
output_folder = "images"
os.makedirs(output_folder, exist_ok=True)

# Initialize counter
counter = 0

for file in os.listdir(input_folder):
    if file.endswith(".jpg"):
        # Construct full path for each image file
        input_image_path = os.path.join(input_folder, file)
        
        # Load the image
        frame = cv2.imread(input_image_path)
        if frame is None:
            print(f"Failed to load image: {file}")
            continue

        # Define crop area (adjust these values as needed)
        x_start, y_start, x_end, y_end = 92, 29, 1187, 674
        cropped_frame = frame[y_start:y_end, x_start:x_end]

        # Save the raw cropped image
        raw_image_path = os.path.join(output_folder, f"raw_{counter:02}.jpg")
        cv2.imwrite(raw_image_path, cropped_frame)
        
        # # Draw bounding boxes on a copy of the cropped frame
        # drawn_frame = cropped_frame.copy()

        # # Save the image with bounding boxes
        # drawn_image_path = os.path.join(output_folder, f"drawn_{counter:02}.jpg")
        # cv2.imwrite(drawn_image_path, drawn_frame)

        # Optional: Display the image with bounding boxes in a window
        # cv2.imshow("YOLOv8 Detection", drawn_frame)
        # cv2.waitKey(0)  # Press any key to close the window

        # Cleanup
        cv2.destroyAllWindows()

        # Increment counter
        counter += 1
