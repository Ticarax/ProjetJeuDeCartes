from classes.class_carte import Carte

class CartePiege(Carte):
    def __init__(self, nom, description):
        super().__init__(nom, description)

    def activer_effet(self, partie, cible):
        pass
