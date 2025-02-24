# Simulateur de Jardin Virtuel 🌱

## Description
Ce projet est un simulateur de jardin virtuel où l'utilisateur peut planter, entretenir et observer la croissance de ses plantes.
Il inclut une interface graphique réalisée avec Tkinter et gère des événements aléatoires pouvant affecter le jardin.

## Fonctionnalités
- Planter et entretenir différentes plantes 🌿
- Arroser, exposer au soleil et fertiliser les plantes ☀️💧
- Gestion d'événements aléatoires (tempêtes, parasites, sécheresse) ⚡
- Sauvegarde et chargement de l'état du jardin 💾

## Installation
### Prérequis
Assurez-vous d'avoir **Python 3.x** installé sur votre machine.

### Cloner le projet
```bash
git clone https://github.com/votre-repo/simulateur-jardin.git
cd simulateur-jardin
```

### Installer les dépendances
Aucune dépendance externe n'est requise car le projet utilise uniquement des bibliothèques standard de Python.

## Exécution du programme
Lancez le simulateur avec la commande suivante :
```bash
python main.py
```

## Structure du projet
```
/simulateur_jardin
│── /models
│   │── plante.py          # Gestion des plantes
│   │── jardin.py          # Gestion du jardin
│   │── evenement.py       # Gestion des événements
│── /controllers
│   │── gestion_jardin.py  # Interactions utilisateur
│── /gui
│   │── interface.py       # Interface graphique Tkinter
│── /data
│   │── sauvegarde.json    # Sauvegarde des données
│── main.py                # Point d'entrée du programme
│── README.md              # Documentation
```

## Auteurs
- **Votre Nom**

## Licence
Ce projet est sous licence MIT.