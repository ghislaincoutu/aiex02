#!/bin/bash

function apply_pause() {
    read -p "$*"
}

echo "Activation de l’environnement virtuel Python 3"
echo "Version du 2025-08-14"
apply_pause "Appuyer sur la touche [Retour] pour continuer..."

source /media/disk01/aiex02/ai02/bin/activate
