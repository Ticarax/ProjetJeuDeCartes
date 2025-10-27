from classes.class_joueur import Joueur
from classes.class_partie import Partie
from classes.class_carte_monstre import CarteMonstre

# Create players
joueur1 = Joueur("Joueur 1")
joueur2 = Joueur("Joueur 2")

# Create cards
monstre1 = CarteMonstre("Dragon Blanc aux Yeux Bleus", "Un dragon légendaire", 3000, 2500, 8)
monstre2 = CarteMonstre("Magicien Sombre", "Un magicien puissant", 2500, 2100, 7)

# Add cards to decks
joueur1.deck = [monstre1] * 10
joueur2.deck = [monstre2] * 10

# Create game
partie = Partie(joueur1, joueur2)

# Start game
partie.demarrer_partie()

# Game loop
while True:
    print(f"C'est au tour de {partie.joueur_actuel.nom}")
    print(f"Phase actuelle : {partie.phases[partie.phase_actuelle_index]}")

    partie.prochaine_phase()

    gagnant = partie.verifier_victoire()
    if gagnant:
        print(f"{gagnant.nom} a gagné la partie !")
        break

    input("Appuyez sur Entrée pour continuer...")
