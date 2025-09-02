# YOLO -- Détection d'objets à partir d'une vidéo
# Visionnement du résultat de la détection.

import os
import cv2
os.system("clear")

def pause():
    programPause = input("Appuyez sur la touche Retour pour continuer...")

print("YOLO -- Détection d’objets à partir d’une vidéo")
pause()

# Path to YOLO output images
folder_path = 'runs_output/best_pred'  # Adjust as needed

# Collect and sort .jpg images
images = sorted([img for img in os.listdir(folder_path) if img.endswith(".jpg")])

# Check if images found
if not images:
    print("No .jpg images found in the folder.")
    exit()

# Slideshow speed (in milliseconds)
delay = 100  # ~10 FPS

# Fullscreen window
cv2.namedWindow("YOLO Fullscreen Slideshow", cv2.WINDOW_FULLSCREEN)

while True:
    for img_name in images:
        img_path = os.path.join(folder_path, img_name)
        img = cv2.imread(img_path)

        if img is None:
            print(f"Failed to load {img_path}, skipping.")
            continue

        cv2.imshow("YOLO Fullscreen Slideshow", img)

        # Press 'q' to quit
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            exit()
