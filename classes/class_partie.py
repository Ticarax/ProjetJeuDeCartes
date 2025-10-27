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
        for _ in range(5):
            self.joueur1.piocher()
            self.joueur2.piocher()

    def prochaine_phase(self):
        self.phase_actuelle_index = (self.phase_actuelle_index + 1) % len(self.phases)
        if self.phases[self.phase_actuelle_index] == "Pioche":
            self.changer_tour()

    def changer_tour(self):
        if self.joueur_actuel == self.joueur1:
            self.joueur_actuel = self.joueur2
        else:
            self.joueur_actuel = self.joueur1
        self.joueur_actuel.piocher()

    def verifier_victoire(self):
        if self.joueur1.points_de_vie <= 0:
            return self.joueur2
        elif self.joueur2.points_de_vie <= 0:
            return self.joueur1
        return None
