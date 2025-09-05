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

# Load your custom YOLO model
model = YOLO("runs/detect/train/weights/best.pt")

# Load video
video_path = "medias/GeoShapes02-0001-0220.mp4"
cap = cv2.VideoCapture(video_path)

# Get video properties
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)

# Set up output video writer
out = cv2.VideoWriter(
    "output/result.mp4", 
    cv2.VideoWriter_fourcc(*'mp4v'), 
    fps, 
    (width, height)
)

# Process each frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame)

    # Draw detections on the frame
    annotated_frame = results[0].plot()

    # Show (optional)
    cv2.imshow("YOLO Detection", annotated_frame)

    # Write frame to output video
    out.write(annotated_frame)

    # Press Q to quit early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
out.release()
cv2.destroyAllWindows()
