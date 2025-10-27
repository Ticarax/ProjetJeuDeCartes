from classes.class_carte import Carte

class CarteMonstre(Carte):
    def __init__(self, nom, description, points_attaque, points_defense, niveau):
        super().__init__(nom, description)
        self.points_attaque = points_attaque
        self.points_defense = points_defense
        self.niveau = niveau
        self.position = "Attaque"

    def attaquer(self, monstre_cible):
        pass

    def changer_position(self):
        pass
