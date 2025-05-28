from ultralytics import YOLO
import cv2
import torch

# Load the model
model = YOLO('yolov8s.pt')  # You can replace this with 'yolov5m.pt', 'yolov5l.pt', etc. for larger models

def get_ingredients_from_image(image):
    img = cv2.imread(image)
    results = model(img)
    
    detected_classes = []

# Extract the detected classes
    for result in results:
        class_ids = result.boxes.cls  # Get class IDs for detected objects
        for cls_id in class_ids:
            class_name = result.names[int(cls_id)]  # Convert class ID to class name
            detected_classes.append(class_name) 

    return detected_classes

# print(get_ingredients_from_image('fruits.jpg'))