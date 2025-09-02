#!/bin/bash

function apply_pause() {
    read -p "$*"
}

echo "Conversion des images annotées au format MP4"
echo "Version du 2025-09-02"
apply_pause "Appuyer sur la touche [Retour] pour continuer..."

path=/media/disk01/aiex02/runs_output/best_pred
ffmpeg -framerate 24 -i $path/frame_%06d.jpg -c:v libx264 -pix_fmt yuv420p yolo_output.mp4
