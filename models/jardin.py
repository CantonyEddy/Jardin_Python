from models.plante import Plante


class Jardin:
    def __init__(self):
        self.plantes = []

    def ajouter_plante(self, plante):
        self.plantes.append(plante)
        print(f"🌿 {plante.nom} a été plantée dans le jardin.")

    def afficher_plantes(self):
        if not self.plantes:
            print("🌱 Le jardin est vide.")
        else:
            print("\n🌳 État du jardin 🌳")
            for plante in self.plantes:
                plante.verifier_etat()

    def sauvegarder_jardin(self, fichier="data/save.json"):
        import json
        with open(fichier, "w") as f:
            json.dump([vars(plante) for plante in self.plantes], f)
        print("💾 Jardin sauvegardé.")

    def charger_jardin(self, fichier="data/save.json"):
        import json
        try:
            with open(fichier, "r") as f:
                data = json.load(f)
                self.plantes = [Plante(**plante) for plante in data]
            print("📂 Jardin chargé avec succès.")
        except FileNotFoundError:
            print("⚠️ Aucun fichier de sauvegarde trouvé.")