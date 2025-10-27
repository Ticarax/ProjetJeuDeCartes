# classes/bibliotheque_cartes.py

from .class_carte_monstre import CarteMonstre
from .class_carte_magie import CarteMagie


# --- Monstres ---
# CarteMonstre(nom, description, points_attaque, points_defense, niveau)
monstre_geant = CarteMonstre("Soldat du Lustre Noir", "Un guerrier redoutable.", 3000, 2500, 7)
magicien_temps = CarteMonstre("Magicien du Temps", "Un magicien qui peut vieillir.", 500, 400, 2)
guerrier_puissant = CarteMonstre("garen", "Un puissant guerrier de Démacia.", 3400, 2000, 6)
saiyan = CarteMonstre("Goku", "Orphelin abandonner.", 4000, 2400, 8)
saiyan2 = CarteMonstre("Vegeta", "prince saiyen.", 4000, 2400, 8)
ver_sable = CarteMonstre("Le ver du désert", "un ver ancien coincer dans un désert abandonner.", 1000, 500, 3)
ver_glace = CarteMonstre("Le ver des glaces", "un ver ancien coincer dans les glacier.", 1000, 500, 3)
ver_feu = CarteMonstre("Le ver de feu", "un ver ancien coincer dans un volcan.", 1000, 500, 3)
troupe_élite1 = CarteMonstre("Gustavo", "Simple soldat admis sur recommandation.", 300, 400, 1)
troupe_élite2 = CarteMonstre("Gustava", "Simple soldat admis sur recommandation.", 300, 400, 1)
troupe_élite3 = CarteMonstre("Gustavi", "Simple soldat admis sur recommandation.", 300, 400, 1)
troupe_élite4 = CarteMonstre("Gustavu", "Simple soldat admis sur recommandation.", 300, 400, 1)
troupe_élite5 = CarteMonstre("Gustavou", "Simple soldat admis sur recommandation.", 300, 400, 1)
troupe_élite6 = CarteMonstre("Gustavon", "Simple soldat admis sur recommandation.", 300, 400, 1)
chef_troupe = CarteMonstre("Gustavito", "chef de la troupe d'élite des gustaves.", 500,1100, 3)
tiktokeur_née = CarteMonstre("Grandingo", "createur de ref de génie.", 600, 500, 3)
tiktokeur_vue = CarteMonstre("Nicolux", "createur de ref de génie.", 400, 700, 3)
youtubeur = CarteMonstre("Polo", "createur de ref de génie.", 700, 400, 3)
animatronique = CarteMonstre("Frédy", "Marionnette folle.", 400, 800, 2)
clown = CarteMonstre("Gripsou", "araigner de l'espace.", 1500, 2000, 5)
pourfendeur = CarteMonstre("dragon Slayeur", "Noble chevalier qui apporta la tete du dragon de feu.", 1800, 1100, 4)
gobelin1 = CarteMonstre("gobelino", "gobelin classic.", 200, 300, 1)
gobelin2 = CarteMonstre("gobelina", "gobelin classic.", 200, 400, 1)
gobelin3 = CarteMonstre("gobelini", "gobelin classic.", 200, 400, 1)
gobelin4 = CarteMonstre("gobelinous", "gobelin classic.", 200, 400, 1)
gobelin5 = CarteMonstre("gobelineu", "gobelin classic.", 200, 400, 1)
gobelin6 = CarteMonstre("gobelinus", "gobelin classic.", 200, 400, 1)
gobelin7 = CarteMonstre("gobelinor", "gobelin classic.", 200, 400, 1)
gobelin8 = CarteMonstre("gobelinar", "gobelin classic.", 200, 400, 1)
gobeling_gang = CarteMonstre("gobline gang", "gobelin classic.", 800, 1400, 5)

# --- Magies ---
# CarteMagie(nom, description, type_effet, valeur)
# type_effet peut être "degats", "soin", "pioche", "vole", "finish", "renforcement", "régénération", "buff" etc.
# valeur est le montant des dégats/soins/cartes à piocher.

soins_lumiere = CarteMagie("Pluie de Guérison", "Soigne le joueur actif.", "soin", 500)
marteau_puissant = CarteMagie("Marteau de Thor", "Inflige des dégâts à la carte adverse.", "degats", 700)
bibliothecaire = CarteMagie("Connaissance Ancienne", "Fait piocher des cartes.", "pioche", 2)
bibliothecaire2 = CarteMagie("Connaissance Ancienne", "Fait piocher des cartes.", "pioche", 2)
voleur = CarteMagie("chipeur", "Vole une carte de la pioche.", "vole", 2)
voleur2 = CarteMagie("chipeur", "Vole une carte de la pioche.", "vole", 2)
fire_ball = CarteMagie("Boule de feu", "Inflige des dégâts à la carte adverse.", "degats", 600)
fire_ball2 = CarteMagie("Boule de feu", "Inflige des dégâts à la carte adverse.", "degats", 600)
divine_light = CarteMagie("Lumiere divine", "Soigne le joueur actif.", "soin", 1000)
divine_light2 = CarteMagie("Lumiere divine", "Soigne le joueur actif.", "soin", 1000)
Dark_blast = CarteMagie("Rayon noir", "Inflige des dégâts à la carte adverse.", "degats", 1000)
Smite = CarteMagie("Smite", "Finie la carte adverse si il lui reste peu de pv.", "finish", 400)
Smite2 = CarteMagie("Smite", "Finie la carte adverse si il lui reste peu de pv.", "finish", 400)
friendship = CarteMagie("friendship power", "augmente l'attaque d'une carte'.", "buff", 400)
fiole = CarteMagie("fiole sacré", "soigne une carte.", "régénération", 500)
fiole2 = CarteMagie("fiole sacré", "soigne une carte.", "régénération", 500)
#Sepukku = CarteMagie("sepuku", "augmente l'attaque d'une carte'.""baisse la vie de la carte.", "buff", 400)
fiole_special = CarteMagie("fiole miraculeuse", "par une attaque.", "renforcement", 1)
fiole_special2 = CarteMagie("fiole miraculeuse", "par une attaque.", "renforcement", 1)

# 3. Regroupez toutes les cartes dans une liste principale
BIBLIOTHEQUE_COMPLETE = [
    # Monstres
    monstre_geant,
    magicien_temps,
    guerrier_puissant,
    saiyan,
    saiyan2,
    ver_sable,
    ver_feu,
    ver_glace,
    troupe_élite1,
    troupe_élite2,
    troupe_élite3,
    troupe_élite4,
    troupe_élite5,
    troupe_élite6,
    chef_troupe,
    tiktokeur_née,
    tiktokeur_vue,
    youtubeur,
    animatronique,
    clown,
    pourfendeur,
    gobelin1,
    gobelin2,
    gobelin3,
    gobelin4,
    gobelin5,
    gobelin6,
    gobelin7,
    gobelin8,
    gobeling_gang,



    
    # Magies
    soins_lumiere,
    marteau_puissant,
    bibliothecaire,
    bibliothecaire2,
    voleur,
    voleur2,
    fire_ball,
    fire_ball2,
    divine_light,
    divine_light2,
    Dark_blast,
    Smite,
    Smite2,
    friendship,
    fiole,
    fiole2,
    Sepuku,
    fiole_special,
    fiole_special2,

]
