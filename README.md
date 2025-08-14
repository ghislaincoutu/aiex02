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
```

## Création d’un environnement virtuel Python3
```sh
cd /var
sudo mkdir aiex02
sudo chown $USER:$USER aiex02
cd /var/aiex02
python3 -m venv ai02
source /var/aiex02/ai02/bin/activate
```
Saisir la commande `deactivate` pour sortir de l’environnement virtuel Python3.

Commande pour activer l’environnemnet virtuel Python3 à partir du script `activate_venv.sh`.
```sh
cd /var/aiex02
source ./activate_venv.sh
```

## Installation de YOLO et de ses dépendances
```sh
source /var/aiex02/ai02/bin/activate
pip install --upgrade pip
pip install ultralytics
pip install opencv-python
```
