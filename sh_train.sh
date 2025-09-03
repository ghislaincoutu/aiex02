#!/bin/bash

function apply_pause() {
    read -p "$*"
}

echo "Entraînement du jeu de données vidéo"
echo "Version du 2025-09-02"
apply_pause "Appuyer sur la touche [Retour] pour continuer..."

yolo task=detect mode=train model=yolov8n.pt data=dataset02.yaml epochs=30 imgsz=640
