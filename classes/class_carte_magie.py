from classes.class_carte import Carte

class CarteMagie(Carte):
    def __init__(self, nom, description, type_effet):
        super().__init__(nom, description)
        self.type_effet = type_effet

    def activer_effet(self, partie, cible):
        return f"L'effet de la carte {self.nom} a été activé."

    def jouer(self, proprietaire):
        # For now, playing a magic card activates its effect immediately
        return self.activer_effet(None, None)

