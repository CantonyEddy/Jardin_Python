import random

class Evenement:
    def __init__(self, nom, description, effet):
        self.nom = nom
        self.description = description
        self.effet = effet

    def appliquer(self, jardin):
        self.effet(jardin)


# Définition des effets des événements

def secheresse(jardin):
    for plante in jardin.plantes:
        plante.eau = max(0, plante.eau - 10)
    print("☀️ Une sécheresse frappe le jardin ! Les plantes perdent beaucoup d’eau.")

def invasion_parasites(jardin):
    if jardin.plantes:
        victime = random.choice(jardin.plantes)
        victime.croissance = max(0, victime.croissance - 10)
        print(f"🐛 Une invasion de parasites attaque {victime.nom} qui perd de la croissance.")

def pluie_abondante(jardin):
    for plante in jardin.plantes:
        plante.eau = min(plante.eau + 10, plante.eau_max)
    print("🌧️ Une pluie abondante arrose tout le jardin !")

def sol_enrichi(jardin):
    for plante in jardin.plantes:
        plante.fertilite = min(plante.fertilite + 5, 20)
    print("🌿 Le sol est enrichi naturellement ! Les plantes gagnent de la fertilité.")

def canicule(jardin):
    for plante in jardin.plantes:
        plante.eau = max(0, plante.eau - 5)
        plante.fertilite = max(0, plante.fertilite - 3)
    print("🔥 Une canicule frappe ! Eau et fertilité baissent plus vite.")

def aucun_evenement(jardin):
    print("😊 Aucun événement particulier aujourd'hui, tout est calme.")

# Liste globale des événements
LISTE_EVENEMENTS = [
    Evenement("Sécheresse", "Les plantes perdent beaucoup d’eau.", secheresse),
    Evenement("Invasion de parasites", "Une plante perd de la croissance.", invasion_parasites),
    Evenement("Pluie abondante", "Toutes les plantes gagnent de l’eau.", pluie_abondante),
    Evenement("Sol enrichi", "Le sol devient plus fertile.", sol_enrichi),
    Evenement("Canicule", "Eau et fertilité baissent plus vite.", canicule),
    Evenement("Rien", "Rien de spécial aujourd’hui.", aucun_evenement)
]