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

## Installation des applications complémentaires
```sh
sudo apt-get install vlc
sudo apt-get install ffmpeg
sudo apt-get install blender
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
source ./sh_activate_venv.sh
```

## Installation de YOLO et de ses dépendances
```sh
source /media/disk01/aiex02/ai02/bin/activate
pip install --upgrade pip
pip install ultralytics
pip install opencv-python
```

## Édition des jeux de données vidéo avec CVAT
Il est possible d’utiliser l’application CVAT sur une machine virtuelle, à partir d’une image Docker (avec Docker Compose). Pour installer CVAT, au préalable il faut avoir installé et configuré Docker pour environnement Linux sur la machine virtuelle.

### Procédure pour installer Docker Compose
```sh
sudo curl -L "https://github.com/docker/compose/releases/download/v2.39.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

### Procédure pour installer CVAT
```sh
cd /media/disk01/Docker/Compose/cvat
git clone https://github.com/cvat-ai/cvat
cd cvat
docker compose up -d
```

### Procédure pour créer un utilisateur CVAT local
```sh
docker exec -it cvat_server bash -ic 'python3 ~/manage.py createsuperuser'
```

Compte factice à créer :
```
Username: user831
Email: user831@debian831.local
Password: debian831
```

L’application est accessible à partir de l’adresse URL suivante :
```
http://localhost:8080
```

### Commande pour démarrer et arrêter CVAT
```sh
cd /media/disk01/Docker/Compose/cvat
docker compose up -d
docker compose down
```
