from classes.class_carte import Carte

class CarteMonstre(Carte):
    def __init__(self, nom, description, points_attaque, points_defense, niveau):
        super().__init__(nom, description)
        self.points_attaque = points_attaque
        self.points_defense = points_defense
        self.niveau = niveau
        self.position = "Attaque"

    def attaquer(self, monstre_cible):
        if monstre_cible.position == "Attaque":
            if self.points_attaque > monstre_cible.points_attaque:
                return "Attaquant gagne"
            elif self.points_attaque < monstre_cible.points_attaque:
                return "Défenseur gagne"
            else:
                return "Égalité"
        elif monstre_cible.position == "Défense":
            if self.points_attaque > monstre_cible.points_defense:
                return "Attaquant gagne"
            else:
                return "Défenseur gagne"

    def changer_position(self):
        if self.position == "Attaque":
            self.position = "Défense"
        else:
            self.position = "Attaque"

    def jouer(self, proprietaire):
        # For now, playing a monster card does nothing special
        pass
