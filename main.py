from classes.class_joueur import Joueur
from classes.class_partie import Partie
from classes.class_carte_monstre import CarteMonstre

def afficher_etat_jeu(partie):
    joueur = partie.joueur_actuel
    print("\n" + "="*20)
    print(f"Tour de {joueur.nom}")
    print(f"Phase : {partie.phases[partie.phase_actuelle_index]}")
    print(f"Points de vie : {joueur.points_de_vie}")
    print("\nMain du joueur:")
    for i, carte in enumerate(joueur.main):
        print(f"  {i+1}: {carte.nom} (ATK: {carte.points_attaque} / DEF: {carte.points_defense})")
    
    print("\nPlateau:")
    print("  Monstres Joueur 1:", [c.nom if c else 'Vide' for c in partie.plateau.zones_monstre_j1])
    print("  Monstres Joueur 2:", [c.nom if c else 'Vide' for c in partie.plateau.zones_monstre_j2])
    print("="*20 + "\n")

# --- Initialisation du jeu ---
# Création des joueurs
joueur1 = Joueur("Yugi")
joueur2 = Joueur("Kaiba")

# Création des cartes
monstre1 = CarteMonstre("Magicien Sombre", "Le magicien ultime en termes d\'attaque et de défense.", 2500, 2100, 7)
monstre2 = CarteMonstre("Dragon Blanc aux Yeux Bleus", "Un dragon légendaire qui pulvérise ses ennemis.", 3000, 2500, 8)

# Remplissage des decks
joueur1.deck = [monstre1] * 5
joueur2.deck = [monstre2] * 5

# Création de la partie
partie = Partie(joueur1, joueur2)

# Démarrage de la partie (pioche initiale)
print("La partie commence !")
partie.demarrer_partie()

# --- Boucle de jeu principale ---
while True:
    afficher_etat_jeu(partie)
    joueur_actuel = partie.joueur_actuel

    # Vérification de victoire
    gagnant = partie.verifier_victoire()
    if gagnant:
        print(f"Victoire ! {gagnant.nom} a gagné la partie !")
        break

    action = input("Que voulez-vous faire ? (invoquer / fin) > ").lower()

    if action == "invoquer":
        if partie.phases[partie.phase_actuelle_index] == "Principale":
            try:
                choix_carte = int(input("Quelle carte de votre main voulez-vous invoquer ? (numéro) > ")) - 1
                choix_pos = int(input("Sur quel emplacement ? (0-4) > "))

                if 0 <= choix_carte < len(joueur_actuel.main) and 0 <= choix_pos < 5:
                    carte_a_invoquer = joueur_actuel.main[choix_carte]
                    
                    # Logique d'invocation
                    joueur_id = 1 if joueur_actuel == joueur1 else 2
                    partie.plateau.placer_carte(joueur_id, carte_a_invoquer, "monstre", choix_pos)
                    joueur_actuel.main.pop(choix_carte)
                    
                    print(f"{joueur_actuel.nom} a invoqué {carte_a_invoquer.nom}!")
                else:
                    print("Choix invalide.")
            except (ValueError, IndexError):
                print("Entrée invalide. Veuillez réessayer.")
        else:
            print("Vous ne pouvez invoquer que pendant votre phase Principale.")

    elif action == "fin":
        partie.prochaine_phase()
        if partie.phases[partie.phase_actuelle_index] == "Pioche": # Si on a fait un tour complet
            print(f"Fin du tour de {joueur_actuel.nom}.")
    else:
        print("Action non reconnue.")