import time
from models.jardin import Jardin
from models.temps import Temps
from models.plante import Tomate, Tournesol, Carotte, Radis_noir, Aronia, Zingiber_spectabile
from controllers.gestion_jardin import PLANTES_DISPONIBLES
from controllers.sauvegarde import Sauvegarde

class InterfaceConsole:
    def __init__(self):
        self.jardin = Jardin()
        self.temps = Temps()
        self.actions_restantes = 4

        self.sauvegarde = Sauvegarde()
        self.sauvegarde.charger_jardin(self.jardin, PLANTES_DISPONIBLES)

    def afficher_jardin(self):
        print("\n🌿 État actuel du jardin:")
        if not self.jardin.plantes:
            print("Aucune plante n'est présente.")
        else:
            for i, plante in enumerate(self.jardin.plantes):
                plante.verifier_etat()
                print(f"[{i+1}] {plante.nom}")
                print(f"    - Eau : {plante.eau}/{plante.eau_max}")
                print(f"    - Lumière : {plante.lumiere}/{plante.lumiere_max}")
                print(f"    - Croissance : {plante.croissance}/{plante.croissance_max}")
                print(f"    - Fertilité : {plante.fertilite}")
                print(f"    - État : {plante.etat}")

    def menu_principal(self):
        while True:
            print(f"\n=== Menu Principal (Actions restantes : {self.actions_restantes}) ===")
            print("1. Afficher le jardin")
            print("2. Planter une plante")
            print("3. Entretenir une plante (arroser, exposer au soleil, fertiliser, insecticide)")
            print("4. Avancer le temps")
            print("5. Sauvegarder et quitter")
            print("6. Quitter sans sauvegarder")

            choix = input("Choisissez une option: ")

            if choix == "1":
                self.afficher_jardin()
            elif choix in ["2", "3"] and self.actions_restantes <= 0:
                print("❌ Vous avez utilisé toutes vos actions pour ce tour. Avancez le temps pour en récupérer !")
            elif choix == "2":
                self.choisir_plante_a_planter()
                self.actions_restantes -= 1
            elif choix == "3":
                self.choisir_entretien_plante()
                self.actions_restantes -= 1
            elif choix == "4":
                self.avancer_temps()
                self.actions_restantes = 4
            elif choix == "5":
                self.sauvegarder_et_quitter()
                break
            elif choix == "6":
                self.quitter_sans_sauvegarder()
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

    def choisir_entretien_plante(self):
        self.afficher_jardin()
        if not self.jardin.plantes:
            print("Aucune plante à entretenir.")
            return

        choix = input("Entrez le numéro ou le nom de la plante à entretenir: ").strip().lower()

        plante = None
        if choix.isdigit():
            index = int(choix) - 1
            if 0 <= index < len(self.jardin.plantes):
                plante = self.jardin.plantes[index]
            else:
                print("⚠️ Numéro invalide.")
                return
        else:
            for p in self.jardin.plantes:
                if p.nom.lower() == choix:
                    plante = p
                    break
            if plante is None:
                print("⚠️ Nom de plante invalide.")
                return

        print("\n🌿 Action pour la plante :", plante.nom)
        print("Actions possibles :")
        print("1. Arroser")
        print("2. Exposer au soleil")
        print("3. Fertiliser")
        print("4. Pulvériser de l'insecticide")

        action_choisie = input("Quelle action souhaitez-vous réaliser (entrez le numéro) ? ").strip()

        if action_choisie == "1":
            plante.arroser()
        elif action_choisie == "2":
            plante.exposer_au_soleil()
        elif action_choisie == "3":
            plante.fertiliser()
        elif action_choisie == "4":
            plante.croissance = max(0, plante.croissance - 5)
            plante.fertilite = max(0, plante.fertilite - 1)
            print(f"🐛 {plante.nom} a été traitée contre les parasites.")
        else:
            print("⚠️ Action inconnue.")

    def avancer_temps(self):
        self.temps.avancer_temps(self.jardin)
        self.jardin.verifier_etat_du_jardin()
        self.sauvegarde.sauvegarder_jardin(self.jardin)
        print(f"⏳ Le temps a avancé. Nous sommes maintenant en {self.temps.periode}.")
        self.afficher_jardin()

    def sauvegarder_et_quitter(self):
        self.sauvegarde.sauvegarder_jardin(self.jardin)
        self.sauvegarde.fermer()
        print("💾 Jardin sauvegardé. À bientôt !")

    def quitter_sans_sauvegarder(self):
        self.sauvegarde.fermer()
        print("👋 Vous avez quitté sans sauvegarder. À bientôt !")

if __name__ == "__main__":
    interface = InterfaceConsole()
    interface.menu_principal()