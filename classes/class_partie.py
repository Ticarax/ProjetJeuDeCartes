from classes.class_joueur import Joueur
from classes.class_plateau import Plateau

class Partie:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.plateau = Plateau()
        self.joueur_actuel = joueur1
        self.phase_actuelle = "Pioche"

    def demarrer_partie(self):
        pass

    def prochaine_phase(self):
        pass

    def changer_tour(self):
        pass

    def verifier_victoire(self):
        pass
