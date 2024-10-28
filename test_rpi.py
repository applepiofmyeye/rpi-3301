import cv2
import os

# Ensure the images directory exists
output_dir = './images'
os.makedirs(output_dir, exist_ok=True)

# Open the camera (0 is typically the default camera)
cap = cv2.VideoCapture(-1)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

# Capture a single frame
ret, frame = cap.read()

if ret:
    # Save the captured frame to the ./images directory
    image_path = os.path.join(output_dir, 'captured_image.jpg')
    cv2.imwrite(image_path, frame)
    print(f"Image saved at {image_path}")
else:
    print("Error: Could not capture the image.")

# Release the camera
cap.release()

# Optionally, close all OpenCV windows if any were opened
cv2.destroyAllWindows()

