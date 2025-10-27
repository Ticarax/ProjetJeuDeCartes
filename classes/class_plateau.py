class Plateau:
    def __init__(self):
        self.zones_monstre_j1 = [None] * 5
        self.zones_magie_piege_j1 = [None] * 5
        self.zones_monstre_j2 = [None] * 5
        self.zones_magie_piege_j2 = [None] * 5

    def placer_carte(self, joueur, carte, zone, position=0):
        if joueur == 1:
            if zone == "monstre":
                self.zones_monstre_j1[position] = carte
            elif zone == "magie_piege":
                self.zones_magie_piege_j1[position] = carte
        elif joueur == 2:
            if zone == "monstre":
                self.zones_monstre_j2[position] = carte
            elif zone == "magie_piege":
                self.zones_magie_piege_j2[position] = carte

    def retirer_carte(self, carte):
        # This is a simplified version
        pass

    def get_monstres_visibles(self, joueur):
        if joueur == 1:
            return self.zones_monstre_j1
        elif joueur == 2:
            return self.zones_monstre_j2
