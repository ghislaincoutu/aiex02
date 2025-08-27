path=/media/disk01/aiex02/runs/detect/best_pred
ffmpeg -framerate 10 -i $path/frame_%06d.jpg -c:v libx264 -pix_fmt yuv420p yolo_output.mp4
