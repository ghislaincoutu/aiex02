# YOLO -- Détection d'objets à partir d'une vidéo

import os
from ultralytics import YOLO
os.system("clear")

def pause():
    programPause = input("Appuyez sur la touche Retour pour continuer...")

print("YOLO -- Détection d’objets à partir d’une vidéo")
pause()

image_dir = 'dataset02/images/val'
model_best = 'runs/detect/train/weights/best.pt'
model_last = 'runs/detect/train/weights/last.pt'

output_best = 'runs_output/best_pred'
output_last = 'runs_output/last_pred'

print("Exécution de la détection avec l'option best.pt.")
pause()
yolo_best = YOLO(model_best)
yolo_best.predict(source=image_dir, save=True, project='runs_output', name='best_pred', exist_ok=True)

print("Exécution de la détection avec l'option last.pt.")
pause()
yolo_last = YOLO(model_last)
yolo_last.predict(source=image_dir, save=True, project='runs_output', name='last_pred', exist_ok=True)

print("Détection complétée.")
print(f"Meilleures prédictions du modèle enregistrées dans le dossier {output_best}")
print(f"Dernières prédictions du modèle enregistrées dans le dossier {output_last}")
