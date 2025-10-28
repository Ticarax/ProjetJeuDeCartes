from classes.class_joueur import Joueur
from classes.class_partie import Partie
from classes.class_carte_monstre import CarteMonstre
from classes.class_carte_magie import CarteMagie
from classes.bibliotheque_cartes import BIBLIOTHEQUE_COMPLETE
import random

def afficher_etat_jeu(partie):
    joueur = partie.joueur_actuel
    adversaire = partie.joueur2 if partie.joueur_actuel == partie.joueur1 else partie.joueur1
    print("\n" + "="*30)
    print(f"Tour de {joueur.nom} | Phase : {partie.phases[partie.phase_actuelle_index]} | PV: {joueur.points_de_vie}")
    print(f"Adversaire : {adversaire.nom} | PV: {adversaire.points_de_vie}")
    print("="*30)
    
    print("\n--- Votre Main ---")
    for i, carte in enumerate(joueur.main):
        if isinstance(carte, CarteMonstre):
            print(f"  {i+1}: {carte.nom} (Monstre - ATK: {carte.points_attaque} / DEF: {carte.points_defense})")
        elif isinstance(carte, CarteMagie):
            print(f"  {i+1}: {carte.nom} (Magie - Effet: {carte.type_effet}, Valeur: {carte.valeur})")
    
    print("\n--- Plateau de {joueur.nom} ---")
    print("  Monstres:", [c.nom if c else 'Vide' for c in (partie.plateau.zones_monstre_j1 if joueur == partie.joueur1 else partie.plateau.zones_monstre_j2)])
    print("  Magie/Piège:", [c.nom if c else 'Vide' for c in (partie.plateau.zones_magie_piege_j1 if joueur == partie.joueur1 else partie.plateau.zones_magie_piege_j2)])

    print("\n--- Plateau de {adversaire.nom} ---")
    print("  Monstres:", [c.nom if c else 'Vide' for c in (partie.plateau.zones_monstre_j2 if joueur == partie.joueur1 else partie.plateau.zones_monstre_j1)])
    print("  Magie/Piège:", [c.nom if c else 'Vide' for c in (partie.plateau.zones_magie_piege_j2 if joueur == partie.joueur1 else partie.plateau.zones_magie_piege_j1)])
    print("="*30 + "\n")

# --- Initialisation du jeu ---
# Création des joueurs
joueur1 = Joueur("Remi")
joueur2 = Joueur("Tim")

# Préparation du paquet de cartes
# Filtrer les monstres et les magies
monstres = [carte for carte in BIBLIOTHEQUE_COMPLETE if isinstance(carte, CarteMonstre)]
magies = [carte for carte in BIBLIOTHEQUE_COMPLETE if isinstance(carte, CarteMagie)]

# Mélanger les listes
random.shuffle(monstres)
random.shuffle(magies)

# Sélectionner 20 monstres et 10 magies (si possible)
deck_monstres = monstres[:20]
deck_magies = magies[:10]

# Créer le paquet de jeu final
paquet_de_jeu = deck_monstres + deck_magies
random.shuffle(paquet_de_jeu)

# S'assurer qu'on a assez de cartes, sinon le jeu ne peut pas commencer
if len(paquet_de_jeu) < 30:
    print(f"Attention: Le paquet ne contient que {len(paquet_de_jeu)} cartes. Le jeu risque de ne pas fonctionner comme prévu.")
    # On pourrait vouloir arrêter le jeu ici ou gérer le cas
    # Pour l'instant, on distribue ce qu'on a
    moitie = len(paquet_de_jeu) // 2
    joueur1.deck = paquet_de_jeu[:moitie]
    joueur2.deck = paquet_de_jeu[moitie:]
else:
    # Distribution des decks (15 cartes par joueur)
    joueur1.deck = paquet_de_jeu[:15]
    joueur2.deck = paquet_de_jeu[15:30]

# Création de la partie
partie = Partie(joueur1, joueur2)

# Démarrage de la partie (pioche initiale)
print("La partie commence !")
partie.demarrer_partie()

# --- Boucle de jeu principale ---
while True:
    joueur_actuel = partie.joueur_actuel
    adversaire = partie.joueur2 if joueur_actuel == joueur1 else joueur1
    afficher_etat_jeu(partie)

    # Vérification de victoire
    gagnant = partie.verifier_victoire()
    if gagnant:
        print(f"Victoire ! {gagnant.nom} a gagné la partie !")
        break

    action = input("Que voulez-vous faire ? (invoquer / poser / attaquer / activer / fin) > ").lower()

    if action == "invoquer":
        if partie.phases[partie.phase_actuelle_index] == "Principale":
            try:
                choix_carte = int(input("Quelle carte de votre main voulez-vous invoquer ? (numéro) > ")) - 1
                choix_pos = int(input("Sur quel emplacement ? (0-4) > "))

                if 0 <= choix_carte < len(joueur_actuel.main) and isinstance(joueur_actuel.main[choix_carte], CarteMonstre) and 0 <= choix_pos < 5:
                    carte_a_invoquer = joueur_actuel.main[choix_carte]
                    
                    joueur_id = 1 if joueur_actuel == joueur1 else 2
                    partie.plateau.placer_carte(joueur_id, carte_a_invoquer, "monstre", choix_pos)
                    joueur_actuel.main.pop(choix_carte)
                    
                    print(f"{joueur_actuel.nom} a invoqué {carte_a_invoquer.nom}!")
                else:
                    print("Choix invalide. Assurez-vous de choisir un monstre.")
            except (ValueError, IndexError):
                print("Entrée invalide. Veuillez réessayer.")
        else:
            print("Vous ne pouvez invoquer que pendant votre phase Principale.")

    elif action == "poser":
        if partie.phases[partie.phase_actuelle_index] == "Principale":
            try:
                choix_carte = int(input("Quelle carte de votre main voulez-vous poser ? (numéro) > ")) - 1
                choix_pos = int(input("Sur quel emplacement ? (0-4) > "))

                if 0 <= choix_carte < len(joueur_actuel.main) and isinstance(joueur_actuel.main[choix_carte], CarteMagie) and 0 <= choix_pos < 5:
                    carte_a_poser = joueur_actuel.main[choix_carte]
                    
                    joueur_id = 1 if joueur_actuel == joueur1 else 2
                    partie.plateau.placer_carte(joueur_id, carte_a_poser, "magie_piege", choix_pos)
                    joueur_actuel.main.pop(choix_carte)
                    
                    print(f"{joueur_actuel.nom} a posé {carte_a_poser.nom} face cachée.")
                else:
                    print("Choix invalide. Assurez-vous de choisir une carte Magie.")
            except (ValueError, IndexError):
                print("Entrée invalide. Veuillez réessayer.")
        else:
            print("Vous ne pouvez poser une carte que pendant votre phase Principale.")

    elif action == "activer":
        if partie.phases[partie.phase_actuelle_index] == "Principale":
            try:
                choix_carte = int(input("Quelle carte de votre main voulez-vous activer ? (numéro) > ")) - 1

                if 0 <= choix_carte < len(joueur_actuel.main) and isinstance(joueur_actuel.main[choix_carte], CarteMagie):
                    carte_a_activer = joueur_actuel.main[choix_carte]
                    carte_cible = None

                    # Gérer le ciblage
                    effets_ciblage = ["degats", "finish", "renforcement", "régénération", "buff"]
                    if carte_a_activer.type_effet in effets_ciblage:
                        if carte_a_activer.type_effet in ["degats", "finish"]:
                            print("Quel monstre adverse voulez-vous cibler ?")
                            zones_cibles = partie.plateau.zones_monstre_j2 if joueur_actuel == joueur1 else partie.plateau.zones_monstre_j1
                        else: # renforcement, régénération, buff
                            print("Quel de vos monstres voulez-vous cibler ?")
                            zones_cibles = partie.plateau.zones_monstre_j1 if joueur_actuel == joueur1 else partie.plateau.zones_monstre_j2
                        
                        for i, monstre in enumerate(zones_cibles):
                            if monstre:
                                print(f"  {i}: {monstre.nom}")
                        
                        try:
                            choix_cible = int(input("Numéro du monstre > "))
                            if 0 <= choix_cible < len(zones_cibles) and zones_cibles[choix_cible]:
                                carte_cible = zones_cibles[choix_cible]
                            else:
                                print("Cible invalide.")
                                continue # Recommence la boucle d'action
                        except ValueError:
                            print("Entrée invalide.")
                            continue

                    partie.jouer_carte_magie(carte_a_activer, joueur_actuel, adversaire, carte_cible)

                else:
                    print("Choix invalide. Assurez-vous de choisir une carte Magie.")
            except (ValueError, IndexError):
                print("Entrée invalide. Veuillez réessayer.")
        else:
            print("Vous ne pouvez activer une carte que pendant votre phase Principale.")

    elif action == "attaquer":
        if partie.phases[partie.phase_actuelle_index] == "Combat":
            try:
                # Choix de l'attaquant
                zones_joueur = partie.plateau.zones_monstre_j1 if joueur_actuel == joueur1 else partie.plateau.zones_monstre_j2
                choix_att = int(input("Avec quel monstre attaquer ? (emplacement 0-4) > "))
                attaquant = zones_joueur[choix_att]

                # Choix de la cible
                zones_adv = partie.plateau.zones_monstre_j2 if joueur_actuel == joueur1 else partie.plateau.zones_monstre_j1
                choix_def = int(input("Quel monstre adverse attaquer ? (emplacement 0-4) > "))
                defenseur = zones_adv[choix_def]

                if attaquant and defenseur:
                    resultat = joueur_actuel.declarer_attaque(attaquant, defenseur, adversaire)
                    print(f"Combat ! {attaquant.nom} attaque {defenseur.nom}.")

                    if resultat["dommages"] > 0:
                        print(f"Des dommages sont infligés ! Montant : {resultat["dommages"]}")
                    if resultat["attaquant_detruit"]:
                        print(f"{attaquant.nom} est détruit.")
                        zones_joueur[choix_att] = None
                        joueur_actuel.cimetiere.append(attaquant)
                    if resultat["defenseur_detruit"]:
                        print(f"{defenseur.nom} est détruit.")
                        zones_adv[choix_def] = None
                        adversaire.cimetiere.append(defenseur)
                else:
                    print("Emplacement de monstre invalide.")

            except (ValueError, IndexError):
                print("Entrée invalide. Veuillez réessayer.")
        else:
            print("Vous ne pouvez attaquer que pendant votre phase de Combat.")

    elif action == "fin":
        partie.prochaine_phase()
        if partie.phases[partie.phase_actuelle_index] == "Pioche": # Si on a fait un tour complet
            print(f"Fin du tour de {joueur_actuel.nom}.")
    else:
        print("Action non reconnue.")