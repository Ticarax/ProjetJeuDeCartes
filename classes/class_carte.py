from abc import ABC, abstractmethod

class Carte(ABC):
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description

    @abstractmethod
    def jouer(self, proprietaire):
        pass

#la methode abstraite a etait proposer par un ia afin de securiser le bon fonctionnement et que les effet jouer son independant entre les class qui ont un heritage de de Carte
#la def jouer quand a elle sert a ce que les cartes pourrait avoir un effet au moment de la poser sur le plateau mais pour le cas present cette affet est inutiliser / ou autre mais pas d'idee
