from models.jardin import Jardin
from models.plante import Plante
from models.plante import Tomate, Tournesol, Carotte
from models.evenement import Evenement

PLANTES_DISPONIBLES = {
    "tomate": Tomate,
    "tournesol": Tournesol,
    "carotte": Carotte
}

def planter_une_plante(jardin):
    print("🌱 Plantes disponibles :")
    for nom in PLANTES_DISPONIBLES.keys():
        print(f"- {nom}")
    
    choix = input("Entrez le nom de la plante à planter : ").lower()
    if choix in PLANTES_DISPONIBLES:
        nouvelle_plante = PLANTES_DISPONIBLES[choix]()
        jardin.ajouter_plante(nouvelle_plante)
        print(f"✅ Vous avez planté une {nouvelle_plante.nom} !")
    else:
        print("⚠️ Plante inconnue. Veuillez réessayer.")
        
def choisir_plante(jardin):
    if not jardin.plantes:
        print("🌱 Il n'y a aucune plante dans le jardin.")
        return None
    
    print("📋 Liste des plantes disponibles :")
    for i, plante in enumerate(jardin.plantes):
        print(f"{i+1}. {plante.nom} - Eau: {plante.eau}, Lumière: {plante.lumiere}, Croissance: {plante.croissance}")
    
    choix = int(input("Entrez le numéro de la plante avec laquelle interagir : ")) - 1
    if 0 <= choix < len(jardin.plantes):
        return jardin.plantes[choix]
    else:
        print("⚠️ Choix invalide !")
        return None

def entretenir_plante(jardin, action):
    plante = choisir_plante(jardin)
    if plante:
        if action == "arroser":
            plante.arroser()
        elif action == "exposer_au_soleil":
            plante.exposer_au_soleil()
        elif action == "fertiliser":
            plante.fertiliser()
        print(f"✅ {plante.nom} a été {action}é(e) !")
    else:
        print("⚠️ Aucune action effectuée.")