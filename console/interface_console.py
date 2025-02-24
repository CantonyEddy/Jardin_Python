import time
from models.jardin import Jardin
from models.temps import Temps
from models.evenement import Evenement
from models.plante import Tomate, Tournesol, Carotte
from controllers.gestion_jardin import PLANTES_DISPONIBLES, entretenir_plante, planter_une_plante

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
        for nom in PLANTES_DISPONIBLES.keys():
            print(f"- {nom}")
        choix = input("Entrez le nom de la plante à planter: ").lower()
        if choix in PLANTES_DISPONIBLES:
            nouvelle_plante = PLANTES_DISPONIBLES[choix]()
            self.jardin.ajouter_plante(nouvelle_plante)
            print(f"✅ Vous avez planté une {nouvelle_plante.nom}!")
        else:
            print("⚠️ Plante inconnue, veuillez réessayer.")

    def choisir_entretien_plante(self):
        self.afficher_jardin()
        if not self.jardin.plantes:
            return
        
        choix = int(input("Entrez le numéro de la plante à entretenir: ")) - 1
        if 0 <= choix < len(self.jardin.plantes):
            plante = self.jardin.plantes[choix]
            action = input("Choisissez une action (arroser, exposer_au_soleil, fertiliser): ").lower()
            entretenir_plante(self.jardin, action)
            print(f"✅ {plante.nom} a été {action}é(e)!")
        else:
            print("⚠️ Sélection invalide.")

    def avancer_temps(self):
        self.temps.avancer_temps(self.jardin)
        print(f"⏳ Le temps a avancé. Nous sommes maintenant en {self.temps.periode}.")
        self.afficher_jardin()

if __name__ == "__main__":
    interface = InterfaceConsole()
    interface.menu_principal()