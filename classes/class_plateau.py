class Plateau:
    def __init__(self):
        self.zones_monstre_j1 = [None] * 5
        self.zones_monstre_j2 = [None] * 5

    def placer_carte(self, joueur, carte, zone, position=0):
        if zone == "monstre":
            if joueur == 1:
                self.zones_monstre_j1[position] = carte
            elif joueur == 2:
                self.zones_monstre_j2[position] = carte

    def retirer_carte(self, carte):
        for i, c in enumerate(self.zones_monstre_j1):
            if c == carte:
                self.zones_monstre_j1[i] = None
                return
        for i, c in enumerate(self.zones_monstre_j2):
            if c == carte:
                self.zones_monstre_j2[i] = None
                return


    def get_monstres_visibles(self, joueur):
        if joueur == 1:
            return self.zones_monstre_j1
        elif joueur == 2:
            return self.zones_monstre_j2
