# YOLO -- Détection d'objets à partir d'une image

import os
import cv2
from ultralytics import YOLO
os.system("clear")

def pause():
    programPause = input("Appuyez sur la touche Retour pour continuer...")

print("YOLO -- Détection d’objets à partir d’une image")
pause()

# Load a pre-trained YOLOv8 model
#model = YOLO('yolov8n.pt')  # 'yolov8n.pt' is the nano version, good for quick examples
model = YOLO('yolov9c.pt')

# Load an image
image_path = 'medias/geoshapes01.png'
img = cv2.imread(image_path)

# Perform object detection
results = model(img)

# Iterate through detected objects and draw bounding boxes
for r in results:
    boxes = r.boxes  # Bounding boxes
    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0]) # Get coordinates
        confidence = box.conf[0] # Confidence score
        class_id = int(box.cls[0]) # Class ID
        class_name = model.names[class_id] # Get class name

        # Draw rectangle
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2) # Green rectangle

        # Put label
        label = f'{class_name} {confidence:.2f}'
        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the image with detections
cv2.imshow('YOLO Object Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()