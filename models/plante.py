class Plante:
    def __init__(self, nom, eau_max, lumiere_max, croissance_max):
        self.nom = nom
        self.eau = eau_max // 2
        self.lumiere = lumiere_max // 2
        self.croissance = 0
        self.eau_max = eau_max
        self.lumiere_max = lumiere_max
        self.croissance_max = croissance_max
        self.etat = "Jeune pousse"

    def arroser(self):
        self.eau = min(self.eau + 10, self.eau_max)
        print(f"💧 {self.nom} a été arrosée ! Eau actuelle: {self.eau}")

    def exposer_au_soleil(self):
        self.lumiere = min(self.lumiere + 5, self.lumiere_max)
        print(f"☀️ {self.nom} reçoit plus de lumière ! Lumière actuelle: {self.lumiere}")

    def fertiliser(self):
        self.croissance += 5
        print(f"🌱 {self.nom} a été fertilisée ! Croissance: {self.croissance}")

    def verifier_etat(self):
        if self.croissance >= self.croissance_max:
            self.etat = "Plante adulte"
        elif self.eau < 5 or self.lumiere < 5:
            self.etat = "En mauvaise santé"
        else:
            self.etat = "Jeune pousse"
        print(f"📊 {self.nom} - État: {self.etat} | Eau: {self.eau} | Lumière: {self.lumiere}")

# Ajout des types de plantes

class Tomate(Plante):
    def __init__(self):
        super().__init__("Tomate", eau_max=50, lumiere_max=30, croissance_max=100)

class Tournesol(Plante):
    def __init__(self):
        super().__init__("Tournesol", eau_max=40, lumiere_max=50, croissance_max=120)

class Carotte(Plante):
    def __init__(self):
        super().__init__("Carotte", eau_max=30, lumiere_max=20, croissance_max=90)