from classes.class_joueur import Joueur
from classes.class_plateau import Plateau

class Partie:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.plateau = Plateau()
        self.joueur_actuel = joueur1
        self.phases = ["Pioche", "Principale", "Combat"]
        self.phase_actuelle_index = 0

    def demarrer_partie(self):
        for _ in range(5):
            self.joueur1.piocher()
            self.joueur2.piocher()

    def prochaine_phase(self):
        self.phase_actuelle_index = (self.phase_actuelle_index + 1) % len(self.phases)
        if self.phases[self.phase_actuelle_index] == "Pioche":
            self.changer_tour()

    def changer_tour(self):
        if self.joueur_actuel == self.joueur1:
            self.joueur_actuel = self.joueur2
        else:
            self.joueur_actuel = self.joueur1
        self.phase_actuelle_index = 0 # Reset phase to Pioche for the new player
        self.joueur_actuel.piocher()

    def verifier_victoire(self):
        if self.joueur1.points_de_vie <= 0:
            return self.joueur2
        elif self.joueur2.points_de_vie <= 0:
            return self.joueur1
        return None

    def jouer_carte_magie(self, carte_magie, joueur_actif, joueur_adverse, carte_cible=None):
        print(f"{joueur_actif.nom} active l'effet de {carte_magie.nom}!")
        self.activer_effet_magie(carte_magie, joueur_actif, joueur_adverse, carte_cible)
        joueur_actif.main.remove(carte_magie)
        joueur_actif.cimetiere.append(carte_magie)

    def activer_effet_magie(self, carte_magie, joueur_actif, joueur_adverse, carte_cible=None):
        if carte_magie.type_effet == "degats":
            if carte_cible:
                carte_cible.points_defense -= carte_magie.valeur
                print(f"{carte_cible.nom} perd {carte_magie.valeur} points de défense.")
            else:
                joueur_adverse.points_de_vie -= carte_magie.valeur
                print(f"{joueur_adverse.nom} perd {carte_magie.valeur} points de vie.")
        elif carte_magie.type_effet == "soin":
            joueur_actif.points_de_vie += carte_magie.valeur
            print(f"{joueur_actif.nom} gagne {carte_magie.valeur} points de vie.")
        elif carte_magie.type_effet == "pioche":
            for _ in range(carte_magie.valeur):
                joueur_actif.piocher()
            print(f"{joueur_actif.nom} pioche {carte_magie.valeur} cartes.")
        elif carte_magie.type_effet == "vole":
            print(f"{joueur_actif.nom} tente de voler {carte_magie.valeur} carte(s) du deck de {joueur_adverse.nom}.")
            for i in range(carte_magie.valeur):
                if joueur_adverse.deck:
                    carte_volee = joueur_adverse.deck.pop(0)
                    joueur_actif.main.append(carte_volee)
                    print(f"  -> Carte volée !")
                else:
                    print("Le deck de l'adversaire est vide.")
                    break
        elif carte_magie.type_effet == "finish":
            if carte_cible and carte_cible.points_defense <= carte_magie.valeur:
                self.plateau.retirer_carte(carte_cible)
                print(f"{carte_cible.nom} a été détruit !")
            else:
                print(f"L'effet finish a échoué sur {carte_cible.nom}.")
        elif carte_magie.type_effet == "renforcement":
            if carte_cible:
                carte_cible.renforcee = True
                print(f"{carte_cible.nom} est maintenant renforcé.")
        elif carte_magie.type_effet == "régénération":
            if carte_cible:
                carte_cible.points_defense += carte_magie.valeur
                print(f"{carte_cible.nom} a récupéré {carte_magie.valeur} points de défense.")
        elif carte_magie.type_effet == "buff":
            if carte_cible:
                carte_cible.points_attaque += carte_magie.valeur
                print(f"{carte_cible.nom} a gagné {carte_magie.valeur} points d'attaque.")
