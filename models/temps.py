import time
from models.jardin import Jardin

class Temps:
    def __init__(self):
        self.tour = 0
        self.periode = "Matin"
        self.periodes = ["Matin", "Après-midi", "Soir", "Nuit"]

    def avancer_temps(self, jardin):
        self.tour += 1
        self.periode = self.periodes[self.tour % len(self.periodes)]
        print(f"⏳ Tour {self.tour} - Période: {self.periode}")
        self.effet_du_temps(jardin)

    def effet_du_temps(self, jardin):
        for plante in jardin.plantes:
            if self.periode in ["Matin", "Après-midi"]:
                plante.croissance = min(plante.croissance + 2, plante.croissance_max)
            if self.periode == "Nuit":
                plante.eau = max(plante.eau - 3, 0)
        print("🌿 Les plantes ont été affectées par le passage du temps.")