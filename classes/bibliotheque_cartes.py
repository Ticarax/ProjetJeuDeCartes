# classes/bibliotheque_cartes.py

# 1. Importez les classes de cartes dont vous avez besoin
from .class_carte_monstre import CarteMonstre
from .class_carte_magie import CarteMagie

# 2. Créez vos cartes en suivant le format de chaque classe

# --- Monstres ---
# CarteMonstre(nom, description, points_attaque, points_defense, niveau)
monstre_geant = CarteMonstre("Soldat du Lustre Noir", "Un guerrier redoutable.", 3000, 2500, 8)
magicien_temps = CarteMonstre("Magicien du Temps", "Un magicien qui peut vieillir.", 500, 400, 2)

# --- Magies ---
# CarteMagie(nom, description, type_effet, valeur)
# type_effet peut être "degats", "soin", "pioche", etc.
# valeur est le montant des dégats/soins/cartes à piocher.

soins_lumiere = CarteMagie("Pluie de Guérison", "Soigne le joueur actif.", "soin", 500)
marteau_puissant = CarteMagie("Marteau de Thor", "Inflige des dégâts à l'adversaire.", "degats", 700)
bibliothecaire = CarteMagie("Connaissance Ancienne", "Fait piocher des cartes.", "pioche", 2)


# 3. Regroupez toutes les cartes dans une liste principale
BIBLIOTHEQUE_COMPLETE = [
    # Monstres
    monstre_geant,
    magicien_temps,
    
    # Magies
    soins_lumiere,
    marteau_puissant,
    bibliothecaire,
]
