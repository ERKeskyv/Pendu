"""Ce ficher contient le jeu du pendu.
S'appuie sur les fichiers :
- donnees.py
- fonctions.py"""

# -*-coding:utf-8 -*

#import os

from donnees import nb_coups
from fonctions import recup_nom_utilisateur, recup_lettre, choisir_mot, recup_mot_masque, enregistrer_scores, recup_scores

# On récupère le score
scores = recup_scores()

# On récupère un nom d'utilisateur
utilisateur = recup_nom_utilisateur()

if utilisateur not in scores.keys():
    scores[utilisateur] = 0

# Variable pour savoir quand arrêter la partie
continuer_partie = 'o'

while continuer_partie != 'n':
    print("Joueur {0} : {1} points".format(utilisateur,scores[utilisateur]))
    mot_a_trouver = choisir_mot()
    lettres_trouvees = []
    mot_trouve = recup_mot_masque(mot_a_trouver,lettres_trouvees)
    nb_chances = nb_coups
    while mot_a_trouver != mot_trouve and nb_chances >0:
        print("Mot à trouver {0} (encore {1} chances)".format(mot_trouve,nb_chances))
        lettre = recup_lettre()
        if lettre in lettres_trouvees:
            print("Vous avez déjà choisi cette lettre.")
        elif lettre in mot_a_trouver :
            lettres_trouvees.append(lettre)
            print("Bien joué.")
        else:
            nb_chances -= 1
            print("Dommage.")
        mot_trouve = recup_mot_masque(mot_a_trouver,lettres_trouvees)

    if mot_a_trouver == mot_trouve:
        print("Félicitations ! Vous avez trouvé le mot {0}.".format(mot_a_trouver))
    else :
        print("Pendu ! Vous avez perdu.")

    # On met à jour le score de l'utilisateur
    scores[utilisateur] += nb_chances

    continuer_partie = input("Souhaitez-vous continuer la partie (O/N) ?")
    continuer_partie = continuer_partie.lower()


enregistrer_scores(scores)

print("Vous finissez la partie avec {0} points.".format(scores[utilisateur]))
