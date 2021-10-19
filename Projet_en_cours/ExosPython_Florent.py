import math, random

# Premier exercice: les impairs

import math
def nb_impair(param1, param2):

    a = math.floor(param1)
    b = math.floor(param2)

    for i in range(a,b,1):
        if ((a + i) % 2) != 0:
            print(i)

nb_impair(42.75,52.23)


# Deuxième exercice: Jeu du plus ou moins

import random, sys

def JeuDuPlusOuMoins():

    nb_recherche = random.randint(1,100)
    print(nb_recherche) 
# A activer pour trouver le nombre avant la boucle et tester le félicitations.

    choix_user = float(input())
    compteur = 1

    while choix_user != nb_recherche:
    
        if choix_user < nb_recherche:
            print("La valeur recherchée est plus grande.")
            if choix_user < 0:
                print("La valeur doit être supérieure à 0")
            choix_user = float(input())

        else :
            print("La valeur recherchée est plus petite.")
            if choix_user > 100:
                print("La valeur doit être supérieure à 100")
            choix_user = float(input())

        compteur += 1

    print(f"Vous avez trouvé en {compteur} fois, félicitations!")
    print("Voulez-vous rejouer? Si oui, tapez 0.")
    rejouer = int(input())

    if rejouer == 0:
        JeuDuPlusOuMoins()
    else :
        sys.exit()

JeuDuPlusOuMoins()



# Troisième exercice: Les plus grands nombres

# import random

def PlusGrandsNombres(taille,nb_entiers):

    import random
    liste_entiers = [random.randint(0,99) for element in range(100)]

    seconde_liste = []

    while len(liste_entiers) > 0:
        m = min(liste_entiers)
        liste_entiers.remove(m)
        seconde_liste.append(m)
    print(seconde_liste[-10:])

# liste_test = [0,1,2,3,4,5,6,87,89,4,36,64,22,26,27,32,29]
# taille = len(liste_test)
# PlusGrandsNombres(taille,10)

# exerice 4: Les algorithmes de tri

def tri_listes(liste):

    for i in range(len(liste)):
        for j in range(i+1, len(liste)):
            if liste[i] > liste[j]:
                liste[i], liste[j] = liste[j], liste[i]
    print(liste) 

liste_test = [0,1,2,3,4,5,6,87,89,4,36,64,22,26,27,32,29]
tri_listes(liste_test)

import time
start_time = time.time()
tri_listes(liste_test)
print("--- %s seconds ---" % (time.time() - start_time))

import time
start_time = time.time()
liste_test.sort()
print("--- %s seconds ---" % (time.time() - start_time))

import time
start_time = time.time()
sorted([0,1,2,3,4,5,6,87,89,4,36,64,22,26,27,32,29])
print("--- %s seconds ---" % (time.time() - start_time))


# exercice 5: Des conversions

def Conversion_Horaire(seconde):

    annee = seconde // 31557600
    annee_reste = seconde % 31557600
    mois = annee_reste // 2629800
    mois_reste = annee_reste % 2629800
    jour = mois_reste // 86400
    jour_reste = mois_reste % 86400
    heure = jour_reste // 3600
    heure_reste = jour_reste % 3600
    minute = heure_reste // 60
    minute_reste = heure_reste % 60
    secondes = minute_reste

  
    print(f"{seconde} secondes correspondent à :" )
    print(f"{annee} annees {mois} mois {jour} jours")
    print(f"{heure} heures {minute} minutes {secondes} secondes")

Conversion_Horaire(3430061596791935255)


def conversion_Km(mile_par_heure):

    a = mile_par_heure

    kilometre_heure = round(a * 1.609,2)
    metre_sec = round((kilometre_heure * 1000) / 3600,2)


    print(f"{kilometre_heure} km/h, ou {metre_sec} m/s")

conversion_Km(19)


# exercice 6 : Triangle de Pascal

# n = lignes , k = colonnes

def trianglePascal(n):
    T = [[0] * (n+1) for p in range(n+1)]
    for n in range(n+1):
        if n == 0:
            T[n][0] = 1
        else:
            for k in range(n+1):
                if k == 0:
                    T[n][0] = 1
                else:
                    T[n][k] = T[n-1][k-1] + T[n-1][k]
    return T
print(trianglePascal(9))


# Exercice 7 : Manipulation de dictionnaires

def echange_Dico(dictionnaire):

    dico_echange = {}
    liste_echange = []
    liste_echange2 = []

    for cle, valeur in dictionnaire.items():
        liste_echange.append(valeur)
        liste_echange2.append(cle)
    
    dico_echange = dict(zip(liste_echange,liste_echange2))
    print(dico_echange)


dico_test = {
    "français": "anglais",
    "chat": "cat",
    "chien": "dog",
    "cochon": "pig",
    "poulet": "chicken",
    "poisson" : "fish",
}

print(dico_test)
(echange_Dico(dico_test))


# Exercice 8 : Manipulation de fichiers textes
# Ne fonctionne pas.

def manipulation_Fichier():
    
    # print("Veuillez entrer le nom du fichier : ")
    file_name = input("Veuillez saisir un nom de fichier: ")

    print("Veuillez taper 1 si vous souhaitez le modifier, ou 2 pour simplement l'afficher")
    choice = int(input())

    while choice != 1 and choice != 2:
        print("Nous vous rappelons qu'il faut taper 1 si vous souhaitez le modifier, ou 2 pour simplement l'afficher")
        choice = int(input())
    
    if choice == 1:
        file = open(file_name, "w")
        while True:
            saisie = (input("Veuillez saisir du texte"))
            if saisie == "":
                break
            else:
                file.write(saisie + '\n')
        file.close()

    else:
        file = open(file_name,"r")
        ligne = file.readlines()
        for i in ligne:
            print(i, end='')
        file.close()

# def tableMulti(n):
#      # Fonction générant la table de multiplication par n (20 termes)
#  # La table sera renvoyée sous forme d'une chaîne de caractères :
#  i, ch = 0, ""
#  while i < 20:
#     i = i + 1
#     ch = ch + str(i * n) + " "
#  return ch
# NomF = input("Nom du fichier à créer : ")
# fichier = open(NomF, 'w')
# # Génération des tables de 2 à 30 :
# table = 2
# while table < 31:
#     fichier.write(tableMulti(table) + '\n')
#     table = table

# print(tableMulti(20))
   
# Triplement des espaces dans un fichier texte.
# Ce script montre également comment modifier le contenu d'un fichier
# en le transférant d'abord tout entier dans une liste, puis en
# ré-enregistrant celle-ci après modifications

# def triplerEspaces(ch):
#  "fonction qui triple les espaces entre mots dans la chaîne ch"
#  i, nouv = 0, ""
#  while i < len(ch):
#  if ch[i] == " ":
#  nouv = nouv + " "
#  else:
#  nouv = nouv + ch[i]
#  i = i +1
#  return nouv
# NomF = input("Nom du fichier : ")
# fichier = open(NomF, 'r+') # 'r+' = mode read/write
# lignes = fichier.readlines() # lire toutes les lignes
# n=0
# while n < len(lignes):
#  lignes[n] = triplerEspaces(lignes[n])
#  n =n+1

# fichier.seek(0) # retour au début du fichier
# fichier.writelines(lignes) # réenregistrement
# fichier.close()


# Exercice 9 : Quelques notes
# Ne fonctionne pas entièrement
import numpy as np, statistics

def notes_Eleves(nb_eleves):

    liste_note = []
    liste_nom = []
    dico_total = {}
    nb_notes = 0

    try:
        while nb_eleves > 0:
            nom_eleve = input()
            liste_nom.append(nom_eleve)
            nb_eleves -= 1
    except ValueError:
        print(liste_nom)
        print("Entrez des noms seulement.")

    try:
        print("Veuillez entrer une note entre 0 et 20 compris: ")
        note = round(float(input()),2)
        while note >= 0 and note <= 20:
            liste_note.append(note)
            note = round(float(input()),2)
            nb_notes += 1
            note_max = max(liste_note)
            note_min = min(liste_note)
            note_moy = statistics.mean(liste_note)
    except ValueError:
        print(liste_note,nb_notes)
        print("N'oubliez pas que seuls les nombres entre 0 et 20 sont acceptés.")
   
    # A partir d'ici le code ne fonctionne plus. 

    # for i in range (len(liste_nom)):
    #     dico_total["nom"] = liste_nom[i]
    # print(dico_total)
       
    print(liste_nom, liste_note,nb_notes,note_max, note_min, note_moy)


print(notes_Eleves(5))



