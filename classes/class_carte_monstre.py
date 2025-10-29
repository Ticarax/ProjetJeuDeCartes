from classes.class_carte import Carte

class CarteMonstre(Carte):
    def __init__(self, nom, description, points_attaque, points_defense, niveau):
        super().__init__(nom, description)
        self.points_attaque = points_attaque
        self.points_defense = points_defense
        self.niveau = niveau
        self.position = "Attaque"
        self.renforcee = False
        self.a_attaque_ce_tour = False

    def attaquer(self, monstre_cible):
        resultat = {
            "attaquant_detruit": False,
            "defenseur_detruit": False,
            "dommages": 0
        }

        if monstre_cible.position == "Attaque":
            if self.points_attaque > monstre_cible.points_attaque:
                resultat["defenseur_detruit"] = True
                resultat["dommages"] = self.points_attaque - monstre_cible.points_attaque
            elif self.points_attaque < monstre_cible.points_attaque:
                resultat["attaquant_detruit"] = True
                resultat["dommages"] = monstre_cible.points_attaque - self.points_attaque
            else: # Égalité
                resultat["attaquant_detruit"] = True
                resultat["defenseur_detruit"] = True
        
        elif monstre_cible.position == "Défense":
            if self.points_attaque > monstre_cible.points_defense:
                resultat["defenseur_detruit"] = True
            elif self.points_attaque < monstre_cible.points_defense:
                resultat["dommages"] = monstre_cible.points_defense - self.points_attaque
        
        return resultat

    def changer_position(self):
        if self.position == "Attaque":
            self.position = "Défense"
        else:
            self.position = "Attaque"

    def jouer(self, proprietaire):
        # For now, playing a monster card does nothing special
        pass
