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

def manipulation_Fichier():
    
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

manipulation_Fichier()

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

def notes_Eleves():
# Pour le "N", il ne faut pas rappeler le dictionnaire car sinon il se vide.

    import numpy as np, statistics
    dico_total = {}
    nom = input("Voulez-vous entrer un nouvel élève (Y/N)?")

    if nom == "Y":
        nom = input("entrer le nouveau nom de l'élève")
        dico_total[nom] = []
        note = input("Saisissez une note")
        while note != "":
            if (float(note)>20) or (float(note)<0): 
                note = input("Saisissez une note")
            else:
                dico_total[nom].append(float(note))
                note = input("Saisissez une note")
    elif nom == "N": 
        nom = input("dis moi le nom")
        dico_total[nom] 
    else:
        print("Il faut entrer Y ou N")

    note_max = max(dico_total[nom])
    note_min = min(dico_total[nom])
    note_moy = statistics.mean(dico_total[nom])
    print(dico_total, note_max,note_min,note_moy)


notes_Eleves()

# Exercice 10: Une première base de données
# souci pour contrôler la saisie du sexe par exemple et l'except.

dico_personne = {}
age = 0
taille = 0
sexe = ""

nom = input("Voulez-vous entrer une nouvelle personne (Y/N)?")

if nom == "Y":
    nom = input("entrer le nouveau nom :")
    dico_personne[nom] = []
    try:
        while ((age ==0) and (taille==0) and (sexe=="") and (sexe != 'M' and sexe != 'F')):
            age = int(input("Saisissez un âge"))
            sexe = input("Saisissez 'F' pour femme et 'M' pour homme")
            taille = float(input("Saisissez une taille en mètres"))
            tuple_personne = (age, sexe, taille)
            dico_personne[nom].append(tuple_personne)
            # dico_personne[nom].append(taille)
            # dico_personne[nom].append(sexe)
    except:
        ValueError ("Il faut remplir correctement la saisie.")
elif nom == "N": 
        nom = input("Précisez le nom")
        dico_personne[nom] 
else:
    print("Il faut entrer Y ou N")

print(dico_personne[nom])

for i in dico_personne[nom]:
    dico_personne[nom][i]
    for j in dico_personne[nom]:
        dico_personne[nom][j]
        

# for clef,valeur in dico_personne.items():
#     print(f"Pour {clef[0]} : {valeur[1][0]} est l'âge,{valeur[1][1]} est le sexe ")
