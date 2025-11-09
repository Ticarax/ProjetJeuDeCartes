# Ref_Battle
Phase 1 : L'analyse des besoins
Mise en place d'un « cahier des charges »

Le sujet du projet : Quelle situation cherchez-vous à modéliser ? Quel est le but ? L'objectif final du projet ?

Situation à modéliser : Le projet vise à modéliser un duel de cartes entre deux joueurs humains. Chaque joueur possède un deck de cartes composé de monstres et de magies/pièges. Le jeu se déroule sur un plateau virtuel où les joueurs peuvent invoquer des monstres, les faire combattre, et utiliser des cartes aux effets variés pour réduire les points de vie de l'adversaire à zéro.

But : Le but est de concevoir un moteur de jeu robuste et modulaire en utilisant les principes de la programmation orientée objet. L'architecture doit être pensée pour séparer la logique du jeu de son affichage, afin de permettre le développement futur d'une interface graphique (GUI) sans avoir à réécrire le cœur du programme.

Objectif final : Développer une application en ligne de commande fonctionnelle permettant à deux joueurs de s'affronter. L'application doit gérer les tours, les phases de jeu (pioche, combat, fin de tour), les invocations de monstres, les combats et les conditions de victoire.

Modélisation prévisionnelle du projet : Identifier quels vont être les objets, ainsi que leurs attributs et leurs méthodes.

1. Les Objets (Classes)

Carte (Classe de base/abstraite) : Le modèle de base pour toutes les cartes.

CarteMonstre (hérite de Carte) : Une créature avec des statistiques de combat.

CarteMagie (hérite de Carte) : Une carte avec un effet immédiat.

CartePiege (hérite de Carte) : Une carte posée face cachée, qui s'active sous certaines conditions.

Joueur : Représente l'un des deux participants au duel.

Plateau : L'espace de jeu central, contenant les zones pour les cartes de chaque joueur.

Partie : L'objet principal qui orchestre tout le jeu, les tours et les phases.

2. Attributs et Méthodes par Objet

Classe Carte

Attributs : nom (string), description (string).

Méthodes : jouer(proprietaire) : Méthode abstraite définissant l'action de base de la carte.

Classe CarteMonstre (hérite de Carte)

Attributs : points_attaque (int), points_defense (int), niveau (int), position (string: "Attaque" ou "Défense").

Méthodes : attaquer(monstre_cible), changer_position().

Classe CarteMagie (hérite de Carte)

Attributs : type_effet (string).

Méthodes : activer_effet(partie, cible).

Classe Joueur

Attributs : nom (string), points_de_vie (int), deck (liste d'objets Carte), main (liste), cimetiere (liste).

Méthodes : piocher(), invoquer_monstre(...), poser_carte(...), declarer_attaque(...).

Classe Plateau

Attributs :

zones_monstre_j1 (liste de 5 slots, pouvant contenir CarteMonstre ou None).

zones_magie_piege_j1 (liste de 5 slots).

zones_monstre_j2 (liste de 5 slots).

zones_magie_piege_j2 (liste de 5 slots).

Méthodes : placer_carte(joueur, carte, zone), retirer_carte(carte), get_monstres_visibles(joueur_adverse).

Classe Partie

Attributs : joueur1 (objet Joueur), joueur2 (objet Joueur), plateau (objet Plateau), joueur_actuel (objet Joueur), phase_actuelle (string: "Pioche", "Principale", "Combat", "Fin").

Méthodes : demarrer_partie(), prochaine_phase(), changer_tour(), verifier_victoire().

3. Cas d'utilisation (Use Case)

Titre : Un joueur attaque un monstre adverse.

Acteur principal : Joueur Actuel.

Préconditions : La partie est en phase de "Combat". Le joueur actuel a au moins un monstre en position d'attaque sur son plateau. Le joueur adverse a au moins un monstre sur son plateau.

Règle additionnelle : Un joueur ne peut pas attaquer durant son tout premier tour de jeu. Les attaques sont possibles à partir du deuxième tour de chaque joueur (soit à partir du 3ème tour de la partie).

Scénario de succès :

Le joueur actuel sélectionne l'un de ses monstres en position d'attaque (monstre_attaquant).

Le joueur actuel sélectionne un monstre adverse comme cible (monstre_defenseur).

Le système appelle la méthode attaquer() de monstre_attaquant avec monstre_defenseur en paramètre.

La méthode compare les points d'attaque/défense selon la position du monstre_defenseur.

Les points de vie du ou des joueurs sont mis à jour en fonction du résultat du combat.

Le monstre vaincu est retiré du Plateau et placé dans le cimetiere de son propriétaire.

Le système demande au joueur s'il souhaite attaquer avec un autre monstre.

Tout ce qui vous semble utile pour la compréhension de votre projet ;

Architecture pour une future interface graphique (Modèle-Vue-Contrôleur) :
Pour garantir que l'on puisse ajouter une interface graphique plus tard, le projet sera structuré en deux parties distinctes :

Le Modèle (le moteur de jeu) : Toutes les classes décrites ci-dessus (Carte, Joueur, Plateau, Partie). Règle d'or : ces classes ne doivent contenir AUCUN print() ou input(). Elles gèrent uniquement les données et la logique du jeu. Elles ne savent pas et ne doivent pas savoir comment le jeu est affiché.

La Vue/Contrôleur (l'interface en ligne de commande) : Un fichier principal (ex: main.py) sera responsable de l'affichage. Il créera les objets du Modèle (une Partie), puis entrera dans une boucle qui :

Affiche l'état actuel du jeu en lisant les informations des objets (plateau.zones_monstre_j1, joueur1.main, etc.).

Demande au joueur ce qu'il veut faire (input()).

Traduit cette demande en un appel de méthode sur les objets du Modèle (ex: partie.joueur_actuel.invoquer_monstre(...)).

Cette séparation est cruciale : pour passer à une interface graphique, il suffira de remplacer la partie "Vue/Contrôleur" en ligne de commande par une nouvelle interface graphique (avec Pygame ou Tkinter), sans toucher à une seule ligne de code du moteur de jeu.
