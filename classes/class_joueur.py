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
        # version simplier mais pas utiliser car fait differament dans la main page
        pass

    def poser_carte(self, carte, plateau):
        # version simplier mais pas utiliser car fait differament dans la main page
        pass

    def declarer_attaque(self, attaquant, defenseur, adversaire):
        resultat = attaquant.attaquer(defenseur)

        if resultat["dommages"] > 0:
            if resultat["attaquant_detruit"]:
                self.points_de_vie -= resultat["dommages"]
            else:
                adversaire.points_de_vie -= resultat["dommages"]
        
        return resultat
