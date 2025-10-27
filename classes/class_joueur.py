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
            return carte
        else:
            return None

    def invoquer_monstre(self, monstre, plateau):
        # This is a simplified version
        pass

    def poser_carte(self, carte, plateau):
        # This is a simplified version
        pass

    def declarer_attaque(self, attaquant, defenseur):
        # This is a simplified version
        pass
