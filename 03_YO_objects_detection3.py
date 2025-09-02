# YOLO -- Détection d'objets à partir d'une vidéo

import os
from ultralytics import YOLO
os.system("clear")

def pause():
    programPause = input("Appuyez sur la touche Retour pour continuer...")

print("YOLO -- Détection d’objets à partir d’une vidéo")
pause()

# --- Paths ---
image_dir = 'dataset01/images/val'  # folder of test images
model_best = 'runs/detect/train/weights/best.pt'
model_last = 'runs/detect/train/weights/last.pt'

# Output directories
output_best = 'runs_output/best_pred'
output_last = 'runs_output/last_pred'

print("Running detection with best.pt...")
pause()
yolo_best = YOLO(model_best)
yolo_best.predict(source=image_dir, save=True, project='runs/detect', name='best_pred', exist_ok=True)

print("Running detection with last.pt...")
pause()
yolo_last = YOLO(model_last)
yolo_last.predict(source=image_dir, save=True, project='runs/detect', name='last_pred', exist_ok=True)

print("Detection complete. Check folders:")
print(f"Best model predictions: {output_best}")
print(f"Last model predictions: {output_last}")
