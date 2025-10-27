from classes.class_carte import Carte

class CartePiege(Carte):
    def __init__(self, nom, description):
        super().__init__(nom, description)

    def activer_effet(self, partie, cible):
        print(f"L'effet de la carte piège {self.nom} a été activé.")

    def jouer(self, proprietaire):
        # For now, playing a trap card does nothing until it is activated
        pass
