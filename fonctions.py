"""Ce fichier contient les fonctions nécessaires à notre application i.e. notre programme pendu

S'appuie sur le fichier donnees.py"""

import os
import pickle

from random import choice
from donnees import liste_mots, nom_fichier_scores

# Fonctions gérant le score

def recup_scores():
    """Fonction chargée de :
    - récupérer l'objet dépické contenant les scores enregistrés si le fichier existe
    - renvoier un dictionnaire vide sinon 

    S'appuie sur nom_fichier_scores défini dans donnees.py"""
    
    if os.path.exists(nom_fichier_scores): # Le fichier existe
        # On le récupère
        fichier_scores = open(nom_fichier_scores, "rb")
        mon_depickler = pickle.Unpickler(fichier_scores)
        scores = mon_depickler.load()
        fichier_scores.close()
    else: # Le fichier n'existe pas
        scores = {}
    return scores

def enregistrer_scores(scores):
    """Fonction chargée d'enregistrer le score dans le fichier nom_fichier_score

    Paramètres : dictionnaire des scores à enregistrer"""  
    
    fichier_scores = open(nom_fichier_scores,"wb")
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(fichier_scores)
    fichier_scores.close()

 



# Fonctions gérant les éléments saisis par l'utilisateur

def recup_nom_utilisateur():
    """Fonction chargée de récupérer le nom de l'utilisateur pour enregistrer son score
    Le nom doit être composé de 4 caractères (chiffres et lettres exclusivement) minimum
    Si le nom n'est pas valide, on appelle récursivement la fonction pour en obtenir un nouveau"""

    nom_utilisateur = input("Tapez votre nom : ")
    # On met la première lettre en majuscule ET les autres en minuscules
    nom_utilisateur = nom_utilisateur.capitalize()
    if not nom_utilisateur.isalnum() or len(nom_utilisateur)<4:
        print("Ce nom est invalide.")
        # On appelle de nouveau la fonction pour avoir un autre nom
        return recup_nom_utilisateur()
    else:
        return nom_utilisateur

def recup_lettre():
    """Fonction chargée de récupérer une lettre saisie par l'utilisateur
    Si la chaine récupérée n'est pas valide, on appelle récursivement la fonction pour en obtenir une nouvelle"""

    lettre = input("Tapez une lettre : ")
    # On met la lettre en minuscules
    lettre = lettre.lower()
    if not lettre.isalpha() or len(lettre)>1:
        print("Vous n'avez pas saisi une lettre valide.")
        # On appelle de nouveau la fonction pour avoir une nouvelle chaine
        return recup_lettre()
    else:
        return lettre

# Fonctions du jeu

def choisir_mot():
    """Fonction renvoyant le mot choisit dans la liste des mots liste_mots"""

    return choice(liste_mots)

def recup_mot_masque(mot_complet,lettres_trouvees):
    """Fonction renvoyant le mot masqué en focntion de :
    - mot d'origine (type str)
    - lettres trouvées (type list)
    Renvoi le mot avec des * à la place des lettres manquantes"""

    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque

#os.system("pause")
