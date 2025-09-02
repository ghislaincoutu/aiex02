# YOLO -- Détection d'objets à partir d'une vidéo
# Visionnement du résultat de la détection.

import os
from PIL import Image

def pause():
    programPause = input("Appuyez sur la touche Retour pour continuer...")

print("YOLO -- Détection d’objets à partir d’une vidéo")
pause()

# Path to YOLO output images
folder_path = 'runs/detect/best_pred'  # Adjust as needed
output_gif_path = 'yolo_output.gif'  # Output filename

# Get sorted list of .jpg files
images = sorted([f for f in os.listdir(folder_path) if f.endswith('.jpg')])

# Load images into a list
frames = [Image.open(os.path.join(folder_path, img)).convert("RGB") for img in images]

# Save as animated GIF
if frames:
    frames[0].save(
        output_gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=100,  # duration per frame in ms (~10 FPS)
        loop=0  # 0 = infinite loop
    )
    print(f"Saved GIF as {output_gif_path}")
else:
    print("No .jpg images found in the folder.")
