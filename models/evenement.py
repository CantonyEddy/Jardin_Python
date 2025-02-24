import random

class Evenement:
    @staticmethod
    def evenement_aleatoire(jardin):
        evenements = [
            ("🌩 Tempête ! Certaines plantes perdent de l'eau.", lambda p: setattr(p, 'eau', max(0, p.eau - 5))),
            ("🔥 Canicule ! Les plantes ont besoin d'eau.", lambda p: setattr(p, 'eau', max(0, p.eau - 10))),
            ("🐛 Insectes nuisibles ! Certaines plantes cessent de croître.", lambda p: setattr(p, 'croissance', max(0, p.croissance - 5)))
        ]
        event, effet = random.choice(evenements)
        print("\n⚠️ Événement :", event)
        for plante in jardin.plantes:
            effet(plante)
