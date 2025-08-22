# aiex02
aiex02 — Expérimentations d’applications d’intelligence artificielle

## Dépôt Git
https://github.com/ghislaincoutu/aiex02

## Installation des modules Python3
```sh
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install python3-venv
sudo apt-get install python3-tk
sudo apt-get install blender
sudo apt-get install vlc
sudo apt-get install pyqt5-dev-tools
```

## Installation de FFmpeg
```sh
sudo apt-get install ffmpeg
```

## Création d’un environnement virtuel Python3
```sh
cd /media/disk01
sudo mkdir aiex02
sudo chown $USER:$USER aiex02
cd /media/disk01/aiex02
python3 -m venv ai02
source /media/disk01/aiex02/ai02/bin/activate
```
Saisir la commande `deactivate` pour sortir de l’environnement virtuel Python3.

Commande pour activer l’environnemnet virtuel Python3 à partir du script `activate_venv.sh`.
```sh
cd /media/disk01/aiex02
source ./activate_venv.sh
```

## Installation de YOLO et de ses dépendances
```sh
source /media/disk01/aiex02/ai02/bin/activate
pip install --upgrade pip
pip install ultralytics
pip install opencv-python
pip install lxml
pip install labelImg
```

## Commande pour démarrer LabelImg
```sh
labelImg
```
