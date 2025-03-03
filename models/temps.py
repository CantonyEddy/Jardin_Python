import random
from models.evenement import LISTE_EVENEMENTS

class Temps:
    def __init__(self):
        self.tour = 0
        self.periode = "Matin"

    def avancer_temps(self, jardin):
        self.tour += 1
        if self.tour % 3 == 0:
            self.periode = "Soir"
        elif self.tour % 2 == 0:
            self.periode = "Après-midi"
        else:
            self.periode = "Matin"

        # 80% de chance d'un événement, 20% de journée calme
        if random.random() <= 0.8:
            evenement = random.choice(LISTE_EVENEMENTS)
            print(f"🌟 Événement : {evenement.nom} - {evenement.description}")
            evenement.appliquer(jardin)
        else:
            print("😊 Aujourd'hui, il ne se passe rien de spécial.")

        # Faire pousser les plantes et baisser eau/lumière
        for plante in jardin.plantes:
            plante.croissance += 2
            plante.eau = max(0, plante.eau - 3)
            plante.lumiere = max(0, plante.lumiere - 2)