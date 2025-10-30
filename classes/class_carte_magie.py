from classes.class_carte import Carte

class CarteMagie(Carte):
    def __init__(self, nom, description, type_effet, valeur=0):
        super().__init__(nom, description)
        self.type_effet = type_effet
        self.valeur = valeur

    def activer_effet(self, partie, cible):
        return {"type": self.type_effet, "valeur": self.valeur, "nom": self.nom}

    def jouer(self, proprietaire):
        return self.activer_effet(None, None)

