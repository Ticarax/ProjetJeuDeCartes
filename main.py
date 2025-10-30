from classes.class_joueur import Joueur
from classes.class_partie import Partie
from classes.class_carte_monstre import CarteMonstre
from classes.class_carte_magie import CarteMagie
from classes.bibliotheque_cartes import BIBLIOTHEQUE_COMPLETE
import random

def demander_action(partie):
    phase_actuelle = partie.phases[partie.phase_actuelle_index]
    print(f"--- Phase {phase_actuelle} ---")
    #f = sa facilite l'affichage quand il y a bcp de texte
    actions_possibles = {}
    joueur_actuel = partie.joueur_actuel
    
    if phase_actuelle == "Principale":
        # On vérifie si le joueur peut invoquer un monstre en main et de la place sur son plateau
        peut_invoquer = any(isinstance(c, CarteMonstre) for c in joueur_actuel.main) and any(z is None for z in (partie.plateau.zones_monstre_j1 if partie.joueur_actuel == partie.joueur1 else partie.plateau.zones_monstre_j2))
        # fait par IA car complique a trouver
        peut_activer = any(isinstance(c, CarteMagie) for c in joueur_actuel.main)
        #any = regarde tout les element et renvoie trus si un seul est true, false si  tout est faux / va simplifer et eviter de rajouter plei nde and/or ect...
        #isinstance = permet de vérifier le type d'objet d'une variable     

        menu = {}
        if peut_invoquer:
            menu[str(len(menu)+1)] = ("Invoquer un monstre", "invoquer")
        if peut_activer:
            menu[str(len(menu)+1)] = ("Activer une carte magie", "activer")
        
        menu[str(len(menu)+1)] = ("Passer à la phase de combat", "phase_combat")
        menu[str(len(menu)+1)] = ("Finir le tour", "fin_tour")
        actions_possibles = menu
        #affiche dans une biblio appeler menu le menu / les 2 action avec if sont pour les afficher uniquement si c'est possible de le faire 

    elif phase_actuelle == "Combat":
        # On vérifie si le joueur a un monstre qui peut encore attaquer
        zones_joueur = partie.plateau.zones_monstre_j1 if partie.joueur_actuel == partie.joueur1 else partie.plateau.zones_monstre_j2
        peut_attaquer = any(monstre is not None and not monstre.a_attaque_ce_tour for monstre in zones_joueur)

        menu = {}
        if peut_attaquer:
            menu[str(len(menu)+1)] = ("Déclarer une attaque", "attaquer")
        
        menu[str(len(menu)+1)] = ("Finir le tour", "fin_tour")
        actions_possibles = menu

    if not actions_possibles:
        return "auto"

    print("Actions possibles :")
    for key, (description, _) in actions_possibles.items():
        print(f"  {key}: {description}")
        
    choix = input("> ")
    action_tuple = next((v for k, v in actions_possibles.items() if k == choix), None)

    if action_tuple:
        return action_tuple[1]
    else:
        print("Action non valide.")
        return None
    #sa permet de veifier si le nombre que l'on rentre correspond a une action disponible

def afficher_etat_jeu(partie):
    joueur = partie.joueur_actuel
    adversaire = partie.joueur2 if partie.joueur_actuel == partie.joueur1 else partie.joueur1
    print("\n" + "="*30)
    print(f"Tour de {joueur.nom} | Phase : {partie.phases[partie.phase_actuelle_index]} | PV: {joueur.points_de_vie}")
    print(f"Adversaire : {adversaire.nom} | PV: {adversaire.points_de_vie}")
    print("="*30)
    
    print("\n--- Votre Main ---")
    for i, carte in enumerate(joueur.main):#enumerate = pour le nombre de carte que le joueur a dans sa main
        if isinstance(carte, CarteMonstre):
            print(f"  {i+1}: {carte.nom} (Monstre - ATK: {carte.points_attaque} / DEF: {carte.points_defense})")
        elif isinstance(carte, CarteMagie):
            print(f"  {i+1}: {carte.nom} (Magie - Effet: {carte.type_effet}, Valeur: {carte.valeur})")

    #afficher le deck en main du joueur 
    
    print(f"\n--- Plateau de {joueur.nom} ---")
    print("  Monstres:", [c.nom if c else 'Vide' for c in (partie.plateau.zones_monstre_j1 if joueur == partie.joueur1 else partie.plateau.zones_monstre_j2)])
    #aider par ia pour afficher les nom des carte positioner sur le plateau en fonction du joueur qui joue 
    print(f"\n--- Plateau de {adversaire.nom} ---")
    print("  Monstres:", [c.nom if c else 'Vide' for c in (partie.plateau.zones_monstre_j2 if joueur == partie.joueur1 else partie.plateau.zones_monstre_j1)])
    print("="*30 + "\n")

# --- Initialisation du jeu ---
# création des joueurs
joueur1 = Joueur("Remi")
joueur2 = Joueur("Tim")

# preparation du paquet de cartes
# filtrer les monstres et les magies
monstres = [carte for carte in BIBLIOTHEQUE_COMPLETE if isinstance(carte, CarteMonstre)]
magies = [carte for carte in BIBLIOTHEQUE_COMPLETE if isinstance(carte, CarteMagie)]

# melanger les listes
random.shuffle(monstres)
random.shuffle(magies)

# selectionner 20 monstres et 10 magies 
deck_monstres = monstres[:20]
deck_magies = magies[:10]

# créer le paquet de jeu final
paquet_de_jeu = deck_monstres + deck_magies
random.shuffle(paquet_de_jeu)

# s'assurer qu'on a assez de cartes, sinon le jeu ne peut pas commencer / on la mit au debut pour eviter les beug et les testes mais on a decider de le laisser 
if len(paquet_de_jeu) < 30:
    print(f"Attention: Le paquet ne contient que {len(paquet_de_jeu)} cartes. Le jeu risque de ne pas fonctionner comme prévu.")
    # on pourrait vouloir arrêter le jeu ici ou gérer le cas
    # pour l'instant, on distribue ce qu'on a
    moitie = len(paquet_de_jeu) // 2
    joueur1.deck = paquet_de_jeu[:moitie]
    joueur2.deck = paquet_de_jeu[moitie:]
else:
    # Distribution des decks (15 cartes par joueur)
    joueur1.deck = paquet_de_jeu[:15]
    joueur2.deck = paquet_de_jeu[15:30]

# creation de la partie
partie = Partie(joueur1, joueur2)

# demarrage de la partie (pioche initiale)
print("La partie commence !")
partie.demarrer_partie()

# --- Boucle de jeu principale ---
while True:
    joueur_actuel = partie.joueur_actuel
    adversaire = partie.joueur2 if joueur_actuel == joueur1 else joueur1

    # gerer la phase de pioche automatiquement
    if partie.phases[partie.phase_actuelle_index] == "Pioche":
        print("-" * 30)
        print(f"Nouveau tour pour {joueur_actuel.nom} !")
        carte_piochee = joueur_actuel.piocher()
        if carte_piochee:
            print(f"{joueur_actuel.nom} pioche une carte.")
        else:
            print(f"{joueur_actuel.nom} ne peut plus piocher !")
        partie.prochaine_phase() # Passe à la phase Principale
        continue
        #passe a la suite / decouvert aleatoirement 

    afficher_etat_jeu(partie)

    # verification de victoire
    gagnant = partie.verifier_victoire()
    if gagnant:
        print(f"Victoire ! {gagnant.nom} a gagné la partie !")
        break
        #va casser la boucle des lors qu'il y a un gagnant

    action = demander_action(partie)

    if action is None:
        continue # action invalide, on redemande

    if action == "auto":
        print("Aucune action possible, passage à la phase suivante.")
        # si on est en phase de combat, on finit le tour
        if partie.phases[partie.phase_actuelle_index] == "Combat":
            partie.changer_tour()
        # sinon on passe à la phase de combat
        else:
            partie.prochaine_phase()
        continue

    # --- Gérer les changements de phase ---
    if action == "phase_combat":
        partie.prochaine_phase()
        continue
    
    if action == "fin_tour":
        print(f"Fin du tour de {joueur_actuel.nom}.")
        partie.changer_tour() # change de joueur et met la phase à Pioche
        continue

    # --- Exécution des actions de jeu ---
    if action == "invoquer":
        try:     # try = verifie que les reponses des inputs sont valide sinon sa bascule sur le excepte en bas 
            print("--- Votre Main (Monstres) ---")
            for i, carte in enumerate(joueur_actuel.main):
                if isinstance(carte, CarteMonstre):
                    print(f"  {i+1}: {carte.nom} (ATK: {carte.points_attaque} / DEF: {carte.points_defense})")
            
            choix_carte = int(input("Quelle carte de votre main voulez-vous invoquer ? (numéro) > ")) - 1
            choix_pos = int(input("Sur quel emplacement ? (0-4) > "))
            #defini quel carte monstre et a quelle emplacement on la pose

            if 0 <= choix_carte < len(joueur_actuel.main) and isinstance(joueur_actuel.main[choix_carte], CarteMonstre) and 0 <= choix_pos < 5:
                joueur_id = 1 if joueur_actuel == joueur1 else 2
                zones_monstres_joueur = partie.plateau.zones_monstre_j1 if joueur_id == 1 else partie.plateau.zones_monstre_j2
                
                if zones_monstres_joueur[choix_pos] is None:    #verifie qu'il n'y a pas d'autre carte a cet emplacement
                    carte_a_invoquer = joueur_actuel.main.pop(choix_carte)
                    partie.plateau.placer_carte(joueur_id, carte_a_invoquer, "monstre", choix_pos)
                    print(f"{joueur_actuel.nom} a invoqué {carte_a_invoquer.nom}!")
                else:
                    print("Action impossible : cet emplacement est déjà occupé.")
            else:
                print("Choix invalide.")
        except (ValueError, IndexError):
            print("Entrée invalide. Veuillez réessayer.")

    elif action == "activer":
        try:
            print("--- Votre Main (Magie) ---")
            magie_en_main = {i: carte for i, carte in enumerate(joueur_actuel.main) if isinstance(carte, CarteMagie)}
            for i, carte in magie_en_main.items():
                print(f"  {i+1}: {carte.nom} (Effet: {carte.type_effet})")

            choix_carte_idx = int(input("Quelle carte de votre main voulez-vous activer ? (numéro) > ")) - 1

            if 0 <= choix_carte_idx < len(joueur_actuel.main) and isinstance(joueur_actuel.main[choix_carte_idx], CarteMagie):
                carte_a_activer = joueur_actuel.main[choix_carte_idx]
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
                        # on selectionne les monstres a visés  les siens/adverse 
                    for i, monstre in enumerate(zones_cibles):
                        if monstre:
                            print(f"  {i}: {monstre.nom}")
                    
                    try:
                        choix_cible = int(input("Numéro du monstre > "))
                        if 0 <= choix_cible < len(zones_cibles) and zones_cibles[choix_cible]:
                            carte_cible = zones_cibles[choix_cible]
                        else:
                            print("Cible invalide.")
                            continue
                    except (ValueError, IndexError):
                        print("Entrée invalide.")
                        continue
                
                # la carte est retirée de la main dans jouer_carte_magie
                partie.jouer_carte_magie(carte_a_activer, joueur_actuel, adversaire, carte_cible)

            else:
                print("Choix invalide.")
        except (ValueError, IndexError):
            print("Entrée invalide. Veuillez réessayer.")

    elif action == "attaquer":
        try:
            zones_joueur = partie.plateau.zones_monstre_j1 if joueur_actuel == joueur1 else partie.plateau.zones_monstre_j2
            print("Avec quel monstre voulez-vous attaquer ?")
            for i, monstre in enumerate(zones_joueur):
                if monstre:
                    print(f"  {i}: {monstre.nom}")
            choix_att = int(input("Avec quel monstre attaquer ? (emplacement 0-4) > "))
            
            if 0 <= choix_att < 5:
                attaquant = zones_joueur[choix_att]

                if attaquant:
                    if attaquant.a_attaque_ce_tour:
                        print("Ce monstre a déjà attaqué ce tour.")
                    else:
                        zones_adv = partie.plateau.zones_monstre_j2 if joueur_actuel == joueur1 else partie.plateau.zones_monstre_j1
                        if all(monstre is None for monstre in zones_adv): # all = pour signifier tout les monstres / dans ce cas la c'est pour indiquer qu'il n'y a pas de monstre sur les emplacements adverse
                            print(f"L'adversaire n'a pas de monstres. Vous attaquez directement ses points de vie !")
                            adversaire.points_de_vie -= attaquant.points_attaque
                            print(f"{attaquant.nom} inflige {attaquant.points_attaque} points de dégâts à {adversaire.nom}.")
                            attaquant.a_attaque_ce_tour = True
                        else:
                            print("Quel monstre adverse attaquer ?")
                            for i, monstre in enumerate(zones_adv):
                                if monstre:
                                    print(f"  {i}: {monstre.nom}")

                            choix_def = int(input("Cible ? (emplacement 0-4) > "))
                            if 0 <= choix_def < 5:
                                defenseur = zones_adv[choix_def]

                                if defenseur:
                                    resultat = joueur_actuel.declarer_attaque(attaquant, defenseur, adversaire)
                                    attaquant.a_attaque_ce_tour = True  # pour eviter qu'il ne puisse réattaquer
                                    print(f"Combat ! {attaquant.nom} attaque {defenseur.nom}.")

                                    if resultat.get("attaquant_detruit"):
                                        print(f"{attaquant.nom} est détruit.")
                                        zones_joueur[choix_att] = None
                                        joueur_actuel.cimetiere.append(attaquant)
                                    if resultat.get("defenseur_detruit"):
                                        print(f"{defenseur.nom} est détruit.")
                                        zones_adv[choix_def] = None
                                        adversaire.cimetiere.append(defenseur)
                                        #ajout de la cart au cimetiere en fonction de la carte détruite
                                    
                                    if resultat.get('dommages', 0) > 0:
                                        print(f"Le joueur perdant reçoit {resultat['dommages']} points de dégâts.")

                                else:
                                    print("Il n'y a pas de monstre à cet emplacement.")
                            else:
                                print("Emplacement de cible invalide.")
                else:
                    print("Vous n'avez pas de monstre à cet emplacement pour attaquer.")
            else:
                print("Emplacement d'attaquant invalide.")

        except (ValueError, IndexError):
            print("Entrée invalide. Veuillez réessayer.")