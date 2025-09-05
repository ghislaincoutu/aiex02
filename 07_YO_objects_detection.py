# YOLO -- Détection d'objets à partir d'une vidéo
# Visionnement du résultat de la détection.

import os
import cv2
from ultralytics import YOLO
os.system("clear")

def pause():
    programPause = input("Appuyez sur la touche Retour pour continuer...")

print("YOLO -- Détection d’objets à partir d’une vidéo")
pause()

# Load the custom trained YOLO model
model = YOLO("runs/detect/train/weights/best.pt")

# Open the video file
video_path = "medias/GeoShapes02-0001-0220.mp4"
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error opening video file")

# Loop over video frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO inference on the frame
    results = model(frame)

    # Visualize results on the frame
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("YOLO Detection", annotated_frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
