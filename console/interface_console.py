import time
from models.jardin import Jardin
from models.temps import Temps
from models.plante import Tomate, Tournesol, Carotte, Radis_noir, Aronia, Zingiber_spectabile
from controllers.gestion_jardin import PLANTES_DISPONIBLES

class InterfaceConsole:
    def __init__(self):
        self.jardin = Jardin()
        self.temps = Temps()

    def afficher_jardin(self):
        print("\n🌿 État actuel du jardin:")
        if not self.jardin.plantes:
            print("Aucune plante n'est présente.")
        else:
            for i, plante in enumerate(self.jardin.plantes):
                print(f"[{i+1}] {plante.nom} - Eau: {plante.eau}/{plante.eau_max}, Lumière: {plante.lumiere}/{plante.lumiere_max}, Croissance: {plante.croissance}/{plante.croissance_max}")

    def afficher_evenements_et_temps(self):
        print(f"\n⏳ Temps actuel: {self.temps.periode}")
        print("📢 Événements en cours: Aucun (À implémenter si besoin)")

    def menu_principal(self):
        while True:
            print("\n=== Menu Principal ===")
            print("1. Afficher le jardin")
            print("2. Planter une plante")
            print("3. Entretenir une plante (arroser, exposer au soleil, fertiliser)")
            print("4. Avancer le temps")
            print("5. Quitter")
            
            choix = input("Choisissez une option: ")
            
            if choix == "1":
                self.afficher_jardin()
            elif choix == "2":
                self.choisir_plante_a_planter()
            elif choix == "3":
                self.choisir_entretien_plante()
            elif choix == "4":
                self.avancer_temps()
            elif choix == "5":
                print("👋 Au revoir!")
                break
            else:
                print("⚠️ Option invalide, veuillez réessayer.")

    def choisir_plante_a_planter(self):
        print("\n🌱 Plantes disponibles:")
        liste_plantes = list(PLANTES_DISPONIBLES.keys())
        for idx, nom in enumerate(liste_plantes, start=1):
            print(f"- ({idx}) {nom}")
        
        choix = input("Entrez le numéro ou le nom de la plante à planter: ").strip().lower()

        if choix.isdigit():
            index = int(choix) - 1
            if 0 <= index < len(liste_plantes):
                choix = liste_plantes[index]
            else:
                print("⚠️ Numéro invalide.")
                return
        
        if choix in PLANTES_DISPONIBLES:
            nouvelle_plante = PLANTES_DISPONIBLES[choix]()
            self.jardin.ajouter_plante(nouvelle_plante)
            print(f"✅ Une {nouvelle_plante.nom} a été plantée !")
        else:
            print("⚠️ Plante inconnue, veuillez réessayer.")