class Plante:
    def __init__(self, nom, eau_max, lumiere_max, croissance_max, fertilite_min):
        self.nom = nom
        self.eau = eau_max // 2
        self.lumiere = lumiere_max // 2
        self.croissance = 0
        self.eau_max = eau_max
        self.lumiere_max = lumiere_max
        self.croissance_max = croissance_max
        self.fertilite_min = fertilite_min  # Seuil de fertilité minimum pour survivre
        self.fertilite = 10  # Valeur de fertilité de base
        self.etat = "Jeune pousse"

    def arroser(self):
        self.eau = min(self.eau + 10, self.eau_max)
        print(f"💧 {self.nom} a été arrosée ! Eau actuelle: {self.eau}")

    def exposer_au_soleil(self):
        self.lumiere = min(self.lumiere + 5, self.lumiere_max)
        print(f"☀️ {self.nom} reçoit plus de lumière ! Lumière actuelle: {self.lumiere}")

    def fertiliser(self):
        self.fertilite = min(self.fertilite + 5, 20)  # Fertilité max fixée à 20
        print(f"🌱 {self.nom} a été fertilisée ! Fertilité: {self.fertilite}")

    def verifier_etat(self):
        if self.eau <= 0:
            print(f"💀 {self.nom} est morte de déshydratation !")
            return False
        if self.fertilite < self.fertilite_min:
            print(f"💀 {self.nom} est morte car le sol est trop pauvre !")
            return False
        if self.croissance >= self.croissance_max:
            self.etat = "Plante adulte"
        elif self.eau < 5 or self.lumiere < 5 or self.fertilite < 5:
            self.etat = "En mauvaise santé"
        else:
            self.etat = "Jeune pousse"
        return True
    
# Ajout des types de plantes

class Tomate(Plante):
    def __init__(self):
        super().__init__("Tomate", eau_max=50, lumiere_max=30, croissance_max=100, fertilite_min=5)

class Tournesol(Plante):
    def __init__(self):
        super().__init__("Tournesol", eau_max=40, lumiere_max=50, croissance_max=120, fertilite_min=5)

class Carotte(Plante):
    def __init__(self):
        super().__init__("Carotte", eau_max=30, lumiere_max=20, croissance_max=90, fertilite_min=5)
        
class Radis_noir(Plante):
    def __init__(self):
        super().__init__("Radis noir", eau_max=30, lumiere_max=25, croissance_max=80, fertilite_min=5)
        
class Aronia(Plante):
    def __init__(self):
        super().__init__("Aronia", eau_max=25, lumiere_max=30, croissance_max=60, fertilite_min=5)
        
class Zingiber_spectabile(Plante):
    def __init__(self):
        super().__init__("Zingiber spectabile", eau_max=80, lumiere_max=30, croissance_max=200, fertilite_min=5)