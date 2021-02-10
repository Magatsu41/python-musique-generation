# python-musique-generation
Un projet de test en python pour générer des mélodies

# Installation

## Package Mingus

Commencez par installer le package Mingus depuis votre shell python :

pip install mingus

Documentation de Mingus : https://bspaans.github.io/python-mingus/

## Librairie fluidsynth

Téléchargez la dernière release du Fluidsynth : https://github.com/FluidSynth/fluidsynth/releases

Décompressez l'archive à l'emplacement de votre choix puis ajouter ce dossier à votre PATH :
Sur Windows depuis les variables d'environnement.
Sur Linux en utilisant la commande : export PATH=$PATH,"chemin-vers-votre-dossier"

## La Soundfont General-MIDI

Télécharger la general-MIDI soundfont au format .sf2 : https://member.keymusician.com/Member/FluidR3_GM/index.html

Placez la à l'endroit de votre choix et remplacez dans les scripts python le chemin vers ce fichier sur l'initialisation de la variable fluidsynth (fluidsynth.init)

# A propos

Script créé par Magatsu

Chaine youtube : https://www.youtube.com/channel/UCINhR5bbd3A0q6QVkym4rTg