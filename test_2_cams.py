import cv2
import os
from pathlib import Path
from ultralytics import YOLO

# Load YOLO models (ensure models are in the correct directory or path)
identify_model = YOLO('./models/last.pt')
inspection_model = YOLO('./models/best.pt')


# Create directory to save images
output_folder = 'test_2_cameras'
Path(output_folder).mkdir(exist_ok=True)

def capture_and_predict(camera_index, model1, model2, output_folder):
    CAMERA_WIDTH_PIXELS = 1280
    CAMERA_HEIGHT_PIXELS = 720

    # Initialize camera
    cap = cv2.VideoCapture(camera_index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH_PIXELS)  # Set the width
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT_PIXELS)  # Set the height

    if not cap.isOpened():
        print(f"Cannot open camera {camera_index}")
        return None, None
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    cap.release()
    cv2.imwrite("./images/1280-720.jpg", frame)

    CAMERA_WIDTH_PIXELS = 2560
    CAMERA_HEIGHT_PIXELS = 1440

    # Initialize camera
    cap = cv2.VideoCapture(camera_index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH_PIXELS)  # Set the width
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT_PIXELS)  # Set the height

    if not cap.isOpened():
        print(f"Cannot open camera {camera_index}")
        return None, None
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    cap.release()
    cv2.imwrite("./images/640-480.jpg", frame)

    if not ret:
        print(f"Failed to grab frame from camera {camera_index}")
        return None, None
    
    # Save image
    image_path = os.path.join(output_folder, f"camera_{camera_index}.jpg")
    cv2.imwrite(image_path, frame)

    # Run identify model (class detection)
    results = model1(frame)
    result = results[0]
    boxes = result.boxes.cpu().numpy()
    label = ""
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0].astype(int)
        class_id = box.cls[0].astype(int)
        conf = box.conf[0]
            
        # Draw bounding box and label
        label = f"{identify_model.names[class_id]} {conf:.2f}"

        # Run inspection model (stain detection) TODO: 
        results_inspect = model2.predict(frame)
        stain_detected = len(results_inspect) > 0  # True if any detections (stain present)

        return label, not stain_detected  # Returns class_detected, and False if any stains are detected

# Capture from two cameras, predict classes, and inspect for stains
# class_detected_cam1, is_clean_cam1 = capture_and_predict(0, identify_model, inspection_model, output_folder)
class_detected_cam2, is_clean_cam2 = capture_and_predict(1, identify_model, inspection_model, output_folder)

# Print results
# print(f"Camera 1 - Classes detected: {class_detected_cam1}, Is clean: {is_clean_cam1}")
print(f"Camera 2 - Classes detected: {class_detected_cam2}, Is clean: {is_clean_cam2}")
