from classes.class_carte import Carte

class CarteMagie(Carte):
    def __init__(self, nom, description, type_effet):
        super().__init__(nom, description)
        self.type_effet = type_effet

    def activer_effet(self, partie, cible):
        pass
