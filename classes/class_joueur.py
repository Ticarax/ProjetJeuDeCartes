class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.points_de_vie = 4000
        self.deck = []
        self.main = []
        self.cimetiere = []

    def piocher(self):
        if len(self.deck) > 0:
            carte = self.deck.pop(0)
            self.main.append(carte)
            print(f"{self.nom} a pioché {carte.nom}")
        else:
            print(f"{self.nom} n'a plus de cartes à piocher.")

    def invoquer_monstre(self, monstre, plateau):
        # This is a simplified version
        print(f"{self.nom} a invoqué {monstre.nom}")

    def poser_carte(self, carte, plateau):
        # This is a simplified version
        print(f"{self.nom} a posé une carte.")

    def declarer_attaque(self, attaquant, defenseur):
        # This is a simplified version
        print(f"{self.nom} attaque avec {attaquant.nom} sur {defenseur.nom}")
