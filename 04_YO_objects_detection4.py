# YOLO -- Détection d'objets à partir d'une vidéo
# Visionnement du résultat de la détection.

import os
import cv2
import time

os.system("clear")

def pause():
    programPause = input("Appuyez sur la touche Retour pour continuer...")

print("YOLO -- Détection d’objets à partir d’une vidéo")
pause()

# Set your YOLO output folder path
folder_path = 'runs_output/best_pred'  # Adjust as needed

# Get all JPG images, sorted
images = sorted([img for img in os.listdir(folder_path) if img.endswith(".jpg")])

# Slideshow settings
delay = 100  # milliseconds between frames (e.g., 100 = 10 FPS)

# Create OpenCV window
#cv2.namedWindow("YOLO Slideshow", cv2.WINDOW_NORMAL)
cv2.namedWindow("YOLO Slideshow", cv2.WINDOW_FULLSCREEN)

for img_name in images:
    img_path = os.path.join(folder_path, img_name)
    img = cv2.imread(img_path)

    if img is None:
        print(f"Could not read {img_path}, skipping.")
        continue

    cv2.imshow("YOLO Slideshow", img)
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break  # Press 'q' to exit early

cv2.destroyAllWindows()
