from abc import ABC, abstractmethod

class Carte(ABC):
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description

    @abstractmethod
    def jouer(self, proprietaire):
        pass
