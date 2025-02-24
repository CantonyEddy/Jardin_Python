class Jardin:
    def __init__(self):
        self.plantes = []
    
    def ajouter_plante(self, plante):
        self.plantes.append(plante)
        print(f"🌱 {plante.nom} a été ajoutée au jardin !")
    
    def verifier_etat_du_jardin(self):
        plantes_vivantes = []
        for plante in self.plantes:
            if plante.verifier_etat():
                plantes_vivantes.append(plante)
            else:
                print(f"💀 {plante.nom} a été retirée du jardin car elle est morte.")
        self.plantes = plantes_vivantes
    
    def afficher_jardin(self):
        if not self.plantes:
            print("🌿 Le jardin est vide.")
        else:
            print("\n🌱 État actuel du jardin :")
            for plante in self.plantes:
                print(f"- {plante.nom} | Eau: {plante.eau}/{plante.eau_max} | Lumière: {plante.lumiere}/{plante.lumiere_max} | Fertilité: {plante.fertilite}")