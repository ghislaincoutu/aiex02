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

### Norme de formatage des vidéos
Voici la norme de formatage des vidéos que j’ai adoptée pour effectuer mes tests.

- Résolution : 960 sur 540 pixels (1920 sur 1080 pixels / 2)
- Nombre d’images par seconde : 24

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
Compte utilisateur local à créer :
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

### Format d’exportation d’un jeux de données vidéo à partir de CVAT
À partir de CVAT, les jeux de données vidéo doivent être exportés au format _Ultrasonic YOLO Detection 1.0_.


## Préparation d’un jeux de données personnalisé
Après avoir exporté le jeux de données annotés à partir de CVAT, il faut importer les images et les étiquettes dans le dossier `aiex02`.

### Structure recommandée
Voici la structure qu’il faut adopter pour enregistrer les images et les étiquettes dans le dossier `aiex02`.
```sh
dataset01/
├── images/
│   ├── train/
│   ├── val/
├── labels/
│   ├── train/
│   ├── val/
└── data.yaml
```

Le contenu du fichier `dataset01.yalm` doit contenir les directives suivantes :
```sh
path: ./dataset01
train: images/train
val: images/val

nc: 2  # Nombre de classes
names: ['worker', 'cone']  # Noms des classes
```

### Commande à exécuter
Après avoir enregistré les images et les étiquettes dans le dossier `dataset01` et créé le fichier `dataset.yalm`, exécuter la commande suivante :
```sh
yolo task=detect mode=train model=yolov8n.pt data=dataset01.yaml epochs=30 imgsz=640
```
La commande va procéder à l’entraînement du jeu de données vidéo et va enregistrer le résultat de l’entraînement dans le sous-répertoire `aiex02/runs/detect/train`. À chaque entraînement, on peut supprimer le dossier `aiex02/runs/detect/train` avant de recommencer.

Un minimum de 30 époques (_epochs_) est requis pour que l’entraînement du jeu de données vidéo soit réussi.

### Erreurs à éviter
Si une vidéo annotée contient un objet à détecter qui est hors scène au début de la vidéo, les première étiquettes seront incomplètes. Pour que l’entraînement du jeu de données vidéo fonctionne correctement, il faut que les étiquettes soient pleinement renseignées dès le départ. Si trois objets ont été annotés dans le jeu de données vidéo, il faut donc que les étiquettes (les fichiers textes) contiennent trois lignes de coordonnées. Autrement un bogue se produit lors de l’entraînement du jeu de données.
